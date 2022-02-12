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
    return [
        sign.value.capitalize()
        for sign in HoroscopeSigns
    ]
