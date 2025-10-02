# backend/analysis/data_loader.py
"""
Veri yukleme modulu.
SQL Server'daki readings tablosundan pandas DataFrame olarak veri ceker.
"""

import pandas as pd
from sqlalchemy import create_engine
import logging
from typing import Optional
from backend import config


# Sabit kolon listesi (projede dokumana gore sabitlenmis)
COLUMNS = "id, timestamp, device_id, temperature, pressure, motorspeed, cyclecounter"


def get_engine():
    """
    SQLAlchemy engine olusturur.
    .env dosyasindaki SQLSERVER_DSN parametresini kullanir.
    """
    if not config.SQL_CONN_STR:
        raise ValueError("SQL_CONN_STR bos. Lutfen .env dosyasini kontrol edin.")
    return create_engine(config.SQL_CONN_STR)


def load_data(table_name: Optional[str] = None, limit: Optional[int] = None) -> pd.DataFrame:
    """
    SQL Server'dan readings verilerini DataFrame olarak yukler.

    Args:
        table_name (str, optional): Tablo adi. Varsayilan config.READINGS_TABLE.
        limit (int, optional): Cekilecek maksimum satir sayisi. Eger None ise tum tablo yuklenir.

    Returns:
        pd.DataFrame: Yuklenen veriler.
    """
    table = table_name or config.READINGS_TABLE

    # SQL sorgusunu hazirla
    if limit:
        query = f"""
        SELECT TOP ({limit}) {COLUMNS}
        FROM {table}
        ORDER BY timestamp ASC
        """
    else:
        query = f"""
        SELECT {COLUMNS}
        FROM {table}
        ORDER BY timestamp ASC
        """

    engine = get_engine()
    try:
        with engine.connect() as conn:
            df = pd.read_sql(query, conn)
        logging.info("Veri basariyla yuklendi: %d satir", len(df))
        return df
    except Exception as e:
        logging.error("Veri yuklenirken hata: %s", str(e))
        raise
