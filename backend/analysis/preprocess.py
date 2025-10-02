# backend/analysis/preprocess.py
"""
Veri on isleme modulu.
Eksik veri temizleme, aykiri deger kontrolu, olcekleme gibi islemleri icerir.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
import logging
from typing import Tuple


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tekrarlayan satirlari kaldirir.
    """
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    logging.info("Duplicate kayitlar temizlendi: %d -> %d", before, after)
    return df


def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Eksik (NaN) degerleri siler.
    Ihtiyaca gore burasi ileride imputasyon (ortalama/medyan) ile genisletilebilir.
    """
    before = len(df)
    df = df.dropna()
    after = len(df)
    logging.info("Eksik degerler temizlendi: %d -> %d", before, after)
    return df


def scale_features(df: pd.DataFrame, feature_cols: list[str]) -> Tuple[pd.DataFrame, StandardScaler]:
    """
    Verilen ozellik kolonlarini StandardScaler ile olcekler.
    
    Args:
        df (pd.DataFrame): Giris verisi
        feature_cols (list[str]): Olceklenek kolonlar
    
    Returns:
        Tuple[pd.DataFrame, StandardScaler]: Olceklenmis DataFrame ve scaler nesnesi
    """
    scaler = StandardScaler()
    df[feature_cols] = scaler.fit_transform(df[feature_cols])
    logging.info("Ozellikler olceklendi: %s", feature_cols)
    return df, scaler


def preprocess(df: pd.DataFrame) -> Tuple[pd.DataFrame, StandardScaler]:
    """
    Genel on isleme adimlari:
    1. Zaman sirasina gore sirala
    2. Tekrar kayitlari temizle
    3. Eksik degerleri temizle
    4. Olcekleme uygula
    
    Args:
        df (pd.DataFrame): Giris verisi
    
    Returns:
        Tuple[pd.DataFrame, StandardScaler]: Islenmis veriler ve scaler
    """
    # 1. Zaman sirasi
    df = df.sort_values("timestamp").reset_index(drop=True)
    logging.info("Veriler zaman sirasina gore siralandi")

    # 2. Tekrar kayitlar
    df = remove_duplicates(df)

    # 3. Eksik degerler
    df = handle_missing(df)

    # 4. Ozellikleri olcek
    feature_cols = ["temperature", "pressure", "motorspeed"]
    df, scaler = scale_features(df, feature_cols)

    return df, scaler
