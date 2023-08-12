import asyncio

from core.const import HORO_MAIL_SOURCE_URL
from db.enums import HoroscopeSigns
from services.scrappers.base import BasePBasedScrapper
from services.senders.horo_mail.get_today_sign import GetTodaySignProvider
from services.source.base import BaseSource


class HoroMailSource(BaseSource):
    url = HORO_MAIL_SOURCE_URL

    @classmethod
    async def get_today_by_sign(cls, sign: HoroscopeSigns, *args, **kwargs) -> str:
        page = await GetTodaySignProvider(sign=sign, url=cls.url).provide()
        scrapped_data = await BasePBasedScrapper(page).scrap()
        return scrapped_data


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(HoroMailSource.get_today_by_sign(HoroscopeSigns.ARIES))
