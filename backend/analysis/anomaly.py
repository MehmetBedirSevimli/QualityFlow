# backend/analysis/anomaly.py
"""
Anomali tespiti modulu.
Egitilmis modellerle tahmin yapar ve sonuclari isaretler.
"""

import logging
import pandas as pd
from typing import Any


def detect_anomalies(model: Any, X: pd.DataFrame) -> pd.Series:
    """
    Verilen model ile anomalileri tahmin eder.

    Args:
        model (Any): Egitilmis ML modeli (IsolationForest, LightGBM, XGBoost)
        X (pd.DataFrame): Ozellik matrisi

    Returns:
        pd.Series: Tahmin edilen etiketler (0 = normal, 1 = anomali)
    """
    if hasattr(model, "predict"):
        y_pred = model.predict(X)

        # IsolationForest -1 (anomaly) / 1 (normal) dondurur → 0/1'e cevrildi
        if set(y_pred) == {-1, 1}:
            y_pred = pd.Series((y_pred == -1).astype(int), index=X.index)
        else:
            y_pred = pd.Series(y_pred, index=X.index)

        logging.info("Anomali tahmini tamamlandi")
        return y_pred
    else:
        raise ValueError("Verilen modelde 'predict' fonksiyonu bulunamadi")


def attach_anomalies(df: pd.DataFrame, y_pred: pd.Series) -> pd.DataFrame:
    """
    Tahmin edilen anomalileri DataFrame'e yeni kolon olarak ekler.

    Args:
        df (pd.DataFrame): Orijinal veriler
        y_pred (pd.Series): Tahmin edilen etiketler (0 = normal, 1 = anomali)

    Returns:
        pd.DataFrame: Yeni 'anomaly' kolonu eklenmis DataFrame
    """
    df = df.copy()
    df["anomaly"] = y_pred
    logging.info("Verilere anomaly kolonu eklendi")
    return df


def detect_and_attach(model: Any, X: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
    """
    Anomali tahmini yapar ve sonuclari DataFrame'e ekler (kisa yol fonksiyonu).

    Args:
        model (Any): Egitilmis ML modeli
        X (pd.DataFrame): Ozellik matrisi
        df (pd.DataFrame): Orijinal veriler

    Returns:
        pd.DataFrame: 'anomaly' kolonu eklenmis DataFrame
    """
    y_pred = detect_anomalies(model, X)
    return attach_anomalies(df, y_pred)
