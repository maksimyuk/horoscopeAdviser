from unittest.mock import patch

import requests

from server.horoscopes.base.clients import BaseClient
from server.horoscopes.enums import HoroscopeSigns
from tests.horoscopes.test_base.test_methods import SimpleBaseMethod
from tests.horoscopes.test_base.test_scrappers import HTML_CONTENT_EXAMPLE


class SimpleClient(BaseClient):
    """Simple client for test purposes."""

    def get_today_horoscope_by_sign(self, sign: HoroscopeSigns, **kwargs):
        """Returns result of execution by SimpleBaseMethod."""
        return SimpleBaseMethod().execute()


class TestBaseClient:
    """Tests for base client."""

    @patch("server.horoscopes.base.sender.send_request")
    def test_get_today_horoscope_by_sign(self, patched_send_request):
        """Check result is correct."""
        response = requests.Response()
        response._content = HTML_CONTENT_EXAMPLE.encode()

        patched_send_request.return_value = response

        today_horoscope = SimpleClient().get_today_horoscope_by_sign(HoroscopeSigns.LEO)

        assert "List1 List2" in today_horoscope
