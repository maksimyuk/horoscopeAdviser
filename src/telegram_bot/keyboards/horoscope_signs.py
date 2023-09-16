from functools import lru_cache
from typing import Tuple

from aiogram.types.keyboard_button import KeyboardButton

from db.enums import get_all_horoscope_signs


@lru_cache
def get_all_signs_keyboard_buttons() -> Tuple[KeyboardButton]:
    return tuple(
        KeyboardButton(text=each_sign) for each_sign in get_all_horoscope_signs()
    )
