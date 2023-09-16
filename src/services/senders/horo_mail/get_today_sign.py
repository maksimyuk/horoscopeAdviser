from ..base import BaseSignProvider
from .mappings import INTERNAL_HOROSCOPE_SIGNS_TO_HORO_MAIL_SIGNS


class GetTodaySignProvider(BaseSignProvider):
    async def prepare_url(self) -> str:
        external_system_sign = INTERNAL_HOROSCOPE_SIGNS_TO_HORO_MAIL_SIGNS.get(self._sign)
        return "/".join((self._url, "prediction", external_system_sign.value, "today"))
