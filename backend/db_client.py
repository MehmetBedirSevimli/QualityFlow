# SQL bağlantısı ve insert fonksiyonları

import pyodbc
import logging
from datetime import datetime
import config

def connect_db():
    """
    SQL Server'a bağlantı kurar.
    - Bağlantı bilgisi config.SQL_CONN_STR içinden okunur.
    - Bağlantı başarılı ise info log yazar.
    - Başarısız olursa hata fırlatır.
    """
    try:
        conn = pyodbc.connect(config.SQL_CONN_STR)
        logging.info("SQL Server baglantisi basarili.")
        return conn
    except Exception as e:
        logging.error(f"SQL baglanti hatasi: {e}")
        raise

def insert_reading(conn, device_id, readings):
    """
    PLC'den okunan bir satiriveritabanına kaydeder.
    - conn: SQL bağlantısı
    - device_id: PLC kimliği (örn. PLC_1)
    - readings: dict → {"temperature": float, "pressure": float, ...}
    - Basarisi eklemeyi loglar, hata olursa log + raise yapar.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO readings (timestamp, device_id, temperature, pressure, motorspeed, cyclecounter)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            datetime.now(),              # ölçüm zamanı
            device_id,                   # hangi PLC'den geldiği
            readings["temperature"],     # sıcaklık
            readings["pressure"],        # basınç
            readings["motorspeed"],      # motor hızı
            readings["cyclecounter"],    # sayaç
        ))
        conn.commit()
        logging.info(f"Veri kaydedildi: {readings}")
    except Exception as e:
        logging.error(f"SQL insert hatası: {e}")
        raise
