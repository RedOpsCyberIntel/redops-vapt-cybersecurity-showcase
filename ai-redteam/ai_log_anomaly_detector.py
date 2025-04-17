 ai_log_anomaly_detector.py
# Analyzes logs using basic NLP to identify suspicious patterns.

import re
from collections import Counter

def extract_logins(log_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()
    return [line for line in lines if "login" in line.lower() or "auth" in line.lower()]

def detect_anomalies(log_lines):
    ips = [re.search(r"\d+\.\d+\.\d+\.\d+", line).group() for line in log_lines if re.search(r"\d+\.\d+\.\d+\.\d+", line)]
    freq = Counter(ips)
    print("Suspicious IPs (repeated attempts):")
    for ip, count in freq.items():
        if count > 5:
            print(f"{ip} => {count} attempts")

if __name__ == "__main__":
    logs = extract_logins("auth.log")
    detect_anomalies(logs)
