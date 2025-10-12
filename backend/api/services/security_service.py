# backend/api/services/security_service.py
import os
from fastapi import Header, HTTPException, status
from dotenv import load_dotenv

# .env dosyasindaki degiskenleri yukle
load_dotenv()

# Ortam degiskenlerinden API_KEY degerini cek
API_KEY = os.getenv("API_KEY")

async def verify_api_key(x_api_key: str = Header(...)):
    """
    Her istekte gonderilen API anahtarini dogrular.
    """
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Gecersiz API anahtari"
        )
