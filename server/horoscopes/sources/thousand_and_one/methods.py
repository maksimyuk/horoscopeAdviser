from server.horoscopes.base.methods import BaseMethod
from server.horoscopes.sources.thousand_and_one.fabrics import (
    TodayHoroscopeRequestFabric,
)
from server.horoscopes.sources.thousand_and_one.scrappers import (
    TodayPredictionScrapper,
)


class GetTodayPrediction(BaseMethod):
    """Method for get today prediction."""

    requests_fabric = TodayHoroscopeRequestFabric
    response_scrapper = TodayPredictionScrapper
