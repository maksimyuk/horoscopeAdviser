import pytest

from services.scrappers.base import BasePBasedScrapper


@pytest.mark.asyncio
async def test_1001_horo__get_today_sign_info(horo_mail_today_page, horo_mail_today):
    sut = BasePBasedScrapper(horo_mail_today_page)

    result = await sut.scrap()

    assert result == horo_mail_today
