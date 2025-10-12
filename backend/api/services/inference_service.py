import random
from datetime import datetime
import os
import onnxruntime as rt
from dotenv import load_dotenv
from backend.api.schemas.predict_schema import PredictRequest, PredictResponse
from backend.api.utils.model_loader import load_model

load_dotenv()

USE_REAL_MODEL = True  # True: ONNX modeli, False: Dummy

# -----------------------------
# Dummy inference (test amacli)
# -----------------------------
def run_dummy_inference(request: PredictRequest) -> PredictResponse:
    probability = round(random.uniform(0.7, 0.99), 2)
    quality = "OK" if probability > 0.8 else "NOK"

    return PredictResponse(
        model="dummy_model_v1",
        timestamp=datetime.utcnow().isoformat() + "Z",
        prediction={"quality": quality, "probability": probability}
    )

# ---------------------------------
# Gercek ONNX modelden tahmin alma
# ---------------------------------
def run_onnx_inference(request: PredictRequest) -> PredictResponse:
    session = load_model()  # model_loader'dan session getirir
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name

    input_data = [[request.temperature, request.pressure, request.speed]]
    prediction = session.run([output_name], {input_name: input_data})[0][0]

    quality = "OK" if prediction > 0.5 else "NOK"

    return PredictResponse(
        model="isolation_forest.onnx",
        timestamp=datetime.utcnow().isoformat() + "Z",
        prediction={"quality": quality, "probability": float(prediction)}
    )

# ---------------------------------
# Otomatik secim (dummy / gercek)
# ---------------------------------
def run_inference(request: PredictRequest) -> PredictResponse:
    if USE_REAL_MODEL:
        return run_onnx_inference(request)
    return run_dummy_inference(request)
