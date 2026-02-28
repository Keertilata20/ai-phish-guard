# 🛡️ AI Phish Guard

Detecting deception before it detects you.

AI Phish Guard is a phishing link detection web app that analyses suspicious URLs using behavioral signals, structural patterns, and multilingual phishing indicators — including Hindi-targeted scam attempts.

It provides users with a clear visual explanation of risk instead of just saying “safe” or “dangerous”.

---

## 🚀 Live Demo

🔗 https://ai-phish-guard.onrender.com

---

## ✨ Features

-  AI-powered phishing detection
-  Short link expansion awareness
-  Behaviour-based risk analysis
-  Domain structure analysis
-  Confidence breakdown
-  Human-readable risk explanation
- 🇮🇳 Hindi phishing detection
-  Dual Language Mode (English / हिंदी)
-  Mobile responsive interface
-  Animated scan timeline

---

## 🧠 Why This Project Matters

Many phishing attacks now target regional language users.

Traditional tools miss:
- Hindi phishing keywords
- Unicode spoofing
- Language-targeted urgency scams

AI Phish Guard bridges that gap.

---

## 🛠️ Tech Stack

Frontend:
- HTML
- CSS
- JavaScript

Backend:
- FastAPI (Python)

Deployment:
- Render

---

## 🧪 Example Detection

The system can flag:

- Shortened phishing links  
- Urgent scam language  
- Suspicious domain structures  
- Hindi phishing wording  
- Unicode deception  

---

## 📊 Detection Signals Used

| Signal | Purpose |
|-------|--------|
| Shortened links | Hide malicious destination |
| Phishing keywords | Urgency & manipulation |
| Domain structure | Fake authority mimicry |
| Hindi keywords | Regional targeting |
| Hindi script usage | Unicode spoof attempts |

---

## 🌐 Language Support

Users can switch between:

- English Mode
- Hindi Mode

All explanations dynamically translate.

---

## 📦 Installation (Local Setup)

```bash
git clone https://github.com/Keertilata20/ai-phish-guard.git
cd ai-phish-guard
pip install -r requirements.txt
uvicorn main:app --reload
