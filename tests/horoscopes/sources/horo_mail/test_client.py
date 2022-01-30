
from server.horoscopes.sources.horo_mail.client import HoroMailClient
from server.horoscopes.enums import HoroscopeSigns


class TestClient:

    def test_get_horoscope_by_sign(self):
        horo = HoroMailClient(sign=HoroscopeSigns.LEO).get_horoscope_by_sign()
        assert horo
