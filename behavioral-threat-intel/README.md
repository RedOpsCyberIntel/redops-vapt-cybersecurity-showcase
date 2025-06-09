# Behavioral Threat Intelligence & AI Social Engineering Detector

This module demonstrates a lightweight approach for detecting AI-generated phishing messages.

- **Dataset**: `sample_emails.csv` contains example messages labeled as `ai` or `human`.
- **Detector**: `ai_social_engineering_detector.py` trains a simple logistic regression model using scikit-learn.
- **NIST Mapping**: see `nist_mapping.md` for relevant IA controls.

Run the detector interactively:

```bash
python ai_social_engineering_detector.py
```

You will be prompted to enter email text to classify.
