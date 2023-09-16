from typing import Any

import aiohttp


class HTTPClient:
    def __init__(self, url: str, session: aiohttp.ClientSession | None = None):
        self._session = session if session is not None else aiohttp.ClientSession()
        self._url = url

    async def get(self, params: dict[str, Any] | None = None) -> str:
        async with self._session as session:
            async with session.get(self._url, params=params) as response:
                response.raise_for_status()
                page_encoding = response.get_encoding()
                return await (response.text(encoding=page_encoding) if page_encoding else response.text())
