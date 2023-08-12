from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    Message,
    ParseMode,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.markdown import bold, text
from db.enums import get_all_horoscope_signs
from src.horoscopes.services import UserManager
from src.telegram_bot.states import AddSubscriptionStates

AVAILABLE_SOURCES = (
    "mail",
    "1001",
)
AVAILABLE_PERIODS = (
    "daily",
    "weekly",
)

SUBSCRIPTION_CB = CallbackData("menu", "action")
SUBSCRIPTION_EDIT_CB = CallbackData("subscription", "action")


async def subscription_handler(message: Message):
    """Handler for command work with subscription."""
    subscription = UserManager().get_instance(telegram_user_id=message.from_user.id)

    markup = InlineKeyboardMarkup()
    if subscription:
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
    else:
        markup.row(
            InlineKeyboardButton(
                "Добавить подписку",
                callback_data="subscription-add",
            ),
        )

    await message.answer("Выберите необходимый пункт", reply_markup=markup)


async def subscription_add_start(message: Message) -> None:
    """Callback handler for add subscription."""
    subscription = UserManager().get_instance(telegram_user_id=message.from_user.id)
    if subscription:
        await message.answer("Вы уже подписались на рассылку.")
        return

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for sign in get_all_horoscope_signs():
        markup.add(KeyboardButton(sign))

    await message.answer("Выберите знак зодиака:", reply_markup=markup)
    await AddSubscriptionStates.waiting_for_sign.set()


async def sign_chosen(message: Message, state: FSMContext):
    """Process user chosen sign and ask for source."""
    await state.update_data(sign=message.text)

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*AVAILABLE_SOURCES)

    await AddSubscriptionStates.next()
    await message.reply("Выберите источник гороскопа", reply_markup=markup)


async def chosen_incorrect_value_from_keyboard(message: Message):
    """Process user chosen sign and ask for source."""
    return await message.reply(
        "Введено некорректное значение. Выберите значение представленное на клавиатуре"
    )


async def source_chosen(message: Message, state: FSMContext):
    """Process user chosen source and ask for period."""
    await state.update_data(source=message.text)

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*AVAILABLE_PERIODS)

    await AddSubscriptionStates.next()
    await message.reply(
        "Выберите периодичность получения гороскопа",
        reply_markup=markup,
    )


async def period_chosen(message: Message, state: FSMContext):
    """Finish processing by add state."""

    async with state.proxy() as data:
        data["period"] = message.text

        markup = ReplyKeyboardRemove()

        await message.reply(
            text(
                text("Добавлен пользователь со следующими данными: "),
                text("Sign: ", bold(data["sign"])),
                text("Source: ", bold(data["source"])),
                text("Period: ", bold(data["period"])),
                sep="\n",
            ),
            reply_markup=markup,
            parse_mode=ParseMode.MARKDOWN,
        )

        # Add user to subscription
        instance, created = UserManager().get_or_create(
            telegram_user_id=message.from_user.id
        )
        if not created:
            if instance:
                await message.reply("Вы уже подписались на рассылку")
            else:
                await message.reply("Что-то пошло не так. Попробуйте ещё раз")

    await state.finish()


def register_add_subscription_message_handlers(dp: Dispatcher) -> None:
    """Register message handlers for add subscription."""
    dp.register_message_handler(subscription_add_start, commands=["subscription_add"])

    dp.register_message_handler(
        chosen_incorrect_value_from_keyboard,
        lambda message: message.text not in (get_all_horoscope_signs()),
        state=AddSubscriptionStates.waiting_for_sign,
    )
    dp.register_message_handler(
        sign_chosen,
        state=AddSubscriptionStates.waiting_for_sign,
    )

    dp.register_message_handler(
        chosen_incorrect_value_from_keyboard,
        lambda message: message.text not in AVAILABLE_SOURCES,
        state=AddSubscriptionStates.waiting_for_source,
    )
    dp.register_message_handler(
        source_chosen,
        state=AddSubscriptionStates.waiting_for_source,
    )

    dp.register_message_handler(
        chosen_incorrect_value_from_keyboard,
        lambda message: message.text not in AVAILABLE_PERIODS,
        state=AddSubscriptionStates.waiting_for_period,
    )
    dp.register_message_handler(
        period_chosen,
        state=AddSubscriptionStates.waiting_for_period,
    )


async def subscription_callback_edit(message: Message) -> None:
    """Callback handler for edit subscription."""
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            "Знак гороскопа",
            callback_data=SUBSCRIPTION_EDIT_CB.new(action="sign"),
        ),
        InlineKeyboardButton(
            "Источник",
            callback_data=SUBSCRIPTION_EDIT_CB.new(action="source"),
        ),
        InlineKeyboardButton(
            "Периодичность",
            callback_data=SUBSCRIPTION_EDIT_CB.new(action="period"),
        ),
    )

    await message.reply(
        text(
            text("Выберите что именно отредактировать."),
            text("Текущие настройки:"),
            text(
                text("Знак: ", bold("ЗНАК ПОЛЬЗОВАТЕЛЯ")),
                text("Источник: ", bold("ИСТОЧНИК ПОЛЬЗОВАТЕЛЯ")),
                text("Периодичность: ", bold("ПЕРИОДИЧНОСТЬ ПОЛЬЗОВАТЕЛЯ")),
                sep="\n",
            ),
            sep="\n",
        ),
        reply_markup=markup,
        parse_mode=ParseMode.MARKDOWN,
    )


async def subscription_callback_edit_sign(query: CallbackQuery):
    """Callback handler for edit subscription sign."""
    await query.message.answer("Редактирование знака")


async def subscription_callback_edit_source(query: CallbackQuery):
    """Callback handler for edit subscription sign."""
    await query.message.answer("Редактирование источника")


async def subscription_callback_edit_period(query: CallbackQuery):
    """Callback handler for edit subscription sign."""
    await query.message.answer("Редактирование периода")


async def subscription_callback_delete(message: Message) -> None:
    """Callback handler for delete subscription."""
    await message.answer("Удаление подписки пользователя будет реализован позже.")


def register_edit_subscription_message_handlers(dp: Dispatcher):
    """Register message handlers for edit subscription."""
    dp.register_message_handler(
        subscription_callback_edit, commands=["subscription_edit"]
    )

    dp.register_callback_query_handler(
        subscription_callback_edit_sign, SUBSCRIPTION_EDIT_CB.filter(action="sign")
    )
    dp.register_callback_query_handler(
        subscription_callback_edit_source, SUBSCRIPTION_EDIT_CB.filter(action="source")
    )
    dp.register_callback_query_handler(
        subscription_callback_edit_period, SUBSCRIPTION_EDIT_CB.filter(action="period")
    )


def register_delete_subscription_message_handlers(dp: Dispatcher):
    """Register message handlers for delete subscription."""
    dp.register_message_handler(
        subscription_callback_delete, commands=["subscription_delete"]
    )


def register_subscription_message_handlers(dp: Dispatcher) -> None:
    """Register all message handlers for subscription."""
    register_add_subscription_message_handlers(dp)
    register_edit_subscription_message_handlers(dp)
    register_delete_subscription_message_handlers(dp)
