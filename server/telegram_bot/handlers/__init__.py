from aiogram.types import Message

# from .sign import (  # noqa: F401
#     dumb_handler,
#     get_today_horoscope_by_sign_handler,
# )
# from .start import start_handler  # noqa: F401
from .subscription import register_subscription_message_handlers  # noqa: F401


async def unknown_command_handler(
    message: Message,
):
    """Handler for unknown command."""
    await message.answer(f"Неизвестный ответ: ({message.text})")
