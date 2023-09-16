import asyncio

from core.const import THOUSAND_AND_ONE_SOURCE_URL
from db.enums import HoroscopeSigns
from services.scrappers.thousand_and_one.get_today_sign import GetTodaySignScrapper
from services.senders.thousand_and_one.get_today_sign import GetTodaySignProvider
from services.source.base import BaseSource


class ThousandAndOneSource(BaseSource):
    url = THOUSAND_AND_ONE_SOURCE_URL

    @classmethod
    async def get_today_by_sign(cls, sign: HoroscopeSigns, *args, **kwargs) -> str:
        page = await GetTodaySignProvider(sign=sign, url=cls.url).provide()
        scrapped_data = await GetTodaySignScrapper(page).scrap()
        return scrapped_data


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    x = loop.run_until_complete(ThousandAndOneSource.get_today_by_sign(HoroscopeSigns.ARIES))
    print(x)
