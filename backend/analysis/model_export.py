# backend/analysis/model_export.py
"""
Model disari aktarma modulu.
Egitilmis modelleri ONNX formatina donusturur ve kaydeder.
"""

import os
import logging
from typing import Any

from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import joblib

from backend import config


def export_to_onnx(model: Any, input_dim: int, filename: str = None) -> str:
    """
    Sklearn tabanli bir modeli ONNX formatina donusturur.

    Args:
        model (Any): Egitilmis sklearn modeli (orn: IsolationForest)
        input_dim (int): Ozellik sayisi
        filename (str, optional): Kaydedilecek dosya adi. Varsayilan config.DEFAULT_MODEL.

    Returns:
        str: Kaydedilen ONNX dosyasinin yolu
    """
    # Dosya adi hazirla
    filename = filename or config.DEFAULT_MODEL
    os.makedirs(config.MODEL_DIR, exist_ok=True)
    filepath = os.path.join(config.MODEL_DIR, filename)

    try:
        initial_type = [("input", FloatTensorType([None, input_dim]))]
        onnx_model = convert_sklearn(
    	model,
    	initial_types=initial_type,
    	target_opset={"": config.ONNX_OPSET, "ai.onnx.ml": config.ONNX_ML_OPSET}
	)




        with open(filepath, "wb") as f:
            f.write(onnx_model.SerializeToString())

        logging.info("Model ONNX formatina donusturuldu: %s", filepath)
        return filepath
    except Exception as e:
        logging.error("Model ONNX donusumunde hata: %s", str(e))
        raise


def save_pickle(model: Any, filename: str = "model.pkl") -> str:
    """
    Modeli pickle (joblib) formatinda kaydeder.

    Args:
        model (Any): Egitilmis sklearn modeli
        filename (str): Kaydedilecek dosya adi

    Returns:
        str: Kaydedilen pickle dosyasinin yolu
    """
    os.makedirs(config.MODEL_DIR, exist_ok=True)
    filepath = os.path.join(config.MODEL_DIR, filename)

    try:
        joblib.dump(model, filepath)
        logging.info("Model pickle formatinda kaydedildi: %s", filepath)
        return filepath
    except Exception as e:
        logging.error("Model pickle kaydinda hata: %s", str(e))
        raise
