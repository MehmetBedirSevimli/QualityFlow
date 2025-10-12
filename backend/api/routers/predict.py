# backend/api/routers/predict.py
import os
from fastapi import APIRouter, Depends, Request
from backend.api.schemas.predict_schema import PredictRequest, PredictResponse
from backend.api.services.inference_service import run_inference
from backend.api.services.logging_service import log_request
from backend.api.services.security_service import verify_api_key
from backend.api.services.limiter_service import limiter
from dotenv import load_dotenv

# .env dosyasindaki degiskenleri yukle
load_dotenv()

router = APIRouter()

# .env dosyasindan rate limit degerini oku (varsayilan 3/minute)
RATE_LIMIT = os.getenv("RATE_LIMIT", "3/minute")

@router.post(
    "/", 
    response_model=PredictResponse, 
    dependencies=[Depends(verify_api_key)]
)
@limiter.limit(RATE_LIMIT)
async def predict(request_data: PredictRequest, request: Request):
    """
    Model tahmin istegi (gercek ONNX veya dummy).
    """
    # Tahmin islemini calistir
    result = run_inference(request_data)

    # UUID ve IP bilgisiyle log kaydi olustur
    await log_request(request, "/predict", request_data.dict(), result.dict())

    return result
