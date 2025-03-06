import os
import requests
from dotenv import load_dotenv
from time import time

load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

def interpret_dream(dream_text):
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistral-tiny",  # Still fast
        "messages": [
            {"role": "system", "content": "You are a dream interpretation expert. Provide a concise interpretation in 3-4 lines, focusing on the core meaning without extra sections or formatting. Keep it simple and direct."},
            {"role": "user", "content": f"Interpret this dream: {dream_text}"}
        ]
    }
    start = time()
    response = requests.post(url, json=data, headers=headers)
    end = time()
    print(f"Mistral API call took {end - start:.2f} seconds")

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Sorry, I couldn't interpret your dream right now. (Status: {response.status_code})"