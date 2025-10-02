# backend/analysis/model_train.py
"""
Model egitim modulu.
Anomali tespiti icin farkli algoritmalar (Isolation Forest, LightGBM, XGBoost) egitilir.
"""

import logging
import pandas as pd
from typing import Optional, Tuple, Any

from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

import lightgbm as lgb
import xgboost as xgb

from backend import config


def train_isolation_forest(
    X: pd.DataFrame,
    contamination: float = config.CONTAMINATION,
    random_state: int = config.RANDOM_STATE,
) -> IsolationForest:
    """
    Isolation Forest modeli egitir.

    Args:
        X (pd.DataFrame): Ozellik matrisi
        contamination (float): Anomali orani
        random_state (int): Tekrarlanabilirlik icin sabit rastgelelik

    Returns:
        IsolationForest: Egitilmis model
    """
    model = IsolationForest(
        contamination=contamination,
        random_state=random_state,
        n_jobs=-1
    )
    model.fit(X)
    logging.info("Isolation Forest modeli egitildi")
    return model


def train_lightgbm(
    X: pd.DataFrame,
    y: pd.Series,
    random_state: int = config.RANDOM_STATE
) -> lgb.Booster:
    """
    LightGBM modeli egitir (denetimli ogrenme).

    Args:
        X (pd.DataFrame): Ozellik matrisi
        y (pd.Series): Etiketler (0: normal, 1: anomali)
        random_state (int): Sabit rastgelelik

    Returns:
        lgb.Booster: Egitilmis LightGBM modeli
    """
    dtrain = lgb.Dataset(X, label=y)
    params = {
        "objective": "binary",
        "metric": "binary_logloss",
        "verbosity": -1,
        "seed": random_state,
    }
    model = lgb.train(params, dtrain, num_boost_round=100)
    logging.info("LightGBM modeli egitildi")
    return model


def train_xgboost(
    X: pd.DataFrame,
    y: pd.Series,
    random_state: int = config.RANDOM_STATE
) -> xgb.Booster:
    """
    XGBoost modeli egitir (denetimli ogrenme).

    Args:
        X (pd.DataFrame): Ozellik matrisi
        y (pd.Series): Etiketler
        random_state (int): Sabit rastgelelik

    Returns:
        xgb.Booster: Egitilmis XGBoost modeli
    """
    dtrain = xgb.DMatrix(X, label=y)
    params = {
        "objective": "binary:logistic",
        "eval_metric": "logloss",
        "seed": random_state,
    }
    model = xgb.train(params, dtrain, num_boost_round=100)
    logging.info("XGBoost modeli egitildi")
    return model


def split_train_test(
    X: pd.DataFrame, y: Optional[pd.Series] = None, test_size: float = 0.2
) -> Tuple[pd.DataFrame, pd.DataFrame, Optional[pd.Series], Optional[pd.Series]]:
    """
    Egitim / test veri setlerini ayirir.

    Args:
        X (pd.DataFrame): Ozellik matrisi
        y (pd.Series, optional): Etiketler
        test_size (float): Test seti orani

    Returns:
        X_train, X_test, y_train, y_test
    """
    if y is not None:
        return train_test_split(X, y, test_size=test_size, random_state=config.RANDOM_STATE)
    else:
        return train_test_split(X, test_size=test_size, random_state=config.RANDOM_STATE)
