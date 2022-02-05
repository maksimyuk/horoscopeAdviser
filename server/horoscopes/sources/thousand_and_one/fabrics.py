from server.horoscopes.base.fabrics import SignDrivenRequestFabric
from server.horoscopes.sources.thousand_and_one.settings import (
    THOUSAND_AND_ONE_URL,
)


class BaseThousandAndOneRequestFabric(SignDrivenRequestFabric):
    """Base request fabric for 1001 sources horoscopes."""

    base_url: str = THOUSAND_AND_ONE_URL


class TodayHoroscopeRequestFabric(BaseThousandAndOneRequestFabric):
    """Request fabric for get today horoscope."""

    def prepare_params(self) -> dict[str, str]:
        """Returns params for get today horoscope."""
        return {
            "znak": self.sign.value.lower(),
        }
