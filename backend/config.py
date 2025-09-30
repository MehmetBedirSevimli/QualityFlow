# Ortak ayarlar (IP, port, SQL şifre vb.)

import os
from dotenv import load_dotenv

# .env dosyasını yükle (root dizin)
load_dotenv()

# PLC Ayarları
PLC_IP = os.getenv("PLC_IP", "192.168.0.1")  # Varsayılan: localhost
PLC_RACK = int(os.getenv("PLC_RACK", 0))
PLC_SLOT = int(os.getenv("PLC_SLOT", 1))

# SQL Server Bağlantısı
SQL_CONN_STR = os.getenv("SQLSERVER_DSN")

# Veri Okuma Offsetleri (byte adresleri)
TEMP_OFFSET = 0        # Temperature değişkeni offset
PRESSURE_OFFSET = 4    # Pressure değişkeni offset
MOTORSPEED_OFFSET = 8  # MotorSpeed değişkeni offset
COUNTER_OFFSET = 12    # CycleCounter değişkeni offset
DATA_SIZE = 16         # Toplam okunacak byte sayısı
