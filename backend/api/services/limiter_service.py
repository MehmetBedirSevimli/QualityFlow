# backend/api/services/limiter_service.py
from slowapi import Limiter
from slowapi.util import get_remote_address

# Tum API'lerde ortak limiter nesnesi
limiter = Limiter(key_func=get_remote_address)
