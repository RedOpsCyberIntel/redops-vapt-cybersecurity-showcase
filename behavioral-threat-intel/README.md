# Behavioral Threat Intelligence & AI Social Engineering Detector

This module demonstrates approaches for detecting AI-generated phishing and next-generation Business Email Compromise (BEC) messages.

- **Datasets**: `sample_emails.csv` and `sample_bec_emails.csv` contain example messages labeled for training.
- **Detectors**: `ai_social_engineering_detector.py` trains a basic logistic regression model while `bec_ai_detector.py` uses sentence-transformer embeddings for BEC threats.
- **NIST Mapping**: see `nist_mapping.md` for relevant IA controls.

## Interactive Usage

```bash
python ai_social_engineering_detector.py
```

You will be prompted to enter email text to classify.

### BEC Detector

```bash
python bec_ai_detector.py
```

Detects business email compromise attempts using sentence-transformer embeddings.

## API Service

A small FastAPI server exposes the detector for programmatic use. Install requirements and start the server:

```bash
pip install -r requirements.txt
uvicorn api_server:app --reload
```

Send a POST request to `http://localhost:8000/detect` with JSON `{"text": "your email"}` to receive a prediction.

### Docker

Build and run the service in Docker:

```bash
docker build -t phishing-detector .
docker run -p 8000:8000 phishing-detector
```
