# QualityFlow

## 📌 Proje Tanımı
QualityFlow, üretim hattı verilerini **simülasyon ortamında** üreten, toplayan, analiz eden ve görselleştiren bir endüstriyel veri yönetim projesidir.  
Amaç, gerçek fabrika erişimi olmadan **PLC/SCADA + SQL Server + Python veri bilimi** zincirini uçtan uca simüle etmektir.  

---

## ⚙️ Kullanılan Teknolojiler
- **Python 3.11**  
  - FastAPI (REST API)  
  - Uvicorn (ASGI Server)  
  - Pandas, NumPy, PyArrow (veri işleme)  
  - Scikit-learn, LightGBM, XGBoost (makine öğrenmesi)  
  - SHAP (model açıklanabilirliği)  
  - ONNX + ONNX Runtime (model dağıtımı)  
  - Plotly + Streamlit (dashboard ve görselleştirme)  
  - PyODBC + SQLAlchemy (SQL Server bağlantısı)  

- **Veritabanı**  
  - SQL Server (Docker container)  
  - Opsiyonel: MongoDB (yarı-yapısal log verileri için)  

- **PLC / SCADA**  
  - Siemens TIA Portal  
  - PLCSIM (sanal PLC)  
  - WinCC Runtime (HMI testleri)  

- **Ortam**  
  - Docker Desktop  
  - Git & GitHub  

---

## 🚀 Geliştirme Aşamaları
1. **Ortam Kurulumu**  
   - Python sanal ortam (venv)  
   - Gerekli kütüphaneler kurulumu  
   - Docker üzerinde SQL Server ve opsiyonel MongoDB  

2. **Veri Simülasyonu**  
   - TIA Portal’da pompa, motor, sensörlerle sanal üretim hattı  
   - PLCSIM ile gerçek zamanlı veri üretimi  

3. **Veri Toplama ve Depolama**  
   - Python script ile simülasyon verilerini SQL Server’a yazma  
   - Tablo alanları: `timestamp, device_id, parameter, value`  

4. **Veri İşleme ve Analiz**  
   - Pandas + NumPy ile veri temizleme  
   - ML modelleri (LightGBM/XGBoost) ile anomali tespiti ve trend analizi  
   - Modellerin ONNX formatında kaydedilmesi  

5. **Büyük Veri Senaryosu**  
   - Docker üzerinde Apache Spark ile batch/stream processing denemeleri  

6. **API Katmanı**  
   - FastAPI ile REST API  
   - `/data` → Son verileri döndürme  
   - `/predict` → Arıza tahmini döndürme  
   - JWT ile kimlik doğrulama  

7. **Dashboard ve Görselleştirme**  
   - Streamlit + Plotly arayüzü  
   - Zaman serisi grafikleri, KPI göstergeleri  
   - Rol bazlı kullanıcı girişi  

8. **Dokümantasyon ve Raporlama**  
   - Proje raporu  
   - README + diyagramlar  
   - Canlı demo (Streamlit panel linki)  

---

## 📂 Proje Yapısı (taslak)
```
QualityFlow/
- api/          # FastAPI kodları
- data/         # Örnek veriler
- ml/           # Makine öğrenmesi modelleri
- panel/        # Streamlit dashboard
- infra/        # Docker, veritabanı ayarları
- docs/         # Diyagramlar, raporlar
- README.md
- requirements.txt
```

---

## 📝 Notlar
- Tüm geliştirme **simülasyon ortamında** yapılır, gerçek fabrika verisine ihtiyaç yoktur.  
- İş ilanlarındaki “veri toplama, analiz etme ve görselleştirme” gereksinimleri birebir karşılanır.  
