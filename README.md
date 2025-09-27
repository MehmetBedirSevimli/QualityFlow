# Akıllı Üretim Hattı İzleme ve Anomali Tespiti

## 📌 Projenin Amacı
Bu projenin amacı, fabrika ortamını simüle ederek SCADA/PLC tabanlı üretim hattı verilerinin (sıcaklık, basınç, akış hızı, motor durumu, arıza sinyali vb.) toplanması, SQL veritabanına kaydedilmesi ve Python tabanlı makine öğrenmesi algoritmaları ile işlenmesidir.  
Amaç; üretim hattında anormalliklerin tespiti ve kestirimci bakım senaryolarının uygulanmasıdır.

---

## 🛠️ Kullanılacak Teknolojiler (Versiyonlar)
- **Donanım / Simülasyon**
  - Siemens TIA Portal V19 + PLCSIM V19
  - WinCC Unified Runtime V19 (PC Runtime)

- **Veritabanı**
  - SQL Server 2022 (Docker container)

- **Programlama ve Veri Bilimi**
  - Python 3.11
  - pandas, NumPy, scikit-learn, LightGBM, XGBoost, PyArrow, ONNX, Streamlit, Plotly

- **Altyapı**
  - Docker Desktop 4.x
  - Git & GitHub
  - FastAPI + Uvicorn (API geliştirme)

- **Görselleştirme**
  - Streamlit panel
  - WinCC Unified HMI ekran entegrasyonu

---

## 🚀 Geliştirme Adımları

### 1. Ortam Kurulumu
- Python 3.11 sanal ortam oluşturma  
- Gerekli kütüphanelerin yüklenmesi  
- SQL Server kurulumu ve test veritabanı  
- Docker ve Git altyapısının hazırlanması  
- **TIA Portal V19, S7-PLCSIM V19 ve WinCC Unified (V19) kurulumları**

### 2. Veri Kaynağı (Simülasyon)
- **PLC tarafı**  
  - TIA Portal V19 + PLCSIM ile CPU 1511-1 PN eklendi.  
  - Global tag tablosunda `Temperature`, `Pressure`, `MotorSpeed`, `CycleCounter` oluşturuldu.  
  - `DB_SimState` (Phase, Seed, PressureFaultCounter, MotorStopCounter) tanımlandı.  
  - OB1, **SCL dili** ile yazıldı:  
    - Temperature: 60±10 °C sinüs dalgası + noise  
    - Pressure: 2.0±0.25 bar sinüs + küçük noise  
    - MotorSpeed: 1500±100 kare dalga (1400–1600 RPM)  
    - CycleCounter: sürekli artan sayaç  
  - **Anomali senaryoları eklendi:**  
    - Temperature spike: %1 ihtimalle 85 °C  
    - Pressure sensor fault: %0.5 ihtimalle 5 cycle boyunca 0.0 bar  
    - Motor stop: %0.2 ihtimalle 10 cycle boyunca 0 RPM

- **HMI tarafı (WinCC Unified Runtime V19, PC Runtime)**  
  - HMI Tag’ler tanımlandı (`HMI_Temperature`, `HMI_Pressure`, `HMI_MotorSpeed`, `HMI_CycleCounter`).  
  - PLC tag’leri ile bağlantı kuruldu.  
  - `MainScreen` tasarlandı:  
    - IO field → Temperature (°C, 1 ondalık)  
    - Gauge → Pressure (0–3 bar skala)  
    - Trend Control → MotorSpeed (1000–2000 RPM, 30s zaman penceresi)  
    - IO field (küçük) → CycleCounter (DINT sayaç)  

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
- **TIA Portal V19, S7-PLCSIM V19 ve WinCC Unified (V19) kurulumları yapıldı.**

### Aşama 2 – Veri Kaynağı (Simülasyon)
- TIA Portal V19 + PLCSIM ile sanal veri üretimi yapıldı.  
- OB1 SCL kodu ile Temperature, Pressure, MotorSpeed ve CycleCounter üretildi.  
- Anomali senaryoları eklendi (Temperature spike, Pressure fault, Motor stop).  
- WinCC Unified Runtime (PC Runtime) ekranı tasarlandı: IO field, Gauge, Trend Control.  
- PLC’den üretilen veriler HMI ekranında görselleştirildi.  

---

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
