import telebot
from server.settings.components.telegram_bot import SECRET_TOKEN
from server.telegram_bot.handlers import (
    get_today_horoscope_by_sign_handler,
    start_handler,
    subscription_callback_add,
    subscription_callback_delete,
    subscription_callback_edit,
    subscription_handler,
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
        subscription_handler,
        commands=["subscription"],
        pass_bot=True,
    )
    bot.register_message_handler(
        unknown_command_handler, func=lambda m: True, pass_bot=True
    )


def register_callback_handlers() -> None:
    """Register all callback handlers to bot."""
    bot.register_callback_query_handler(
        subscription_callback_add,
        func=lambda call: call.data == "subscription-add",
        pass_bot=True,
    )
    bot.register_callback_query_handler(
        subscription_callback_edit,
        func=lambda call: call.data == "subscription-edit",
        pass_bot=True,
    )
    bot.register_callback_query_handler(
        subscription_callback_delete,
        func=lambda call: call.data == "subscription-delete",
        pass_bot=True,
    )
    bot.register_callback_query_handler(
        subscription_callback_add,
        func=lambda call: True,
        pass_bot=True,
    )


def run():
    """Start bot."""
    bot.infinity_polling()


register_message_handlers()
register_callback_handlers()

run()
