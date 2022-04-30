import telebot
from server.settings.components.telegram_bot import SECRET_TOKEN
from server.telegram_bot.handlers import send_welcome

bot = telebot.TeleBot(SECRET_TOKEN)


def register_handlers() -> None:
    """Register all handlers to bot."""
    bot.register_message_handler(send_welcome, commands=["start"], pass_bot=True)


def run():
    """Start bot."""
    bot.infinity_polling()


register_handlers()
run()
