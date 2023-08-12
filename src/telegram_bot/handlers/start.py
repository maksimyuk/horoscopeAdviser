from telebot import TeleBot
from telebot.types import Message


def start_handler(message: Message, bot: TeleBot):
    """Process start command."""
    welcome_message = (
        "Бот возвращающий данные по гороскопу "
        "на согласно выбранному знаку зодиака и источнику. "
    )
    bot.reply_to(message, welcome_message)
