from server.horoscopes.base.clients import BaseClient
from server.horoscopes.enums import HoroscopeSigns
from server.horoscopes.sources.thousand_and_one import methods


class ThousandAndOneClient(BaseClient):
    """Client for interacting with https://1001goroskop.ru"""

    def get_today_horoscope_by_sign(self, sign: HoroscopeSigns, **kwargs):
        """Returns today horoscope by sign."""
        return methods.GetTodayPrediction().execute(sign=sign)
