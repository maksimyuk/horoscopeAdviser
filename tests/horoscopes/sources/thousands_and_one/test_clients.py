from unittest.mock import patch

import requests
from server.horoscopes.enums import HoroscopeSigns
from server.horoscopes.sources.thousand_and_one.client import (
    ThousandAndOneClient,
)
from tests.horoscopes.test_base.test_scrappers import HTML_CONTENT_EXAMPLE


class TestThousandAndOneClient:
    """Tests for 1001goroskop client."""

    @patch("server.horoscopes.base.sender.send_request")
    def test_get_horoscope_by_sign(self, patched_send_request):
        response = requests.Response()
        response._content = HTML_CONTENT_EXAMPLE.encode()

        patched_send_request.return_value = response

        today_horoscope = ThousandAndOneClient().get_today_horoscope_by_sign(
            sign=HoroscopeSigns.PISCES
        )

        assert "Par1. Par2." in today_horoscope
