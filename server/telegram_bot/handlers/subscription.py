from telebot import TeleBot
from telebot.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


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
