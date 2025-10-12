# Akıllı Üretim Hattı İzleme ve Anomali Tespiti

## 📌 Projenin Amacı
Bu projenin amacı, fabrika ortamını simüle ederek SCADA/PLC tabanlı üretim hattı verilerinin (sıcaklık, basınç, akış hızı, motor durumu, arıza sinyali vb.) toplanması, SQL veritabanına kaydedilmesi ve Python tabanlı makine öğrenmesi algoritmaları ile işlenmesidir.  
Amaç; üretim hattında anormalliklerin tespiti ve kestirimci bakım senaryolarının uygulanmasıdır.

---

## 🛠️ Kullanılacak Teknolojiler (Versiyonlar)
- **Donanım / Simülasyon**
  - Siemens TIA Portal V19 + S7-PLCSIM Advanced V7.0
  - WinCC Runtime (HMI)

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
  - HMI ekran entegrasyonu

---

## 🚀 Geliştirme Adımları

### 1. Ortam Kurulumu
- Python 3.11 + Virtualenv sanal ortam oluşturma  
- Gerekli kütüphanelerin yüklenmesi  
- SQL Server 2022 + SSMS 
- Docker ve Git altyapısının hazırlanması  
- TIA Portal V19, S7-PLCSIM Advanced ve WinCC Unified (V19) kurulumları

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
- TIA Portal V19, S7-PLCSIM V19 ve WinCC Unified (V19) kurulumları yapıldı.

### Aşama 2 – Veri Kaynağı (Simülasyon)
- TIA Portal V19 + PLCSIM ile sanal veri üretimi yapıldı.  
- OB1 SCL kodu ile Temperature, Pressure, MotorSpeed ve CycleCounter üretildi.  
- Anomali senaryoları eklendi (Temperature spike, Pressure fault, Motor stop).  
- WinCC Unified Runtime (PC Runtime) ekranı tasarlandı: IO field, Gauge, Trend Control.  
- PLC’den üretilen veriler HMI ekranında görselleştirildi.  

---



## ⚙️ Ortam Değişkenleri

Proje ortam değişkenlerini `.env` dosyasında tutar.  

1. `.env.example` dosyasını kopyalayın:  
   ```bash
   cp .env.example .env
   ```

2. `.env` dosyasındaki placeholder değerleri değiştirin:  

```ini
# SQL Server bağlantısı
SQLSERVER_DSN=DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost,1433;DATABASE=QualityFlowDB;UID=sa;PWD=YourPassword;TrustServerCertificate=yes;
```



> ⚠️ `.env` dosyası `.gitignore` içinde olduğundan **GitHub’a yüklenmez**. Sadece `.env.example` paylaşılır.  

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

### Aşama 2 – Veri Kaynağı (Simülasyon)
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


### Aşama 3 – Veri Toplama ve Depolama
- **PLC ile iletişim**: Python’da `snap7` kütüphanesi kullanılarak S7-1500 CPU’ya bağlantı sağlandı. Bağlantı parametreleri (`PLC_IP`, `RACK`, `SLOT`) `.env` dosyası üzerinden yönetilmektedir.
- **Veri okuma**: `plc_client.py` modülü, PLC’nin proses görüntü alanından (`Areas.PE`) sensör ve sayaç değerlerini okur. Okunan değerler:  
  - `Temperature` (°C)  
  - `Pressure` (bar)  
  - `MotorSpeed` (rpm)  
  - `CycleCounter` (döngü sayısı)  
- **Veri tabanına kayıt**: `db_client.py` modülü, okunan verileri SQL Server üzerindeki `dbo.readings` tablosuna kayıt eder. Tablonun yapısı:  
  - `id` (otomatik artan birincil anahtar)  
  - `timestamp` (kayıt zamanı)  
  - `device_id` (PLC kimliği, örn: `PLC_1`)  
  - `temperature`  
  - `pressure`  
  - `motorspeed`  
  - `cyclecounter`  
- **Collector servisi**: `collect.py` script’i ana döngüyü çalıştırır.  
  1. PLC’ye bağlanır.  
  2. Değerleri okur.  
  3. SQL Server’a yazar.  
  4. Log çıktısı üretir.  
  5. Belirlenen süre/döngü sonunda tekrar eder.  
- **Kayıt sınırı**: Collector 50.000 kayıt tamamlandığında otomatik olarak durur. Bu limit test/analiz aşaması için belirlenmiştir.  
- **Doğrulama**: Veriler SQL Server Management Studio (SSMS) üzerinden sorgulandı, hem kayıt sayısı hem de değerlerin doğruluğu teyit edildi.  

#### 🧹 Clean Code Prensipleri
- **Tek sorumluluk prensibi**: Kod parçaları tek bir görev için tasarlandı.  
  - PLC ile bağlantı ve veri okuma: `plc_client.py`  
  - Veritabanı bağlantısı ve kayıt işlemleri: `db_client.py`  
  - Ortak konfigürasyon değerleri: `config.py`  
  - Ana veri toplama döngüsü: `collect.py`  
- **Magic number/string kullanılmaz**:  
  - Sabit offset değerleri (`0, 4, 8, 12, 16`) doğrudan kod içinde değil, `config.py` dosyasında anlamlı sabitler olarak tanımlandı.  
  - IP adresi, rack/slot ve SQL bağlantı bilgileri `.env` dosyasında tutuldu.  
- **Hata yönetimi**:  
  - PLC bağlantısı, veri okuma ve SQL kayıt hataları `try/except` bloklarıyla yakalanıyor.  
  - Hatalar `logging` modülüyle bilgilendirici log mesajlarına dönüştürülüyor.  
- **Okunabilirlik**:  
  - Fonksiyon ve değişken isimleri amacını net şekilde ifade ediyor (`connect_plc`, `read_plc_data`, `insert_reading`).  
  - Gereksiz tekrarlar kaldırıldı, her modül sade tutuldu.  
- **Yapılandırma bağımsızlığı**:  
  - Kodda sabit değer yok. Tüm yapılandırmalar `.env` dosyası veya `config.py` üzerinden yönetiliyor.  

> Kod bu haliyle **temiz, modüler, sürdürülebilir, genişletilebilir ve test edilebilir** bir yapıya sahiptir.

Veri toplama servisini başlat:
```bash
python backend/collect.py
```

### Aşama 4 – Veri İşleme ve Analiz
- **Veri yükleme**:  
  - `data_loader.py` SQL Server’daki `readings` tablosundan verileri çekmek için yazıldı.  
  - Kolonlar sabitlendi: `id, timestamp, device_id, temperature, pressure, motorspeed, cyclecounter`.  
  - `limit` parametresi ile test amaçlı sınırlı veri alınabiliyor.  

- **Ön işleme**:  
  - `preprocess.py` ile ham veriler temizleniyor ve dönüştürülüyor:  
    1. Zaman sırasına göre sıralama  
    2. Tekrarlayan kayıtların temizlenmesi  
    3. Eksik değerlerin silinmesi  
    4. StandardScaler ile özelliklerin normalize edilmesi (`temperature`, `pressure`, `motorspeed`)  

- **Model eğitimi**:  
  - `model_train.py` içinde üç farklı yöntem destekleniyor:  
    - **Isolation Forest** (denetimsiz öğrenme, anomali tespiti için)  
    - **LightGBM** (denetimli)  
    - **XGBoost** (denetimli)  
  - `split_train_test` ile eğitim/test ayrımı yapılabiliyor.  

- **Anomali tespiti**:  
  - `anomaly.py` modülü ile tahminler yapılıyor.  
  - `detect_anomalies`, `attach_anomalies` ve `detect_and_attach` fonksiyonları ile anomaliler `anomaly` kolonu olarak veriye ekliniyor.  

- **Model değerlendirme**:  
  - `evaluate.py` doğruluk metriklerini hesaplıyor: Accuracy, Precision, Recall, F1, Confusion Matrix, Classification Report.  

- **Model dışa aktarma**:  
  - `model_export.py` ONNX dönüşümünü yapıyor.  
  - `skl2onnx` ile ONNX formatında kaydediliyor.  
  - Opset uyumsuzluğu çözülerek `"ai.onnx.ml": 3` parametresi ile başarıyla export edildi.  
  - Alternatif olarak pickle formatı (`joblib`) da destekleniyor.  

- **Ortak importlar**:  
  - `backend/analysis/__init__.py` oluşturuldu.  
  - Tüm fonksiyonlar tek satır import ile çağrılabilir hale getirildi.  

- **Ana akış**:  
  - `analyze.py` ile uçtan uca pipeline kuruldu:  
    1. Veri yükle  
    2. Ön işleme uygula  
    3. Model eğit  
    4. Anomali tespit et ve veriye ekle  
    5. Opsiyonel değerlendirme yap  
    6. Modeli ONNX olarak kaydet  
    7. Kontrol amaçlı ilk 5 satırı ve anomaly dağılımını yazdır  

- **Test sonuçları**:  
  - 50.000 satırlık veri işlendi.  
  - %1.7 oranında (850 satır) anomali tespit edildi.  
  - `models/isolation_forest.onnx` dosyası başarıyla kaydedildi.  

#### 🧹 Clean Code Prensipleri
- **Tek sorumluluk prensibi**: Her modül sadece bir görevi üstleniyor (`data_loader`, `preprocess`, `model_train`, `anomaly`, `evaluate`, `model_export`).  
- **Yapılandırma bağımsızlığı**: Tüm parametreler `.env` ve `config.py` üzerinden yönetiliyor, kod içinde sabit değer yok.  
- **Okunabilirlik ve açıklayıcı isimlendirme**: Fonksiyonlar (`load_data`, `preprocess`, `train_isolation_forest`, `detect_and_attach`) amacını net olarak ifade ediyor.  
- **Docstring kullanımı**: Tüm fonksiyonlarda Python docstring ile açıklamalar mevcut, IDE ve `help()` fonksiyonu üzerinden görülebilir.  
- **Hata yönetimi**: Try/except blokları ve `logging` kullanılarak hata mesajları anlaşılır şekilde loglanıyor.  
- **Modüler yapı**: Ortak importlar için `__init__.py` eklendi, ana akış (`analyze.py`) basitleştirildi.  

## ⚙️ Aşama 5 – API Katmanı (FastAPI ile Makine Öğrenmesi Servisi)

Bu aşamada sistemin veri tahmini ve loglama katmanı geliştirildi. Amaç, modelin (`isolation_forest.onnx`) dış dünyaya güvenli, izlenebilir ve ölçeklenebilir bir RESTful API olarak sunulmasıdır.

---

### 🧩 1. Genel Mimari

```
backend/
└── api/
    ├── main.py                     # Ana uygulama (FastAPI instance)
    ├── config/
    │   └── limiter_config.py       # Rate limiter yapılandırması
    ├── routers/                    # Uç noktalar
    │   ├── health.py               # Sağlık kontrolü
    │   ├── logs.py                 # İstek geçmişi/log kaydı
    │   └── predict.py              # Model tahmin servisi
    ├── schemas/                    # Veri modelleri (Pydantic)
    │   ├── predict_schema.py       # Tahmin girdi/çıktı doğrulama
    │   └── inference_service.py    # Model servis şeması
    ├── services/                   # İş mantığı katmanı
    │   ├── inference_service.py    # ONNX modeli çalıştırır
    │   ├── logging_service.py      # Loglama mekanizması
    │   ├── security_service.py     # API Key doğrulaması
    │   └── limiter_service.py      # Rate limiting yönetimi
    └── utils/
        └── model_loader.py         # Model yükleme yardımcı fonksiyonu
```

Bu yapı klasik katmanlı mimari ilkesine uygundur:
- Routers → HTTP uç noktaları (API entry points)
- Services → İş mantığı ve sistem servisleri
- Schemas → Veri doğrulama ve şema tanımları
- Utils → Yardımcı fonksiyonlar (ör. model yükleme)

---

### 🚀 2. FastAPI Uygulaması

Ana dosya `main.py` üzerinden başlatılır:
- Router kaydı: `/health`, `/predict`, `/logs` uç noktaları yüklendi.
- CORS ve Exception yönetimi yapılandırıldı.
- Rate Limiter ve Security Middleware aktif hale getirildi.

Çalıştırma komutu:
```bash
uvicorn backend.api.main:app --host 0.0.0.0 --port 8000 --reload
```

---

### 🧠 3. Model Yükleme ve Tahmin Akışı

- Model: `isolation_forest.onnx`
- Çalıştırıcı: `onnxruntime.InferenceSession`
- Servis: `inference_service.py`

Akış:
1. İstemci `/predict` üzerinden JSON veri gönderir.
2. `predict_schema.py` veriyi doğrular.
3. Model çalıştırılır ve çıktı üretilir.
4. Sonuç JSON formatında döndürülür.

Örnek çıktı:
```json
{
  "model": "isolation_forest.onnx",
  "timestamp": "2025-10-05T15:37:11Z",
  "prediction": {"quality": "OK", "probability": 1.0}
}
```

---

### 🔒 4. API Key Güvenliği

- Her istekte `X-API-Key` başlığı zorunludur.
- `.env` dosyasındaki değer `security_service.py` ile doğrulanır.
- Hatalı anahtar durumunda 403 döner:
```json
{"detail": "Invalid or missing API key"}
```

Amaç, yalnızca yetkili istemcilerin erişimini sağlamaktır.

---

### 📊 5. Loglama ve İzlenebilirlik

`logging_service.py` her isteği UUID, timestamp, IP, endpoint, istek ve yanıtla birlikte kaydeder. `/logs` uç noktası geçmişi döndürür.

```bash
curl http://127.0.0.1:8000/logs
```

---

### ⏱️ 6. Rate Limiting

`slowapi` ile her istemciye 3 istek/dakika sınırı konuldu. Limit aşıldığında 429 hatası döner:
```json
{"detail": "Rate limit exceeded: 3 per 1 minute"}
```

---

### 🧪 7. Test ve Doğrulama

- `test_client.py` ile `/health`, `/predict`, `/logs` test edildi.
- Curl testleriyle rate limit ve API Key kontrolleri doğrulandı.
- Tüm yanıtlar beklenen formatta döndü.

---

### 🧱 8. Clean Code ve Tasarım Prensipleri

- Katmanlı mimari, tek sorumluluk
- Bağımlılık enjeksiyonu
- Merkezi hata ve log yönetimi
- Docstring ve Türkçe yorumlar (ASCII karakterli)
- Test edilebilir ve ölçeklenebilir yapı

---

### 📘 9. Sonraki Aşamalar

>  HTTPS sertifikasyonu ve istemci erişimi haricinde tüm API bileşenleri tamamlanmıştır.

-  HTTPS ile güvenli iletişim
-  Streamlit ve HMI istemci entegrasyonu


