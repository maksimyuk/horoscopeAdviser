from telebot import TeleBot
from telebot.types import Message

from .sign import (  # noqa: F401
    dumb_handler,
    get_today_horoscope_by_sign_handler,
)
from .start import start_handler  # noqa: F401
from .subscription import (  # noqa: F401
    subscription_callback_add,
    subscription_callback_delete,
    subscription_callback_edit,
    subscription_handler,
)


def unknown_command_handler(message: Message, bot: TeleBot):
    """Handler for unknown command."""
    bot.reply_to(message, f"Неизвестный ответ: ({message.text})")
