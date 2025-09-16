# config.py
import os
import requests

# Mistral model config
MODEL_NAME = "mistral-large-latest"  # Replace with your desired model
API_KEY = "NLYzVfe404irVCajuuesRFBUt1hqdiVN"  # Set this in your environment variables
API_URL = "https://api.mistral.ai/v1/chat/completions"

# Generator function to replace the old pipeline
def generator(prompt, max_tokens=150, temperature=0.7):
    """
    Mimics transformers pipeline interface.
    Returns the generated text from Mistral API.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

# tokenizer placeholder (not needed for API, but keep for imports)
tokenizer = None

# Interview durations
LEVEL_DURATIONS = {
    "easy":  15* 60,
    "moderate": 20 * 60,
    "experienced": 30 * 60
}
