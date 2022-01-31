from server.horoscopes.enums import HoroscopeSigns
from server.horoscopes.sources.horo_mail.fabrics import (
    BaseMailRequestFabric,
    TodayHoroscopeRequestFabric,
)
from server.horoscopes.sources.horo_mail.settings import HORO_MAIL_URL


class TestBaseMailRequestFabric:
    """Tests for base mail request fabric."""

    def test_base_url(self):
        """Check base url contains URL."""
        fabric = BaseMailRequestFabric(sign=HoroscopeSigns.LEO)

        request = fabric.create()
        assert request.url == HORO_MAIL_URL


class TestTodayHoroscopeRequestFabric:
    """Tests for get today horoscope request fabric."""

    def test_prepare_request(self):
        """Check prepared request is correct."""
        fabric = TodayHoroscopeRequestFabric(sign=HoroscopeSigns.LEO)

        request = fabric.create()
        assert (
            request.url == f"{HORO_MAIL_URL}/{HoroscopeSigns.LEO.value.lower()}/today"
        )

    def test_created_request(self):
        """Check prepared request has got no params and body."""
        fabric = TodayHoroscopeRequestFabric(sign=HoroscopeSigns.LEO)

        request = fabric.create()
        assert not request.data
        assert not request.params
