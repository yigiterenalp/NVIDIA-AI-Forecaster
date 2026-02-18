from flask import Flask, render_template, jsonify, request
import pandas as pd
import numpy as np
import joblib
from datetime import timedelta
import traceback

app = Flask(__name__)

# --- DOSYA YOLLARI ---
MODEL_PATH = 'nvidia_xgb_model.pkl'
SCALER_PATH = 'nvidia_scaler.pkl'
DATA_PATH = 'NVIDIA_Stock_Prices.csv' 

print("Sistem başlatılıyor...")
try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("✅ Model ve Scaler başarıyla yüklendi.")
except Exception as e:
    print(f"❌ BAŞLANGIÇ HATASI: {e}")

def predict_future_days(days_to_predict):
    try:
        # 1. Veriyi Oku
        df = pd.read_csv(DATA_PATH)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values('Date')
        
        # Feature Engineering (Eksik sütunları tamamla)
        df['SMA_10'] = df['Close'].rolling(window=10).mean()
        df['SMA_50'] = df['Close'].rolling(window=50).mean()
        df['Daily_Return'] = df['Close'].pct_change()
        
        df.dropna(inplace=True)
        
        future_df = df.copy()
        future_predictions = []
        
        # Volatilite (Oynaklık) Hesapla
        try:
            recent_volatility = df['Daily_Return'].tail(30).std()
            if np.isnan(recent_volatility): recent_volatility = 0.02
        except:
            recent_volatility = 0.02
        
        print(f"🔄 {days_to_predict} gün tahmin ediliyor (Volatilite: {recent_volatility:.4f})...")

        for i in range(days_to_predict):
            # Ortalamaları güncelle
            future_df['SMA_10'] = future_df['Close'].rolling(window=10).mean()
            future_df['SMA_50'] = future_df['Close'].rolling(window=50).mean()
            future_df['Daily_Return'] = future_df['Close'].pct_change()
            
            last_row = future_df.iloc[-1]
            
            # Model Girdisi
            features_array = np.array([[
                last_row['Close'], last_row['High'], last_row['Low'], 
                last_row['Open'], last_row['Volume'], 
                last_row['SMA_10'], last_row['SMA_50'], last_row['Daily_Return']
            ]])
            
            # Tahmin + Gürültü
            features_scaled = scaler.transform(features_array)
            predicted_trend = model.predict(features_scaled)[0]
            noise = np.random.normal(0, recent_volatility)
            final_return = predicted_trend + noise
            
            # Yeni Fiyat Hesapla
            new_price = last_row['Close'] * (1 + final_return)
            new_date = last_row['Date'] + timedelta(days=1)
            
            # Mum Verileri
            day_variation = new_price * recent_volatility
            new_open = last_row['Close']
            new_high = new_price + abs(day_variation)
            new_low = new_price - abs(day_variation)
            new_volume = last_row['Volume'] * np.random.uniform(0.9, 1.1)

            # Kaydet
            future_predictions.append({
                'date': new_date.strftime('%Y-%m-%d'),
                'price': round(float(new_price), 2)
            })
            
            # Tabloya Ekle
            new_row = pd.DataFrame([{
                'Date': new_date,
                'Close': new_price,
                'High': new_high, 'Low': new_low, 'Open': new_open, 'Volume': new_volume
            }])
            future_df = pd.concat([future_df, new_row], ignore_index=True)

        return future_predictions

    except Exception as e:
        print("❌ TAHMİN HATASI:")
        traceback.print_exc()
        raise e

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_prediction', methods=['POST'])
def get_prediction():
    try:
        data = request.get_json()
        days = int(data.get('days', 1))
        
        # 1. Tahmini Yap
        predictions = predict_future_days(days)
        
        # 2. Geçmiş Veriyi Hazırla (DİNAMİK AYAR)
        df = pd.read_csv(DATA_PATH)
        df['Date'] = pd.to_datetime(df['Date'])
        
        if days > 90:
            # Yıllık görünüm için tüm geçmiş
            history = df[['Date', 'Close']].copy()
        else:
            # Kısa vadeli görünüm için son 6 ay
            history = df.tail(180)[['Date', 'Close']].copy()
        
        history_data = []
        for _, row in history.iterrows():
            history_data.append({
                'date': row['Date'].strftime('%Y-%m-%d'),
                'price': round(float(row['Close']), 2)
            })
            
        return jsonify({
            'history': history_data,
            'forecast': predictions,
            'latest_price': history_data[-1]['price'],
            'next_price': predictions[0]['price'],     # Yarınki fiyat
            'final_price': predictions[-1]['price']    # <-- YENİ: Dönem sonundaki fiyat
        })

    except Exception as e:
        print(f"❌ SUNUCU HATASI: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)