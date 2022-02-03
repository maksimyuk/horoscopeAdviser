from unittest.mock import patch

import pytest
import requests
from server.horoscopes.base.methods import BaseMethod
from server.horoscopes.base.sender import BaseRequestsSender
from tests.horoscopes.test_base.test_fabrics import TestRequestFabric
from tests.horoscopes.test_base.test_scrappers import (
    HTML_CONTENT_EXAMPLE,
    SimpleTagBasedScrapper,
)


class SimpleBaseMethod(BaseMethod):
    """Simple method-class for testing purposes."""

    requests_fabric = TestRequestFabric
    requests_sender = BaseRequestsSender
    response_scrapper = SimpleTagBasedScrapper


class TestBaseMethod:
    """Tests for checking base method."""

    @pytest.fixture()
    def method(self) -> SimpleBaseMethod:
        """Returns instantiated simple base method."""
        return SimpleBaseMethod()

    @patch("server.horoscopes.base.sender.send_request")
    def test_execute(self, patched_send_request, method):
        """Check method returns correct data."""
        response = requests.Response()
        response._content = HTML_CONTENT_EXAMPLE.encode()

        patched_send_request.return_value = response

        content = method.execute()
        assert content == "List1 List2"
