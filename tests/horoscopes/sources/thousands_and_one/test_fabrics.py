import pytest
import requests

from server.horoscopes.enums import HoroscopeSigns
from server.horoscopes.sources.thousand_and_one.fabrics import (
    BaseThousandAndOneRequestFabric,
    TodayHoroscopeRequestFabric,
)
from server.horoscopes.sources.thousand_and_one.settings import (
    THOUSAND_AND_ONE_URL,
)


class TestBaseThousandAndOneRequestFabric:
    """Tests for base 1001horoscope request fabric."""

    @pytest.fixture()
    def created_request(self) -> requests.Request:
        """Returns request created by fabric."""
        fabric = BaseThousandAndOneRequestFabric(sign=HoroscopeSigns.CANCER)
        return fabric.create()

    def test_base_url(self, created_request):
        """Check url for request."""
        assert created_request.url == THOUSAND_AND_ONE_URL

    def test_params(self, created_request):
        """Check params for empty."""
        assert created_request.params == {}

    def test_data(self, created_request):
        """Check body-data for empty."""
        assert created_request.data == {}


class TestTodayHoroscopeRequestFabric:
    """Tests for get today horoscope fabric."""

    @pytest.fixture()
    def created_request(self) -> requests.Request:
        """Returns request created by fabric."""
        fabric = TodayHoroscopeRequestFabric(sign=HoroscopeSigns.CANCER)
        return fabric.create()

    def test_base_url(self, created_request):
        """Check url for request."""
        assert created_request.url == THOUSAND_AND_ONE_URL

    def test_params(self, created_request):
        """Check sign value is in params."""
        assert created_request.params == {"znak": HoroscopeSigns.CANCER.value.lower()}

    def test_data(self, created_request):
        """Check body-data for empty."""
        assert created_request.data == {}
