import abc

from server.horoscopes.enums import HoroscopeSigns


class BaseClient(abc.ABC):
    """Base fabric for horoscopes from different sources."""

    def get_today_horoscope_by_sign(self, sign: HoroscopeSigns, **kwargs):
        """Returns horoscope by sign from source for today."""
