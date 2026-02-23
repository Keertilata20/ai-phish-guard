# AI-Phish-Guard
**Zero-Shot ML Phishing Detection Project**

## Project Features
- **Zero-shot learning**: Detects new phishing campaigns
- **XF-PhishBERT inspired**: High accuracy with minimal training data
- **Multilingual**: English and Hindi phishing detection  
- **Explainable**: Shows exactly why email is flagged

## Live Demo Example
- Input: **Urgent bank update required NOW**
- Output: **PHISH RISK: 92% (urgency manipulation detected)**

## ML Pipeline
- HuggingFace ZeroShot pipeline -> BERT embeddings -> Cosine similarity
- Enron dataset and PhishTank validation

## Project Status
- Model prototype complete  
- Flask web demo  
- Hindi language support
