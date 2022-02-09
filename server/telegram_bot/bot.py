
import telebot

from server.settings.components.telegram_bot import SECRET_TOKEN


bot = telebot.TeleBot(SECRET_TOKEN)
