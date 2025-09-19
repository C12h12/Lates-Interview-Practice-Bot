import os
import requests

MODEL_NAME = "gemini-1.5-flash-latest"
API_KEY = "AIzaSyC9AQ0VKIGnkJvVhSfxZntJ6_ARkqpiNWQ"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"

def generator(prompt, max_tokens=150, temperature=0.7):
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        ],
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_tokens
        }
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code != 200:
        print("❌ Error response:", response.text)  # 👈 print Gemini’s detailed error
        response.raise_for_status()

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]


tokenizer = None

LEVEL_DURATIONS = {
    "easy": 15 * 60,
    "moderate": 20 * 60,
    "experienced": 30 * 60
}
