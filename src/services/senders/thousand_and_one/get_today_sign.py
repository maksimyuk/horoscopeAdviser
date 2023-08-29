from typing import Optional

from ..base import BaseSignProvider
from .mappings import INTERNAL_HOROSCOPE_SIGNS_TO_THOUSAND_AND_ONE_SIGNS


class GetTodaySignProvider(BaseSignProvider):
    async def prepare_params(self) -> Optional[dict[str, str | int]]:
        external_system_sign = INTERNAL_HOROSCOPE_SIGNS_TO_THOUSAND_AND_ONE_SIGNS.get(
            self._sign
        )

        return {"znak": external_system_sign.value}
