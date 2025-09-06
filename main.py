import telebot
import os

TOKEN = os.getenv("TELEGRAMBOTTOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "سلام Soheil! رباتت فعاله 🎉 آماده‌ای برای بازی؟")

bot.polling()