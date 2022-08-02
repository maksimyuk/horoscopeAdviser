from enum import Enum


class HoroscopeSigns(Enum):
    """Enum for describing signs of horoscopes."""

    ARIES = "ARIES"
    TAURUS = "TAURUS"
    GEMINI = "GEMINI"
    CANCER = "CANCER"
    LEO = "LEO"
    VIRGO = "VIRGO"
    LIBRA = "LIBRA"
    SCORPIO = "SCORPIO"
    SAGITTARIUS = "SAGITTARIUS"
    CAPRICORN = "CAPRICORN"
    AQUARIUS = "AQUARIUS"
    PISCES = "PISCES"


def get_all_horoscope_signs() -> list[str]:
    """Return list of HoroscopeSigns values as string."""
    return [sign.value.capitalize() for sign in HoroscopeSigns]


def get_horoscope_sign_enum_by_value(value: str) -> HoroscopeSigns:
    """Returns HoroscopeSigns enum by any value."""
    return HoroscopeSigns[value.upper()]


class NotificationFrequency(Enum):
    """Enum for describing types of notification frequency."""

    DAILY = "DAILY"
    WEEKLY = "WEEKLY"


class Sources(Enum):
    """Enum for describing sources of horoscopes."""

    HORO_1001 = "1001"
    HORO_MAIL = "mail"
