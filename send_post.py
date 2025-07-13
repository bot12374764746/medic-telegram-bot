import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_post():
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": "Ты — опытный врач и медицинский эксперт."},
            {"role": "user", "content": "Напиши короткий пост (до 500 символов) на актуальную тему из общей медицины."}
        ]
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

def post_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL,
        "text": text
    }
    requests.post(url, data=payload)

if __name__ == "__main__":
    try:
        text = generate_post()
        post_to_telegram(text)
    except Exception as e:
        print(f"Ошибка: {e}")
