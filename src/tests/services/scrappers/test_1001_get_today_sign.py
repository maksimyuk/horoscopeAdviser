import pytest

from services.scrappers.thousand_and_one.get_today_sign import GetTodaySignScrapper


@pytest.mark.asyncio
async def test_1001_horo__get_today_sign_info(thousand_and_one_today_page, thousand_and_one_today):
    sut = GetTodaySignScrapper(thousand_and_one_today_page)

    result = await sut.scrap()

    assert result == thousand_and_one_today
