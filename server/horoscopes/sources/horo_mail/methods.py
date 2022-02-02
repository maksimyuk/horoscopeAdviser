
from server.horoscopes.base.methods import BaseMethod
from server.horoscopes.enums import HoroscopeSigns


class GetTodayPrediction(BaseMethod):

    def execute(self, sign: HoroscopeSigns) -> str:
        ...
