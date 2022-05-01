from telebot import TeleBot
from telebot.types import Message


def start_handler(message: Message, bot: TeleBot):
    """Process start command."""
    welcome_message = (
        "Бот возвращающий данные по гороскопу "
        "на сегодняшний день согласно выбранному знаку зодиака. "
    )
    bot.reply_to(message, welcome_message)
