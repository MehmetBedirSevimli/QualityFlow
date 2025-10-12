import os
import uuid
from datetime import datetime
from loguru import logger
from fastapi import Request

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "requests.log")

# Klasor yoksa olustur
os.makedirs(LOG_DIR, exist_ok=True)

# Loguru konfigurasyonu
logger.add(
    LOG_FILE,
    rotation="5 MB",      # 5 MB dolunca yeni dosya
    retention="10 days",  # 10 gun sakla
    compression="zip",    # Eski loglari sikistir
    encoding="utf-8"
)

async def log_request(request: Request, endpoint: str, data: dict, response: dict):
    """
    Her API istegini benzersiz ID ve istemci IP bilgisiyle loglar.
    """
    log_entry = {
        "uuid": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "client_ip": request.client.host if request.client else "unknown",
        "endpoint": endpoint,
        "request": data,
        "response": response
    }
    logger.info(log_entry)
