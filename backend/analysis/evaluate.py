# backend/analysis/evaluate.py
"""
Model degerlendirme modulu.
Tahmin sonuclarinin performansini olcer.
"""

import logging
import pandas as pd
from typing import Dict, Any
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)


def evaluate_model(y_true: pd.Series, y_pred: pd.Series) -> Dict[str, Any]:
    """
    Modelin temel siniflandirma metriklerini hesaplar.

    Args:
        y_true (pd.Series): Gercek etiketler (0 = normal, 1 = anomali)
        y_pred (pd.Series): Tahmin edilen etiketler (0 = normal, 1 = anomali)

    Returns:
        Dict[str, Any]: Hesaplanan metrikler
    """
    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1_score": f1_score(y_true, y_pred, zero_division=0),
        "confusion_matrix": confusion_matrix(y_true, y_pred).tolist(),
        "report": classification_report(y_true, y_pred, zero_division=0),
    }

    logging.info("Model degerlendirme tamamlandi")
    return metrics


def print_evaluation(metrics: Dict[str, Any]) -> None:
    """
    Hesaplanan metrikleri okunabilir formatta yazdirir.

    Args:
        metrics (Dict[str, Any]): evaluate_model ciktilari
    """
    print("=== Model Degerlendirme Sonuclari ===")
    print(f"Accuracy : {metrics['accuracy']:.4f}")
    print(f"Precision: {metrics['precision']:.4f}")
    print(f"Recall   : {metrics['recall']:.4f}")
    print(f"F1 Score : {metrics['f1_score']:.4f}")
    print("Confusion Matrix:")
    print(metrics["confusion_matrix"])
    print("Classification Report:")
    print(metrics["report"])
