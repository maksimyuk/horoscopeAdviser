import asyncio

from aiogram import Bot, Dispatcher

from core.config import settings
from telegram_bot.routers.common import common_router
from telegram_bot.routers.default_settings import default_settings_router


async def run(secret_token: str = settings().TELEGRAM_SECRET_TOKEN) -> None:
    bot = Bot(token=secret_token)

    dp = Dispatcher()

    dp.include_router(common_router)
    dp.include_router(default_settings_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(run())
