
import abc

from server.horoscopes.enums import HoroscopeSigns


class HoroscopeFabric(abc.ABCMeta):
    """Base fabric for horoscopes from different sources."""

    def get_horoscope_by_sign(self, sign: HoroscopeSigns, *args, **kwargs):
        """Returns horoscope from by sign source."""
        ...
