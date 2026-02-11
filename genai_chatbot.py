import requests
import json

API_KEY = "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"
url = "https://openrouter.ai/api/v1/chat/completions"

while True:
    msg = input("you: ")
    if msg.lower() == "exit":
        break

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": msg}]
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        data = response.json()
        print("AI:", data["choices"][0]["message"]["content"])
    else:
        print("Failed to get response:", response.status_code, response.text)