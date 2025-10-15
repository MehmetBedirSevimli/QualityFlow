# backend/api/main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from backend.api.routers import health, predict, logs
from backend.api.services.limiter_service import limiter
import os
import uvicorn
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()

# FastAPI uygulaması
app = FastAPI(
    title="QualityFlow API",
    version="1.0.0",
    description="FastAPI tabanlı model tahmin API'si"
)

# Rate limiter middleware bağlantısı
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# Rate limit aşıldığında dönecek hata yanıtı
@app.exception_handler(RateLimitExceeded)
async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": f"Rate limit exceeded: {exc.detail}"}
    )

# Router kayıtları
app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(predict.router, prefix="/predict", tags=["Prediction"])
app.include_router(logs.router, prefix="/logs", tags=["Logs"])

# Başlangıç kontrol
@app.get("/")
async def root():
    return {"message": "QualityFlow API aktif"}

# HTTPS veya HTTP başlatma
if __name__ == "__main__":
    uvicorn.run(
        "backend.api.main:app",
        host=os.getenv("API_HOST", "0.0.0.0"),
        port=int(os.getenv("API_PORT", 8443)),
        ssl_keyfile=os.getenv("SSL_KEY_FILE"),
        ssl_certfile=os.getenv("SSL_CERT_FILE"),
    )
