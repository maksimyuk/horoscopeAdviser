from unittest.mock import patch

import pytest
import requests

from server.horoscopes.enums import HoroscopeSigns
from server.horoscopes.sources.horo_mail.methods import GetTodayPrediction
from tests.horoscopes.test_base.test_scrappers import HTML_CONTENT_EXAMPLE


class TestGetTodayPrediction:
    """Tests for checking work of GetTodayPrediction method."""

    @pytest.fixture()
    def method(self) -> GetTodayPrediction:
        """Returns instantiated simple base method."""
        return GetTodayPrediction()

    @patch("server.horoscopes.base.sender.send_request")
    def test_execute(self, patched_send_request, method):
        """Check method returns correct data."""
        response = requests.Response()
        response._content = HTML_CONTENT_EXAMPLE.encode()

        patched_send_request.return_value = response

        content = method.execute(sign=HoroscopeSigns.LEO)
        assert "Par1. Par2." in content
