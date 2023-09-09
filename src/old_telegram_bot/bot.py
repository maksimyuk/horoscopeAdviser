import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from src.settings.components.telegram_bot import SECRET_TOKEN
from src.telegram_bot.handlers import (  # get_today_horoscope_by_sign_handler,
    register_subscription_message_handlers,
    unknown_command_handler,
)

logging.basicConfig(level=logging.INFO)


def register_message_handlers(dp: Dispatcher) -> None:
    """Register all message handlers to bot."""
    register_subscription_message_handlers(dp)

    dp.register_message_handler(unknown_command_handler, lambda msg: True)


async def run():
    """Start bot."""
    bot = Bot(token=SECRET_TOKEN)

    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    register_message_handlers(dp)

    await dp.skip_updates()
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(run())
