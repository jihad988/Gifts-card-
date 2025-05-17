from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os  # নতুন লাইন যোগ করুন

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🎮 খেলা শুরু করতে /play লিখুন")

def play(update: Update, context: CallbackContext):
    update.message.reply_text("🚀 Level 1 | মুভস: 300 | ইনকাম: 2,043")

# টোকেন Railway-এর ভেরিয়েবল থেকে নিন (কোডে সরাসরি লিখবেন না!)
TOKEN = os.environ.get("BOT_TOKEN")
updater = Updater(TOKEN)  # বন্ধনী ও কোটেশন চেক করুন
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("play", play))
updater.start_polling()
