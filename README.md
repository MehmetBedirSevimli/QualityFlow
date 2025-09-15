# Akıllı Üretim Hattı İzleme ve Anomali Tespiti

## 📌 Projenin Amacı
Bu projenin amacı, fabrika ortamını simüle ederek SCADA/PLC tabanlı üretim hattı verilerinin (sıcaklık, basınç, akış hızı, motor durumu, arıza sinyali vb.) toplanması, SQL veritabanına kaydedilmesi ve Python tabanlı makine öğrenmesi algoritmaları ile işlenmesidir.  
Amaç; üretim hattında anormalliklerin tespiti ve kestirimci bakım senaryolarının uygulanmasıdır.

---

## 🛠️ Kullanılacak Teknolojiler
- **Donanım / Simülasyon**
  - Siemens TIA Portal + PLCSIM
  - WinCC Runtime (HMI)

- **Veritabanı**
  - SQL Server (alternatif: PostgreSQL)

- **Programlama ve Veri Bilimi**
  - Python (pandas, NumPy, scikit-learn, LightGBM, XGBoost, PyArrow, ONNX, Streamlit, Plotly)

- **Altyapı**
  - Docker
  - Git & GitHub
  - FastAPI + Uvicorn (API geliştirme)

- **Görselleştirme**
  - Streamlit panel
  - HMI ekran entegrasyonu

---

## 🚀 Geliştirme Adımları

### 1. Ortam Kurulumu
- Python 3.11 sanal ortam oluşturma  
- Gerekli kütüphanelerin yüklenmesi  
- SQL Server kurulumu ve test veritabanı  
- Docker ve Git altyapısının hazırlanması  

### 2. Veri Kaynağı (Simülasyon)
- TIA Portal + PLCSIM ile sensör/makine verilerinin simüle edilmesi  
- WinCC Runtime üzerinden HMI ekranında değerlerin görselleştirilmesi  

### 3. Veri Toplama ve Depolama
- Python script’i ile PLC’den veri çekme  
- SQL Server’a tablo bazlı kayıt (timestamp, device_id vb. ile)  

### 4. Veri İşleme ve Analiz
- Python ile veri temizleme ve dönüştürme  
- Anomali tespiti için ML modelleri (scikit-learn, LightGBM, XGBoost)  
- ONNX ile model optimizasyonu ve hızlı tahmin  

### 5. API Katmanı
- FastAPI ile ML modellerinin REST API üzerinden servis edilmesi  
- HMI ve diğer istemcilerin API’ye erişimi  

### 6. Görselleştirme
- Streamlit panelinde grafikler, raporlar, alarmlar  
- HMI ekranına özet bilgiler  

### 7. Dokümantasyon ve Versiyonlama
- `README.md`, kullanım kılavuzları ve proje açıklamaları  
- GitHub repo üzerinden versiyonlama ve işbirliği  

---
