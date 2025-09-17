# config.py
import os
import requests

# Gemini model config
MODEL_NAME = "gemini-1.5-flash-latest"
API_KEY = "AIzaSyBDuQUNB4gra81PPuDytO0O012yErtV9TY"  # Replace with your actual Gemini API key
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"

# Generator function to replace the old pipeline
def generator(prompt, max_tokens=150, temperature=0.7):
    """
    Mimics transformers pipeline interface.
    Returns the generated text from Gemini API.
    """
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_tokens
        }
    }

    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]

# tokenizer placeholder (not needed for API, but keep for imports)
tokenizer = None

# Interview durations
LEVEL_DURATIONS = {
    "easy": 15 * 60,
    "moderate": 20 * 60,
    "experienced": 30 * 60
}