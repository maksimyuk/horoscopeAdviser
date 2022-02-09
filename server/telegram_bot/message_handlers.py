
from server.telegram_bot.bot import bot


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f'Я отвечаю на ({message.text})')


bot.infinity_polling()
