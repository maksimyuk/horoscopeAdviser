
import abc

from server.horoscopes.enums import HoroscopeSigns


class BaseClient(abc.ABC):
    """Base fabric for horoscopes from different sources."""

    def __init__(self, sign: HoroscopeSigns, *args, **kwargs):
        """Init client class by requesting sign."""
        self.sign = sign

    def get_horoscope_by_sign(self, *args, **kwargs):
        """Returns horoscope from by sign source."""
        ...
