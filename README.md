# 📈 NVIDIA AI Forecaster: Stock Price Prediction

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/XGBoost-EE4C2C?style=for-the-badge&logo=xgboost&logoColor=white" alt="XGBoost" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Sklearn" />
</p>

## 🌟 Proje Hakkında

**NVIDIA AI Forecaster**, NVIDIA (NVDA) hisse senedi fiyatlarını analiz eden ve **XGBoost** algoritması kullanarak gelecek projeksiyonları sunan bir web uygulamasıdır. Bu proje, ham borsa verilerini anlamlı özelliklere dönüştürerek (feature engineering) **Recursive Forecasting** ve **Monte Carlo** simülasyonu teknikleriyle birleştirir.

## ✨ Öne Çıkan Özellikler

- **🤖 Akıllı Tahmin Motoru:** XGBoost Regressor ile yüksek doğruluklu fiyat projeksiyonu.
- **🔄 Dinamik Zaman Analizi:** 1 Hafta, 1 Ay, 3 Ay ve 1 Yıllık esnek tahmin seçenekleri.
- **📊 Gelişmiş Görselleştirme:** Chart.js ile hem geçmiş trendleri hem de AI tahminlerini birleştiren interaktif grafikler.
- **🎲 Gerçekçi Simülasyon:** Tahminlere piyasa gürültüsü (noise) eklenerek daha doğal borsa hareketleri üretilir.
- **📱 Modern UI:** Dark mode temalı, kullanıcı dostu ve tepkisel (responsive) dashboard tasarımı.
```text
## 📂 Proje Yapısı


NVIDIA-AI-Forecaster/
├── app.py                 # Flask Sunucusu ve Tahmin Algoritması
├── requirements.txt       # Gerekli Kütüphaneler Listesi
├── data/                  # Güncel NVIDIA Borsa Verileri (CSV)
├── models/                # Eğitilmiş Model ve Scaler Dosyaları
├── templates/             # HTML ve JavaScript Arayüz Dosyaları
└── model_training.ipynb   # Model Eğitim Süreci ve Analizler

🧠 Teknik Detaylar
Model eğitimi sırasında aşağıdaki özellik mühendisliği (Feature Engineering) adımları uygulanmıştır:

SMA (Simple Moving Average): 10 ve 50 günlük hareketli ortalamalar.

Daily Return: Günlük yüzde değişim oranları.

Volatilite Analizi: Tahminlerin gerçekçiliğini artırmak için son 30 günün standart sapma verisi kullanılır.


🛠️ Kurulum ve Kullanım

1. Depoyu Klonlayın

git clone [https://github.com/yigiterenalp/NVIDIA-AI-Forecaster.git](https://github.com/yigiterenalp/NVIDIA-AI-Forecaster.git)

cd NVIDIA-AI-Forecaster

2. Gereksinimleri Yükleyin

pip install -r requirements.txt

3. Uygulamayı Başlatın

python app.py

Tarayıcınızda http://127.0.0.1:5000 adresine giderek uygulamayı kullanmaya başlayabilirsiniz.

📝 Lisans
Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına göz atabilirsiniz.
