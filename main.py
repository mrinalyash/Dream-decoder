import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

def interpret_dream(dream_text):
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistral-medium",  # Change model if needed
        "messages": [
            {"role": "system", "content": "You are a dream interpretation expert."},
            {"role": "user", "content": f"My dream: {dream_text}. What does it mean?"}
        ]
    }

    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Sorry, I couldn't interpret your dream right now."
