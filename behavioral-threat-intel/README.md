# Behavioral Threat Intelligence & AI Social Engineering Detector

This module demonstrates a lightweight approach for detecting AI-generated phishing messages.

- **Dataset**: `sample_emails.csv` contains example messages labeled as `ai` or `human`.
- **Detector**: `ai_social_engineering_detector.py` trains a simple logistic regression model using scikit-learn.
- **NIST Mapping**: see `nist_mapping.md` for relevant IA controls.

## Interactive Usage

```bash
python ai_social_engineering_detector.py
```

You will be prompted to enter email text to classify.

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
