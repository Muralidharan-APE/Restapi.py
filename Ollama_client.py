import requests

def chat(prompt):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)

    return response.json()["response"]


if __name__ == "__main__":
    user_input = input("You: ")
    reply = chat(user_input)
    print("AI:", reply)