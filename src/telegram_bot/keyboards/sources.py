from functools import lru_cache
from typing import Tuple

from aiogram.types.keyboard_button import KeyboardButton

from db.enums import Sources


@lru_cache
def get_all_sources_keyboard_buttons() -> Tuple[KeyboardButton]:
    return tuple(KeyboardButton(text=source.value) for source in Sources)
