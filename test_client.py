import requests
import os
from dotenv import load_dotenv

# .env dosyasindan API_KEY oku
load_dotenv()
API_KEY = os.getenv("API_KEY")

BASE_URL = "http://127.0.0.1:8000"
HEADERS = {"X-API-Key": API_KEY}

def test_health():
    r = requests.get(f"{BASE_URL}/health/")
    print("Health:", r.status_code, r.json())

def test_predict():
    payload = {
        "temperature": 62.5,
        "pressure": 2.1,
        "speed": 1500
    }
    r = requests.post(f"{BASE_URL}/predict/", json=payload, headers=HEADERS)
    print("Predict:", r.status_code, r.json())

def test_logs():
    r = requests.get(f"{BASE_URL}/logs/?limit=5", headers=HEADERS)
    print("Logs:", r.status_code, r.json())

if __name__ == "__main__":
    test_health()
    test_predict()
    test_logs()
