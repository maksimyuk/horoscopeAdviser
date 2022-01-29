
from server.horoscopes.enums import HoroscopeSigns
from server.horoscopes.base.fabrics import HoroscopeFabric


class HoroMailFabric(HoroscopeFabric):
    """Fabric of horoscopes for horo mail."""

    def get_horoscope_by_sign(self, sign: HoroscopeSigns, *args, **kwargs):
        pass
