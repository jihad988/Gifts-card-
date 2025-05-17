from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🎮 খেলা শুরু করতে /play লিখুন")

def play(update: Update, context: CallbackContext):
    update.message.reply_text("🚀 Level 1 | মুভস: 300 | ইনকাম: 2,043")

# টোকেন এনভায়রনমেন্ট ভেরিয়েবল থেকে নিন (Railway-এ সেট করুন)
TOKEN = os.environ.get("7404609087:AAFracyE45dInf84eaQDOd4kscY9aC7JuGE")
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("play", play))
updater.start_polling()
