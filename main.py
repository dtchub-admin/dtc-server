import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# توکن ربات تلگرام شما
TELEGRAM_BOT_TOKEN = "8633606355:AAEN35sboCOE8HyfHgRi709Ej3s43pZvbeU"
RENDER_URL = "https://onrender.com"

@app.route('/')
def home():
    return "DTC Server is Live and Connected!"

@app.route('/telegram-webhook', methods=['POST'])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")

        if text == "/start":
            welcome_msg = "به پلتفرم بین‌المللی DTC خوش آمدید! 🚀\nسرور پایتون شما با موفقیت فعال شد و آماده پردازش تسک‌هاست."
            send_telegram_message(chat_id, welcome_msg)

    return jsonify({"status": "success"})

def send_telegram_message(chat_id, text):
    # تصحیح آدرس دقیق API تلگرام
    url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error sending message: {e}")

def set_webhook():
    webhook_url = f"{RENDER_URL}/telegram-webhook"
    # تصحیح اتصال وب‌هوک برای بیدار کردن تلگرام
    url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/setWebhook?url={webhook_url}"
    try:
        res = requests.get(url)
        print(f"Telegram Webhook Response: {res.text}")
    except Exception as e:
        print(f"Error setting webhook: {e}")

# اجرای بیدارباش خودکار
set_webhook()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
