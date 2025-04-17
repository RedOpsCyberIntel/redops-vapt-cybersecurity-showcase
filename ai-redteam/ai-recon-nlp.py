
```python
# ai-recon-nlp.py
# AI-enhanced recon using Google Dorking & NLP entity extraction

import requests
from bs4 import BeautifulSoup
import spacy

nlp = spacy.load("en_core_web_sm")

def google_dork(domain):
    query = f"site:{domain} filetype:pdf OR filetype:docx"
    print(f"Running passive Google Dork: {query}")
    # Simulate result links (replace with real scraper if needed)
    return ["https://example.com/public_resume.pdf"]

def extract_entities_from_url(url):
    print(f"\nExtracting from {url}")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        doc = nlp(text)
        for ent in doc.ents:
            print(f"{ent.label_}: {ent.text}")
    except Exception as e:
        print(f"Error scraping {url}: {e}")

# Run test
targets = google_dork("target-company.com")
for link in targets:
    extract_entities_from_url(link)
