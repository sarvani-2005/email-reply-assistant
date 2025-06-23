# reply_generator.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# ✅ Use correct model name for v1
API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"
HEADERS = {"Content-Type": "application/json"}

def generate_reply(email_text, tone="formal"):
    prompt = f"""You are an AI email assistant. Read the email below and write a {tone} reply.

Email:
\"\"\"
{email_text}
\"\"\"

Reply:"""

    body = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=body)
        response.raise_for_status()
        data = response.json()
        return data['candidates'][0]['content']['parts'][0]['text'].strip()
    except Exception as e:
        return f"Error generating reply: {e}"

