import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

TOKEN = "8633606355:AAEN35sboCOE8HyfHgRi709Ej3s43pZvbeU"
RENDER_URL = "https://onrender.com"

@app.route('/')
def home():
    return "DTC Server is active!"

@app.route('/telegram-webhook', methods=['POST'])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")

        if text == "/start":
            welcome_msg = "به پلتفرم بین‌المللی DTC خوش آمدید! 🚀\nسرور پایتون شما با موفقیت فعال شد."
            url = f"https://telegram.org{TOKEN}/sendMessage"
            requests.post(url, json={"chat_id": chat_id, "text": welcome_msg})

    return jsonify({"status": "success"})

# سرور خودش به محض روشن شدن، دستور بیدارباش را به تلگرام صادر می‌کند
webhook_url = f"{RENDER_URL}/telegram-webhook"
requests.get(f"https://telegram.org{TOKEN}/setWebhook?url={webhook_url}")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
