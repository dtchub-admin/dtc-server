import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# اتصال به ربات تلگرامی شما
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

@app.route('/telegram-webhook', methods=['POST'])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")

        if text == "/start":
            welcome_message = "به پلتفرم بین‌المللی DTC خوش آمدید! 🚀\nسرور پایتون شما با موفقیت فعال شد."
            send_telegram_message(chat_id, welcome_message)

    return jsonify({"status": "success"})

def send_telegram_message(chat_id, text):
    url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
