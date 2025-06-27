from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/sms", methods=["POST"])
def sms_handler():
    data = request.get_json()
    print("🛠️ Получен JSON:", data)
    message = data.get("message") or "Пустое сообщение"

    text = f"📩 СМС от банка:\n{message}"
    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": text}
    )
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
