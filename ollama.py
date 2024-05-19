import requests
import json

def ollama (question):
    answer=""
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "gemma",
        "prompt": question
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        for i in response.content.decode().splitlines():
            answer += json.loads(i)['response']

        return answer
    else:
        print("Failed to generate text. Status code:", response.status_code)
