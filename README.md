# redops-vapt-cybersecurity-showcase
Redacted penetration testing reports, scripts, and methodologies from RedOps Cyber Intelligence Group.

# RedOps VAPT & Cybersecurity Portfolio

Welcome to the official cybersecurity and VAPT showcase for RedOps Cyber Intelligence Group, led by Dr. Sam Wertheim.

This repository includes:
- Sanitized sample reports from real client engagements
- Automation scripts for recon and vulnerability discovery
- OWASP Top 10 testing examples using Burp Suite
- Cloud security examples (AWS IAM, S3 misconfigurations)
- Behavioral threat intelligence examples detecting AI-generated phishing
- Dockerized FastAPI service for AI phishing detection

## Legal Notice
All content is either original or fully redacted to protect client confidentiality.

## Contact
- 🛡️ [Upwork Expert-Vetted Profile](https://www.upwork.com/freelancers/samwertheim)
- 🔗 [LinkedIn](https://linkedin.com/in/samwertheim)
- 🌐 [RedOps Website](https://redopscyberintelligence.com) 

## Running the Phishing Detection API

Build the Docker image and run it locally:

```bash
docker build -t phishing-detector .
docker run -p 8000:8000 phishing-detector
```

