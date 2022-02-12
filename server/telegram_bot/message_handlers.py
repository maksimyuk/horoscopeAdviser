
from telebot import types

from server.horoscopes.enums import get_all_horoscope_signs
from server.telegram_bot.bot import bot


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Обработка приветственного сообщения и опроса мануала."""
    welcome_message = (
        '''Бот, возвращающий данные по гороскопу 
        на сегодняшний день согласно выбранному знаку зодиака'''
    )
    bot.reply_to(message, welcome_message)


@bot.message_handler(commands=['get_today_horoscope'])
def get_horoscope(message):
    """Обработка запроса гороскопа."""
    markup = types.ReplyKeyboardMarkup(row_width=3)
    for sign in get_all_horoscope_signs():
        markup.add(types.KeyboardButton(sign))

    bot.reply_to(message, "Выберите знак зодиака:", reply_markup=markup)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f'Я отвечаю на ({message.text})')


bot.infinity_polling()
