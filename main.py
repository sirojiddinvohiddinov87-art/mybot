import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Telegram Bot Tokeningizni kiriting
BOT_TOKEN = "8968779642:AAFGGByvoyxvvsg1tZp3F8QfOAl0NtKm_ec"

# /start komandasi uchun funksiya
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Botga xush kelibsiz 👋")

if __name__ == "__main__":
    # Konsolda loglarni ko'rish uchun
    logging.basicConfig(level=logging.INFO)

    # Bot ilovasini yaratamiz
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # /start komandasi uchun handlerni ro'yxatdan o'tkazamiz
    app.add_handler(CommandHandler("start", start_command))

    # Botni ishga tushiramiz
    app.run_polling()
