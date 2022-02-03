
from server.horoscopes.base.clients import BaseClient
from server.horoscopes.enums import HoroscopeSigns

from server.horoscopes.sources.horo_mail import methods


class HoroMailClient(BaseClient):
    """Client for interacting with https://horo.mail.ru/prediction"""

    def get_today_horoscope_by_sign(self, sign: HoroscopeSigns, **kwargs):
        """Returns today horoscope by sign."""
        return methods.GetTodayPrediction().execute(sign=sign)
