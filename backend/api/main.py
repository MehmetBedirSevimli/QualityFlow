# backend/api/main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from backend.api.routers import health, predict, logs
from backend.api.services.limiter_service import limiter  # Limiter artik ayri servis dosyasinda

# FastAPI uygulamasi
app = FastAPI(
    title="QualityFlow API",
    version="1.0.0",
    description="FastAPI tabanli model tahmin API'si"
)

# Rate limiter middleware baglantisi
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# Rate limit asildiginda donulecek hata yaniti
@app.exception_handler(RateLimitExceeded)
async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": f"Rate limit exceeded: {exc.detail}"}
    )

# Router kayitlari
app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(predict.router, prefix="/predict", tags=["Prediction"])
app.include_router(logs.router, prefix="/logs", tags=["Logs"])

# Baslangic kontrol
@app.get("/")
async def root():
    return {"message": "QualityFlow API aktif"}
