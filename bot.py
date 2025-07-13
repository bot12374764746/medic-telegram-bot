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
    payload = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": "Ты — опытный врач и медицинский эксперт. Твоя задача — писать короткие, полезные и интересные посты для Telegram-канала о здоровье и медицине."},
            {"role": "user", "content": "Напиши короткий пост (до 500 символов) на актуальную тему из общей медицины.Пост должен: быть полезным и легко понятным, содержать практический совет или важный факт, избегать фейков, неточностей и устаревшей информации, не содержать призывов к самолечению. Пример тем: давление, питание, витамины, мифы, вредные привычки, первая помощь, симптомы, профилактика заболеваний."}
        ],
        "max_tokens": 500,
        "temperature": 0.8
    }
    r = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return r.json()["choices"][0]["message"]["content"].strip()

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHANNEL, "text": text, "parse_mode": "HTML"}
    requests.post(url, data=payload)

if __name__ == "__main__":
    post = generate_post()
    send_to_telegram(post)
