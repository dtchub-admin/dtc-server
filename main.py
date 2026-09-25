import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# وارد کردن توکن به صورت کاملاً مستقیم و هاردکد شده بدون دخالت منوهای رندر
TOKEN = "8633606355:AAEN35sboCOE8HyfHgRi709Ej3s43pZvbeU"
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
            welcome_msg = "به پلتفرم بین‌المللی DTC خوش آمدید! 🚀\nسرور پایتون شما با موفقیت فعال شد."
            url = f"https://telegram.org{TOKEN}/sendMessage"
            requests.post(url, json={"chat_id": chat_id, "text": welcome_msg})

    return jsonify({"status": "success"})

# بیدارباش مستقیم با آدرس دهی دستی فرمت استاندارد اینترنت
def set_webhook():
    webhook_url = f"{RENDER_URL}/telegram-webhook"
    target_url = f"https://telegram.org{TOKEN}/setWebhook?url={webhook_url}"
    try:
        res = requests.get(target_url)
        print("Telegram Response:", res.text)
    except Exception as e:
        print("Webhook Error:", e)

set_webhook()

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
