from unittest.mock import patch

import pytest

from db.enums import HoroscopeSigns
from services.source.horo_mail import HoroMailSource


@pytest.mark.asyncio
@patch("http_requests.client.HTTPClient.get")
async def test_horo__get_today_sign(mocked_http_client, horo_mail_today_page, horo_mail_today):
    mocked_http_client.return_value = horo_mail_today_page

    result = await HoroMailSource.get_today_by_sign(HoroscopeSigns.ARIES)

    assert result == horo_mail_today
