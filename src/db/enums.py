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


class HoroMailHoroscopeSigns(Enum):
    ARIES = "aries"
    TAURUS = "taurus"
    GEMINI = "gemini"
    CANCER = "cancer"
    LEO = "leo"
    VIRGO = "virgo"
    LIBRA = "libra"
    SCORPIO = "scorpio"
    SAGITTARIUS = "sagittarius"
    CAPRICORN = "capricorn"
    AQUARIUS = "aquarius"
    PISCES = "pisces"


class ThousandAndOneSigns(Enum):
    ARIES = "aries"
    TAURUS = "taurus"
    GEMINI = "gemini"
    CANCER = "cancer"
    LEO = "leo"
    VIRGO = "virgo"
    LIBRA = "libra"
    SCORPIO = "scorpio"
    SAGITTARIUS = "sagittarius"
    CAPRICORN = "capricorn"
    AQUARIUS = "aquarius"
    PISCES = "pisces"


def get_all_horoscope_signs() -> tuple[str]:
    """Return HoroscopeSigns values as string."""
    return tuple(sign.value.capitalize() for sign in HoroscopeSigns)


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
