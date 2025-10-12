import random
from datetime import datetime
import onnxruntime as rt
import os
from backend.api.schemas.predict_schema import PredictRequest, PredictResponse

# Varsayilan dummy servis
def run_dummy_inference(request: PredictRequest) -> PredictResponse:
    probability = round(random.uniform(0.7, 0.99), 2)
    quality = "OK" if probability > 0.8 else "NOK"

    return PredictResponse(
        model="dummy_model_v1",
        timestamp=datetime.utcnow().isoformat() + "Z",
        prediction={"quality": quality, "probability": probability}
    )


# Gercek ONNX model servisi (ileride aktiflestirmek icin)
class OnnxInferenceService:
    def __init__(self, model_path: str):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model dosyasi bulunamadi: {model_path}")
        self.session = rt.InferenceSession(model_path)

    def run(self, request: PredictRequest) -> PredictResponse:
        # Giris tensorunu hazirla
        input_data = [[request.temperature, request.pressure, request.speed]]
        input_name = self.session.get_inputs()[0].name
        output_name = self.session.get_outputs()[0].name

        # Model calistir
        pred = self.session.run([output_name], {input_name: input_data})[0][0]

        quality = "OK" if pred > 0.5 else "NOK"

        return PredictResponse(
            model=os.path.basename(self.session._model_path),
            timestamp=datetime.utcnow().isoformat() + "Z",
            prediction={"quality": quality, "probability": float(pred)}
        )
