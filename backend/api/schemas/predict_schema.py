from pydantic import BaseModel
from typing import Dict

# API'ye gelen request yapisi
class PredictRequest(BaseModel):
    temperature: float
    pressure: float
    speed: float

# API'nin donecegi response yapisi
class PredictResponse(BaseModel):
    model: str
    timestamp: str
    prediction: Dict[str, float | str]
