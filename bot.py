# bot.py
import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Загружаем .env (если есть)
load_dotenv()

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Получаем токен
TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise RuntimeError("Установите TELEGRAM_TOKEN в Secrets (Replit)")

# Обработчик /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я философский бот.\n"
        "Задай вопрос — скоро научусь отвечать на основе знаний."
    )

# Временный echo
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    logger.info(f"Получено: {text}")
    await update.message.reply_text(
        f"📩 Я получил: *{text}*\n\n"
        "Скоро я начну использовать философские тексты.",
        parse_mode='Markdown'
    )

# Основная функция
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    logger.info("✅ Бот запущен.")
    app.run_polling()

if __name__ == "__main__":
    main()