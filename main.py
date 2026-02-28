from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import re

app = FastAPI()

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str

# ===============================
# 🔍 Hindi Keyword Detection
# ===============================

hindi_keywords = [
    "खाता", "लॉगिन", "सत्यापन", "केवाईसी",
    "पासवर्ड", "अपडेट", "तुरंत", "अभी"
]

def contains_hindi_keyword(text):
    return any(word in text for word in hindi_keywords)

# ===============================
# 🔍 Hindi Script Detection
# ===============================

def contains_hindi_script(text):
    hindi_pattern = re.compile(r'[\u0900-\u097F]')
    return bool(hindi_pattern.search(text))

# ===============================
# 🚨 Suspicious patterns
# ===============================

shorteners = ["bit.ly", "tinyurl", "goo.gl", "t.co"]
phishing_words = ["verify", "update", "login", "urgent", "bank", "account"]

# ===============================
# 🚀 Scan API
# ===============================

@app.post("/scan")
def scan_url(data: URLRequest):

    url = data.url.lower()
    risk_score = 0

    # ===============================
    # 🔍 Detection Flags
    # ===============================

    is_shortened = any(short in url for short in shorteners)
    has_phishing_words = any(word in url for word in phishing_words)
    has_hindi_phishing_words = contains_hindi_keyword(url)
    has_hindi_script = contains_hindi_script(url)
    suspicious_structure = "-" in url
    has_urgent_words = any(word in url for word in ["urgent", "now", "immediate", "verify"])

    # ===============================
    # 🚨 Risk Scoring
    # ===============================

    if is_shortened:
        risk_score += 0.3

    if has_phishing_words:
        risk_score += 0.25

    if has_hindi_phishing_words:
        risk_score += 0.25

    if has_hindi_script:
        risk_score += 0.20

    if suspicious_structure:
        risk_score += 0.15

    risk_score = min(risk_score, 1.0)

    # ===============================
    # 🎯 Label Logic
    # ===============================

    if risk_score > 0.6:
        label = "phishing"
    elif risk_score > 0.3:
        label = "suspicious"
    else:
        label = "safe"

    # ===============================
    # 🌐 Expanded Link
    # ===============================

    expanded_url = None
    if is_shortened:
        expanded_url = "Expanded destination could not be verified"

    # ===============================
    # 🧠 Confidence
    # ===============================

    confidence = risk_score

    # ===============================
    # 📊 Flags (for explanation engine)
    # ===============================

    flags = {
        "shortened": is_shortened,
        "urgent": has_urgent_words,
        "phishing_words": has_phishing_words,
        "hindi": has_hindi_script,
        "hindi_phishing": has_hindi_phishing_words,
        "structure": suspicious_structure
    }

    return {
        "label": label,
        "confidence": confidence,
        "expanded_url": expanded_url,
        "flags": flags
    }

# ===============================
# 📁 Static Hosting
# ===============================

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")