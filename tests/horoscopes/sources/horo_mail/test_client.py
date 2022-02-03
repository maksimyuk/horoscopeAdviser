from server.horoscopes.sources.horo_mail.client import HoroMailClient
from unittest.mock import patch
import requests

from server.horoscopes.enums import HoroscopeSigns
from tests.horoscopes.test_base.test_scrappers import HTML_CONTENT_EXAMPLE


class TestHoroMailClient:
    """Tests for horo.mail.client."""

    @patch("server.horoscopes.base.sender.send_request")
    def test_get_horoscope_by_sign(self, patched_send_request):
        response = requests.Response()
        response._content = HTML_CONTENT_EXAMPLE.encode()

        patched_send_request.return_value = response

        today_horoscope = HoroMailClient().get_today_horoscope_by_sign(sign=HoroscopeSigns.PISCES)

        assert today_horoscope == "Par1. Par2."
