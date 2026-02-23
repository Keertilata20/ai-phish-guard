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
<img width="1174" height="246" alt="image" src="https://github.com/user-attachments/assets/b4bca548-1744-410e-9870-62bcdb61815b" />




**- API Response**
<img width="1186" height="549" alt="image" src="https://github.com/user-attachments/assets/d31d50c8-b28b-412a-b76d-0a4b0dc96ed3" />





**- Source Code**
<img width="1115" height="810" alt="image" src="https://github.com/user-attachments/assets/2d695ca4-01e5-45a3-aacd-9e2bec7dcf6c" />





**- Swagger Docs**
<img width="1919" height="957" alt="image" src="https://github.com/user-attachments/assets/6ed44932-b55f-4176-aadc-8bae78d72636" />




**- Demo**
<img width="1919" height="936" alt="image" src="https://github.com/user-attachments/assets/58f6b033-82ac-47df-84d7-2470ce654e39" />





