from server.horoscopes.enums import (
    get_all_horoscope_signs,
    get_horoscope_sign_enum_by_value,
)
from server.horoscopes.sources.horo_mail.client import HoroMailClient
from server.telegram_bot.bot import bot
from telebot import types


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    """Обработка приветственного сообщения и опроса мануала."""
    welcome_message = (
        "Бот возвращающий данные по гороскопу "
        "на сегодняшний день согласно выбранному знаку зодиака. "
    )
    bot.reply_to(message, welcome_message)


@bot.message_handler(commands=["get_today_horoscope"])
def get_sign(message):
    """Обработка запроса гороскопа."""
    markup = types.ReplyKeyboardMarkup(row_width=3)
    for sign in get_all_horoscope_signs():
        markup.add(types.KeyboardButton(sign))

    bot.reply_to(message, "Выберите знак зодиака:", reply_markup=markup)


@bot.message_handler(func=lambda m: True)
def get_signs_horoscope(message):
    sign = message.text
    if sign not in get_all_horoscope_signs():
        return

    sign_enum = get_horoscope_sign_enum_by_value(sign)
    horoscope = HoroMailClient().get_today_horoscope_by_sign(sign=sign_enum)

    bot.reply_to(message, f"Ваш гороскоп:\n{horoscope}")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"Неизвестный ответ: ({message.text})")


bot.infinity_polling()
