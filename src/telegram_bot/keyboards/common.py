from functools import lru_cache
from typing import Tuple

from aiogram.types.keyboard_button import KeyboardButton

YES = "YES"
NO = "NO"


@lru_cache
def get_yes_no_keyboard_buttons() -> Tuple[KeyboardButton]:
    return tuple(KeyboardButton(text=each_val) for each_val in (YES, NO))
