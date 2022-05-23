from server.horoscopes.enums import get_all_horoscope_signs
from telebot import TeleBot
from telebot.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


# https://www.mindk.com/blog/how-to-develop-a-chat-bot/
def subscription_handler(message: Message, bot: TeleBot):
    """Handler for command work with subscription."""
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            "Добавить подписку",
            callback_data="subscription-add",
        )
    )
    markup.row(
        InlineKeyboardButton(
            "Редактировать текущую подписку",
            callback_data="subscription-edit",
        ),
        InlineKeyboardButton(
            "Удалить текущую подписку",
            callback_data="subscription-delete",
        ),
    )

    bot.reply_to(message, "Выберите необходимый пункт", reply_markup=markup)


def subscription_callback_add(call: CallbackQuery, bot: TeleBot) -> None:
    """Callback handler for add subscription."""
    bot.reply_to(
        call.message, "Добавление подписки пользователя будет реализован позже."
    )


def subscription_callback_edit(call: CallbackQuery, bot: TeleBot) -> None:
    """Callback handler for edit subscription."""
    bot.reply_to(
        call.message, "Редактирование подписки пользователя будет реализован позже."
    )


def subscription_callback_delete(call: CallbackQuery, bot: TeleBot) -> None:
    """Callback handler for edit subscription."""
    bot.reply_to(call.message, "Удаление подписки пользователя будет реализован позже.")


def subscription_callback_add_choose_period(call: CallbackQuery, bot: TeleBot):
    """Callback adding subscription for choose period (daily or weekly)."""
    markup = InlineKeyboardMarkup()

    markup.row(
        InlineKeyboardButton("Ежедневно", callback_data="subscription-add-daily"),
        InlineKeyboardButton("Еженедельно", callback_data="subscription-add-weekly"),
    )
    markup.row(InlineKeyboardButton("Отмена", callback_data="subscription-cancel"))
    bot.reply_to(
        call.message, "Выберите частоту получения гороскопа", reply_markup=markup
    )


def subscription_callback_add_choose_sign(call: CallbackQuery, bot: TeleBot):
    """Callback adding subscription for choose sign."""
    markup = InlineKeyboardMarkup()

    for sign in get_all_horoscope_signs():
        markup.row(
            InlineKeyboardButton(
                "Добавить подписку",
                callback_data=f"subscription-add-sign-{sign}",
            )
        )

    markup.row(
        InlineKeyboardButton("Отмена", callback_data="subscription-cancel"),
    )
    bot.reply_to(call.message, "Выберите знак гороскопа", reply_markup=markup)
