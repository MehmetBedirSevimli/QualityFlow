from fastapi import APIRouter, Request
from datetime import datetime
from backend.api.services.logging_service import log_request

router = APIRouter()

@router.get("/")
async def health_check(request: Request):
    """
    Servis saglik durumunu kontrol eder.
    """
    response = {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    # UUID ve IP log kaydi
    await log_request(request, "/health", {}, response)

    return response
