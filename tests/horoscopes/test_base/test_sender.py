from unittest.mock import patch

import pytest
import requests
from server.horoscopes.base.sender import BaseRequestsSender
from tests.horoscopes.test_base.test_fabrics import TestRequestFabric


@pytest.fixture()
def request_sender() -> BaseRequestsSender:
    """Fixture for base request sender."""
    return BaseRequestsSender(TestRequestFabric())


@pytest.fixture()
def mocked_response() -> requests.Response:
    """Fixture for example of Response object."""
    mocked_response = requests.Response()
    mocked_response._content = b"test"

    return mocked_response


class TestBaseRequestsSender:
    """Tests for checking sender of requests."""

    @patch("server.horoscopes.base.sender.send_request")
    def test_get_response(self, patched_send_request, request_sender):
        """Check on request returns response."""
        patched_send_request.return_value = requests.Response()

        response = request_sender.get_response()
        assert isinstance(response, requests.Response)

    def test_get_response_encoding_default(self, request_sender):
        """Check default encoding value."""
        response = requests.Response()

        encoding = request_sender.get_response_encoding(response)
        assert encoding == "utf-8"

    def test_get_response_encoding_from_request(self, request_sender):
        """Check encoding value from response."""
        response = requests.Response()
        response.encoding = "windows-1251"

        encoding = request_sender.get_response_encoding(response)
        assert encoding == response.encoding

    @patch("server.horoscopes.base.sender.send_request")
    def test_get_decoded_content(
        self, patched_send_request, request_sender, mocked_response
    ):
        """Check on request returns response content."""
        patched_send_request.return_value = mocked_response

        content = request_sender.get_decoded_content()
        assert isinstance(content, str)
        assert content == mocked_response.content.decode("utf-8")
