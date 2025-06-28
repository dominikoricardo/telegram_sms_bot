
from flask import Flask, request
import requests
import os
from datetime import datetime

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

# 👇 Добавленные разрешённые chat_id
ALLOWED_CHAT_IDS = [
    "89148185"
    "6829346705"# ← ты и любые другие пользователи
]

@app.route("/sms", methods=["POST"])
def sms_handler():
    data = request.get_json()
    raw_msg = data.get("msg") or "пустое сообщение"
    timestamp = int(data.get("ts", 0)) // 1000
    time_str = datetime.fromtimestamp(timestamp).strftime("%d.%m.%Y %H:%M")

    text = f"📩 СМС от банка:\n{raw_msg}\nПолучено: {time_str}"

    # 📤 Рассылаем всем в списке
    for chat_id in ALLOWED_CHAT_IDS:
        requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            params={"chat_id": chat_id, "text": text}
        )

    return "OK", 200
