class PhishingDetector:
    def predict(self, url: str) -> dict:
       
        suspicious = ['bit.ly', 'login', 'verify', 'tinyurl']
        score = sum(1 for word in suspicious if word in url.lower())
        return {"phishing_score": min(score/3, 1.0), "risk": "HIGH" if score > 1 else "LOW"}
