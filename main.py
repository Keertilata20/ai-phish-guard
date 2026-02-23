from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title=" AI Phish Guard", version="1.0")

@app.get("/")
def home():
    return {"message": "Zero-shot phishing detection API online!", "status": " Ready"}

class URLRequest(BaseModel):
    url: str

@app.post("/detect")
def detect_phish(request: URLRequest):
    # Simulate AI phishing detection
    risk_score = 0.92
    is_phish = risk_score > 0.8
    
    return {
        "url": request.url,
        "risk_score": risk_score,
        "is_phishing": is_phish,
        "protection": "BLOCKED" if is_phish else "SAFE"
    }

