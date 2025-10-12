import os
import onnxruntime as rt
from dotenv import load_dotenv

load_dotenv()

MODEL_DIR = os.getenv("MODEL_DIR", "models")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "isolation_forest.onnx")

_model_cache = None

def load_model():
    """
    ONNX modelini tek seferlik yukler.
    """
    global _model_cache
    if _model_cache is not None:
        return _model_cache

    model_path = os.path.join(MODEL_DIR, DEFAULT_MODEL)

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model dosyasi bulunamadi: {model_path}")

    session = rt.InferenceSession(model_path)
    _model_cache = session
    return session
