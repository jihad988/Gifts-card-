from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text("play")

def play(update: Update, context: CallbackContext):
    update.message.reply_text("🚀 Level 1 | move: 300 | Earn: 2,043")

updater = Updater("7404609087:AAFracyE45dInf84eaQDOd4kscY9aC7JuGE")) # 
updater.dispatcher.add_handler(CommandHandler("start"))
updater.dispatcher.add_handler(CommandHandler("play"))
updater.start_polling()
