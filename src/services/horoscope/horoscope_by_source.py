from db.enums import HoroscopeSigns
from services.source.mappings import HoroscopeSources


class HoroscopeBySourceFabric:
    @classmethod
    async def get_today_horoscope_by_sign(
        cls, source: HoroscopeSources, sign: HoroscopeSigns, *args, **kwargs
    ) -> str:
        return await source.value.get_today_by_sign(sign, *args, **kwargs)
