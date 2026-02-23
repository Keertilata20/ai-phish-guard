# AI-Phish-Guard
**Zero-Shot ML Phishing Detection Project**

## Features
- **Zero-shot learning**: Detects new phishing campaigns
- **XF-PhishBERT inspired**: High accuracy with minimal training data
- **Multilingual**: English and Hindi phishing detection  
- **Explainable**: Shows exactly why email is flagged

## Live Demo Example
- Input: **"Urgent bank update required NOW"**
- Output: **PHISH RISK: 92% (urgency manipulation detected)**

## ML Pipeline
- HuggingFace ZeroShot pipeline -> BERT embeddings -> Cosine similarity
- Enron dataset and PhishTank validation

## Tech Stack
-  HuggingFace Transformers
-  Python FastAPI
-  Docker
-  PyTorch
-  Flask Prototype 

## Status
- Model prototype in progress 
- Flask web demo  
- Supports Hindi Language

## Target
  - Accuracy: 95%+
  - Inference time: <50ms
  - Throughput: 100+ req/min

##  Quick Start
- git clone https://github.com/Keertilata20/ai-phish-guard
- cd ai-phish-guard
- pip install -r requirements.txt
- uvicorn main:app --reload

##  AI Phish Guard - Live Demo

**- Terminal**
<img width="1186" height="549" alt="image" src="https://github.com/user-attachments/assets/5b7e8395-0120-47d5-8862-bea07ea6a6a7" />




**- Source Code**
<img width="1115" height="810" alt="image" src="https://github.com/user-attachments/assets/2d695ca4-01e5-45a3-aacd-9e2bec7dcf6c" />




**- API Response Example**
<img width="1909" height="874" alt="image" src="https://github.com/user-attachments/assets/2ffc20e6-c6a3-473b-8cd1-6aad5a568661" />
<img width="1497" height="819" alt="image" src="https://github.com/user-attachments/assets/9ed839b7-2281-43a0-9247-84eb5c77bc86" />
<img width="1354" height="804" alt="image" src="https://github.com/user-attachments/assets/a921c15b-887f-4a65-b737-cee6d7aebc80" />




**- Demo**
<img width="1919" height="936" alt="image" src="https://github.com/user-attachments/assets/58f6b033-82ac-47df-84d7-2470ce654e39" />





