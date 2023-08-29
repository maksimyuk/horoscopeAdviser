from enum import Enum

from .horo_mail import HoroMailSource
from .thousand_and_one import ThousandAndOneSource


class HoroscopeSources(Enum):
    HORO_MAIL = HoroMailSource
    THOUSAND_AND_ONE = ThousandAndOneSource
