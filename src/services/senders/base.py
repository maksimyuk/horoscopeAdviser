from abc import ABC
from typing import Optional

from db.enums import HoroscopeSigns
from http_requests.client import HTTPClient


class BaseSignProvider(ABC):
    def __init__(self, sign: HoroscopeSigns, url: str):
        self._url = url
        self._sign = sign

    async def _prepare_url(self) -> str:
        return self._url

    async def _prepare_params(self) -> Optional[dict[str, str | int]]:
        return None

    async def provide(self) -> str:
        url = await self._prepare_url()
        params = await self._prepare_params()

        return await HTTPClient(url=url).get(params=params)
