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

## Geliştirme Aşamaları
### Aşama 1 – Ortam Kurulumu
- Python sanal ortam (`.venv`) oluşturuldu.
- Gerekli bağımlılıklar (`requirements.txt`) yüklendi.
- `requirements-dev.txt` ile geliştirme/test bağımlılıkları ayrıldı.
- Docker Desktop üzerinde SQL Server container kuruldu.
- `QualityFlowDB` veritabanı ve `readings` tablosu oluşturuldu.
- `backend/db.py` ile `.env` üzerinden güvenli bağlantı sağlandı.
- `test_db*.py` dosyaları ile bağlantı, ekleme ve sorgulama testleri yapıldı.

## 🚀 Hızlı Başlatma

Her bilgisayar yeniden başlatıldığında sanal ortam ve Docker container tekrar aktif edilmelidir.

### 1) Sanal ortam (venv) aktive etme
- **Git Bash**
  ```bash
  source .venv/Scripts/activate
  ```
- **PowerShell**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- **CMD**
  ```cmd
  .venv\Scripts\activate.bat
  ```

Pasif etmek için:
```bash
deactivate
```

---

### 2) Docker SQL Server başlatma
Docker Desktop açıldıktan sonra:

```bash
docker start sql-qualityflow
```

Durumu kontrol:
```bash
docker ps
```

Günlükleri görmek:
```bash
docker logs sql-qualityflow --tail 20
```

---