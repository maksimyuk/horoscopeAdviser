from typing import Any

from aiogram import F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove

from services.telegram import TelegramService
from telegram_bot.keyboards.common import NO, YES, get_yes_no_keyboard_buttons
from telegram_bot.keyboards.horoscope_signs import get_all_signs_keyboard_buttons
from telegram_bot.keyboards.sources import get_all_sources_keyboard_buttons

default_settings_router = Router()


class DefaultHoroscopeSettingsStates(StatesGroup):
    # https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html

    source = State()
    sign = State()
    confirm = State()


@default_settings_router.message(Command("set_default_settings"))
async def command_setup_defaults(message: Message, state: FSMContext) -> None:
    # https://mastergroosha.github.io/aiogram-3-guide/fsm/
    await state.set_state(DefaultHoroscopeSettingsStates.source)
    await message.answer(
        "What horoscope source do you prefer?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    *get_all_sources_keyboard_buttons(),
                ],
            ],
            resize_keyboard=True,
        ),
    )


@default_settings_router.message(DefaultHoroscopeSettingsStates.source)
async def process_source(message: Message, state: FSMContext) -> None:
    await state.update_data(source=message.text)
    await state.set_state(DefaultHoroscopeSettingsStates.sign)

    await message.answer(
        f"Okay, you selected {message.text}. What's your sign?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    *get_all_signs_keyboard_buttons(),
                ],
            ],
            resize_keyboard=True,
        ),
    )


@default_settings_router.message(DefaultHoroscopeSettingsStates.sign)
async def process_sign(message: Message, state: FSMContext) -> None:
    data = await state.update_data(sign=message.text)
    await state.set_state(DefaultHoroscopeSettingsStates.confirm)

    await message.answer(text="Alright, let's check your information.")
    await show_summary(message=message, data=data)

    await message.answer(
        "Do you confirm?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    *get_yes_no_keyboard_buttons(),
                ],
            ],
            resize_keyboard=True,
        ),
    )


@default_settings_router.message(DefaultHoroscopeSettingsStates.confirm, F.text.casefold() == YES.lower())
async def process_confirm_ok(message: Message, state: FSMContext) -> None:
    data = await state.get_data()

    await TelegramService().create_or_update_subscription(
        telegram_user_id=message.from_user.id,
        sign=data["sign"],
        source=data["source"],
    )

    await state.clear()
    await message.answer(
        "Saved.",
        reply_markup=ReplyKeyboardRemove(),
    )


@default_settings_router.message(DefaultHoroscopeSettingsStates.confirm, F.text.casefold() == NO.lower())
async def process_confirm_not_ok(message: Message, state: FSMContext) -> None:
    await state.clear()

    await message.answer(text="Okay, let's start from beginning of setting up default.")

    await state.set_state(DefaultHoroscopeSettingsStates.source)

    # FIXME: how not to duplicate code?
    await message.answer(
        "What horoscope source do you prefer?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    *get_all_sources_keyboard_buttons(),
                ],
            ],
            resize_keyboard=True,
        ),
    )


async def show_summary(message: Message, data: dict[str, Any], positive: bool = True) -> None:
    source = data["source"]
    sign = data["sign"]

    text = f"Given data: {sign} from {source}."

    await message.answer(text=text)
