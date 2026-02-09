import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()


# /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот. Напиши мне что-нибудь.")

# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я умею отвечать на сообщения. Просто напиши мне!")

# Обычные сообщения
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"Вы написали: {user_message}")

# Main
def main():
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    if not TOKEN:
        print("Ошибка: TELEGRAM_BOT_TOKEN не найдет в .env файле!")
        return
    OPEN_AI_KEY = os.getenv('OPENAI_API_KEY')
    if not OPEN_AI_KEY:
        print("Ошибка: TELEGRAM_BOT_TOKEN не найдет в .env файле!")
        return

    app = Application.builder().token(TOKEN).build()


    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    
    print("Бот запускается...")
    app.run_polling()
    print("Бот Запустился!")

if __name__ == '__main__':
    main()