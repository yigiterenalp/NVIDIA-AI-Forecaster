\# 📈 NVIDIA AI Forecaster: Stock Price Prediction



!\[Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge\&logo=python)

!\[Framework](https://img.shields.io/badge/Flask-Web%20App-green?style=for-the-badge\&logo=flask)

!\[ML](https://img.shields.io/badge/XGBoost-Forecasting-orange?style=for-the-badge\&logo=xgboost)

!\[License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)



\## 🌟 Proje Hakkında



\*\*NVIDIA AI Forecaster\*\*, finansal zaman serisi analizi yaparak NVIDIA (NVDA) hisse senedi fiyatlarını tahmin eden, makine öğrenmesi tabanlı bir web uygulamasıdır. 



Bu proje, sadece basit bir regresyon yapmak yerine, \*\*Recursive Forecasting (Özyinelemeli Tahmin)\*\* ve \*\*Monte Carlo Simülasyonu\*\* tekniklerini birleştirerek piyasa volatilitesini (oynaklığını) simüle eder. Kullanıcıya interaktif bir dashboard üzerinden 1 haftalık, 1 aylık veya 1 yıllık gelecek projeksiyonları sunar.



\## ✨ Temel Özellikler



\- \*\*🤖 Gelişmiş ML Modeli:\*\* XGBoost algoritması ile eğitilmiş yüksek doğruluklu tahmin motoru.

\- \*\*🔄 Recursive Forecasting:\*\* Model, kendi tahminlerini girdi olarak kullanarak geleceği zincirleme tahmin eder.

\- \*\*📊 Dinamik Volatilite:\*\* Piyasa gürültüsünü (Noise) simüle ederek dümdüz çizgiler yerine gerçekçi, dalgalı fiyat hareketleri üretir.

\- \*\*Time Travel UI:\*\* - \*\*Kısa Vade:\*\* Son 6 aylık veriyi ve yakın geleceği gösterir.

&nbsp; - \*\*Uzun Vade:\*\* 2016'dan bugüne tüm tarihçeyi ve yıllık projeksiyonu gösterir.

\- \*\*⚡ Modern Dashboard:\*\* Flask altyapısı ve Chart.js ile güçlendirilmiş, Dark Mode destekli tepkisel arayüz.



\## 🧠 Teknik Mimari



Proje üç ana katmandan oluşur:



1\.  \*\*Veri İşleme (Data Pipeline):\*\*

&nbsp;   - `pandas` ile zaman serisi manipülasyonu.

&nbsp;   - Feature Engineering: SMA\_10, SMA\_50 (Hareketli Ortalamalar) ve Daily Return (Günlük Getiri) hesaplamaları.

2\.  \*\*Model (Machine Learning):\*\*

&nbsp;   - \*\*Algoritma:\*\* XGBoost Regressor

&nbsp;   - \*\*Eğitim:\*\* 2016-2026 verileriyle eğitim (%80 Train - %20 Test split).

&nbsp;   - \*\*Metrik:\*\* R2 Score ve RMSE optimize edilmiştir.

3\.  \*\*Web Arayüzü (Frontend/Backend):\*\*

&nbsp;   - \*\*Backend:\*\* Flask (Python) API.

&nbsp;   - \*\*Frontend:\*\* HTML5, CSS3 (Bootstrap), JavaScript (Chart.js).



\## 📂 Proje Yapısı



```text

NVIDIA-AI-Forecaster/

│

├── app.py                 # Flask Ana Uygulama Dosyası

├── requirements.txt       # Gerekli Kütüphaneler

├── README.md              # Proje Dokümantasyonu

│

├── models/                # Eğitilmiş Model Dosyaları

│   ├── nvidia\_xgb\_model.pkl

│   └── nvidia\_scaler.pkl

│

├── data/                  # Veri Setleri

│   └── NVIDIA\_Stock\_Prices.csv

│

└── templates/             # Web Arayüzü (Frontend)

&nbsp;   └── index.html

