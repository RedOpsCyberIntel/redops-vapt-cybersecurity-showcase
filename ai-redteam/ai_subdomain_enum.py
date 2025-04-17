# ai_subdomain_enum.py
# This script uses GPT-like fuzzy matching logic to generate subdomain candidates from company names.

import requests
import random

company = input("Enter company name (e.g., acme-corp): ").lower()

common_keywords = ["dev", "test", "vpn", "internal", "mail", "login", "api", "dashboard"]

def generate_candidates(company):
    candidates = []
    for keyword in common_keywords:
        sub = f"{keyword}.{company}.com"
        candidates.append(sub)
    return candidates

def check_subdomains(candidates):
    print("Checking subdomain responses...")
    for sub in candidates:
        try:
            r = requests.get(f"http://{sub}", timeout=2)
            print(f"[+] Found: {sub} | Status: {r.status_code}")
        except:
            print(f"[-] No response: {sub}")

candidates = generate_candidates(company)
check_subdomains(candidates)
