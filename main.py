# main.py
from flask import Flask
from threading import Thread
import os
import subprocess
import sys

# Запускаем бота в отдельном потоке
def run_bot():
    try:
        subprocess.run([sys.executable, "bot.py"], check=True)
    except Exception as e:
        print(f"❌ Ошибка запуска бота: {e}")

# Веб-сервер для keep-alive
app = Flask('')

@app.route('/')
def home():
    return "🧠 Философский бот работает! Он не спит."

def run_web():
    port = int(os.getenv('PORT', 3000))
    app.run(host='0.0.0.0', port=port)

# Запуск
if __name__ == "__main__":
    # Запускаем веб-сервер в потоке
    web_thread = Thread(target=run_web)
    web_thread.start()

    # Запускаем бота
    run_bot()