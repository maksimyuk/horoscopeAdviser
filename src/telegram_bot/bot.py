import asyncio

from aiogram import Bot, Dispatcher, Router
from core.config import settings
from telegram_bot.routers.horoscope import horoscope_router

form_router = Router()


async def run(secret_token: str = settings().TELEGRAM_SECRET_TOKEN) -> None:
    bot = Bot(token=secret_token)

    dp = Dispatcher()

    dp.include_router(form_router)
    dp.include_router(horoscope_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(run())
