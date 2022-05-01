from server.horoscopes.enums import get_all_horoscope_signs
from telebot import TeleBot, types


def dumb_handler(call: types.CallbackQuery, bot: TeleBot) -> None:
    """Process get"""
    bot.reply_to(call.message, "Прост")


def get_today_horoscope_by_sign_handler(message: types.Message, bot: TeleBot) -> None:
    """Process get today horoscope command."""
    markup = types.InlineKeyboardMarkup()
    for sign in get_all_horoscope_signs():
        markup.add(types.InlineKeyboardButton(sign, callback_data="dumb_handler"))

    bot.reply_to(message, "Выберите знак зодиака:", reply_markup=markup)
