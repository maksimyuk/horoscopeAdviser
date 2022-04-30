from telebot import TeleBot
from telebot.types import Message


def send_welcome(message: Message, bot: TeleBot):
    """Обработка приветственного сообщения и опроса мануала."""
    welcome_message = (
        "Бот возвращающий данные по гороскопу "
        "на сегодняшний день согласно выбранному знаку зодиака. "
    )
    bot.reply_to(message, welcome_message)
