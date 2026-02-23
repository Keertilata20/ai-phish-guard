from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="🛡️ AI Phish Guard")

# ✅ SERVE YOUR static/ folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ SERVE index.html from static/
@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

# ✅ YOUR SCANNING API
class UrlRequest(BaseModel):
    url: str

@app.post("/scan")
async def scan_url(request: UrlRequest):
    # Simple phishing detection
    suspicious = ['bit.ly', 'tinyurl', 'login', 'verify', 'paypal', 'amazon']
    score = sum(1 for word in suspicious if word.lower() in request.url.lower())
    risk = "HIGH" if score > 1 else "LOW"
    return {"analysis": {"phishing_score": min(score/3, 1.0), "risk": risk}}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
