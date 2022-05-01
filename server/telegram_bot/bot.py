import telebot
from server.settings.components.telegram_bot import SECRET_TOKEN
from server.telegram_bot.handlers import (
    dumb_handler,
    get_today_horoscope_by_sign_handler,
    start_handler,
    unknown_command_handler,
)

bot = telebot.TeleBot(SECRET_TOKEN)


def register_message_handlers() -> None:
    """Register all message handlers to bot."""
    bot.register_message_handler(start_handler, commands=["start"], pass_bot=True)
    bot.register_message_handler(
        get_today_horoscope_by_sign_handler,
        commands=["get_today_horoscope"],
        pass_bot=True,
    )
    bot.register_message_handler(
        unknown_command_handler, func=lambda m: True, pass_bot=True
    )


def register_callback_handlers() -> None:
    """Register all callback handlers to bot."""
    bot.register_callback_query_handler(
        dumb_handler,
        func=lambda call: True,
        pass_bot=True,
    )


def run():
    """Start bot."""
    bot.infinity_polling()


register_message_handlers()
register_callback_handlers()

run()
