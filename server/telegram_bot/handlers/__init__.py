from telebot import TeleBot
from telebot.types import Message

from .sign import (  # noqa: F401
    dumb_handler,
    get_today_horoscope_by_sign_handler,
)
from .start import start_handler  # noqa: F401


def unknown_command_handler(message: Message, bot: TeleBot):
    """Handler for unknown command."""
    bot.reply_to(message, f"Неизвестный ответ: ({message.text})")
