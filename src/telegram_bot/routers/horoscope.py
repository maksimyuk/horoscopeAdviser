from typing import Any

from aiogram import Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup

horoscope_router = Router()


class HoroscopeSettingsStates(StatesGroup):
    # https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html

    source = State()
    sign = State()


@horoscope_router.message(Command("default_settings"))
async def command_setup_defaults(message: Message, state: FSMContext) -> None:
    await state.set_state(HoroscopeSettingsStates.source)
    await message.answer(
        "What horoscope source do you prefer?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Source1"),
                    KeyboardButton(text="Source2"),
                ],
            ],
            resize_keyboard=True,
        ),
    )


@horoscope_router.message(HoroscopeSettingsStates.source)
async def process_source(message: Message, state: FSMContext) -> None:
    await state.update_data(source=message.text)
    await state.set_state(HoroscopeSettingsStates.sign)

    await message.answer(
        f"Okay, you selected {message.text}. What's your sign?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Fish"),
                    KeyboardButton(text="Aries"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@horoscope_router.message(HoroscopeSettingsStates.sign)
async def process_sign(message: Message, state: FSMContext) -> None:
    data = await state.update_data(sign=message.text)
    await state.clear()

    await show_summary(message=message, data=data)


async def show_summary(message: Message, data: dict[str, Any], positive: bool = True) -> None:
    source = data["source"]
    sign = data["sign"]

    text = f"Given data: {sign} from {source}."

    await message.answer(text=text)
