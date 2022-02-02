import abc
from typing import Type

from server.horoscopes.base.fabrics import BaseRequestFabric
from server.horoscopes.base.sender import BaseRequestsSender
from server.horoscopes.base.scrappers import BaseScrapper


class BaseMethod(abc.ABC):
    """Base class for interacting and returning content."""

    requests_sender: Type[BaseRequestsSender]
    requests_fabric: Type[BaseRequestFabric]
    response_scrapper: Type[BaseScrapper]

    def __init__(self, *args, **kwargs) -> None:
        """Init Method calls by args and kwargs."""

    def execute(self, *args, **kwargs) -> str:
        """Sends request and returns content."""
        request_fabric = self.requests_fabric(**kwargs)
        return self.requests_sender(
            request_fabric=request_fabric
        ).get_decoded_content()
