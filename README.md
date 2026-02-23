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
- git clone AI-Phish-Guard
- cd ai-phish-guard
- pip install -r requirements.txt
- uvicorn main:app --reload
