from unittest.mock import patch

import pytest

from db.enums import HoroscopeSigns
from services.source.thousand_and_one import ThousandAndOneSource


@pytest.mark.asyncio
@patch("http_requests.client.HTTPClient.get")
async def test_1001__get_today_sign(
    mocked_http_client, thousand_and_one_today_page, thousand_and_one_today
):
    mocked_http_client.return_value = thousand_and_one_today_page

    result = await ThousandAndOneSource.get_today_by_sign(HoroscopeSigns.ARIES)

    assert result == thousand_and_one_today
