# recon.py
import whois
import requests

def basic_whois_lookup(domain):
    try:
        w = whois.whois(domain)
        print(f"Domain: {domain}")
        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")
        print(f"Emails: {w.emails}")
    except Exception as e:
        print(f"[!] WHOIS lookup failed: {e}")

def http_headers(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        print(f"[+] HTTP Headers for {domain}")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
    except Exception as e:
        print(f"[!] HTTP header fetch failed: {e}")

if __name__ == "__main__":
    target = input("Enter domain (e.g., example.com): ")
    basic_whois_lookup(target)
    http_headers(target)
