# AI-Driven Phishing Simulation (LLM-Generated)

This RedOps lab used OpenAI’s GPT-4 API to simulate dynamic phishing emails using real-world brand tone analysis.

## 🎯 Objective

Automate the generation of spear phishing emails tailored to:
- HR departments
- Financial officers
- Developers with GitHub credentials

## 📌 Example Prompt (Python API)

```python
prompt = f"""
You are simulating a phishing attack on a financial analyst. Create a fake email from 'payroll@internal-company.com'
asking them to verify their W-2 tax forms. Make it urgent but polite.
"""
