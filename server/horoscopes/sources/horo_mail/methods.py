
from server.horoscopes.enums import HoroscopeSigns


class GetTodayPrediction:

    def execute(self, sign: HoroscopeSigns) -> str:
        ...