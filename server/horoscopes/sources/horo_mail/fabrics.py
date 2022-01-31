
from server.horoscopes.base.fabrics import SignDrivenRequestFabric
from server.horoscopes.sources.horo_mail.settings import HORO_MAIL_URL


class BaseMailRequestFabric(SignDrivenRequestFabric):
    """
    Base Request fabric for mail sources Horoscopes.

    Only defines base URL.
    """
    base_url: str = HORO_MAIL_URL


class TodayHoroscopeRequestFabric(BaseMailRequestFabric):
    """Request fabric for get today horoscope."""

    def prepare_request_url(self) -> str:
        """Return prepared url for request."""
        url = super().prepare_request_url()

        return f'{url}/{self.sign.value.lower()}/today'
