from server.horoscopes.base.methods import BaseMethod
from server.horoscopes.sources.horo_mail.fabrics import (
    TodayHoroscopeRequestFabric,
)
from server.horoscopes.sources.horo_mail.scrappers import (
    TodayPredictionScrapper,
)


class GetTodayPrediction(BaseMethod):
    """Method for get today prediction."""

    requests_fabric = TodayHoroscopeRequestFabric
    response_scrapper = TodayPredictionScrapper
