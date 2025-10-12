from fastapi import APIRouter, Request
from datetime import datetime
import os
from backend.api.services.logging_service import log_request

router = APIRouter()

LOG_FILE = "logs/requests.log"

@router.get("/")
async def get_logs(request: Request, limit: int = 10):
    """
    Son log kayitlarini dondurur.
    Varsayilan limit: 10
    """
    if not os.path.exists(LOG_FILE):
        response = {"logs": []}
        await log_request(request, "/logs", {"limit": limit}, response)
        return response

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    response = {
        "logs": [line.strip() for line in lines[-limit:]],
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    # UUID ve IP log kaydi
    await log_request(request, "/logs", {"limit": limit}, response)

    return response
