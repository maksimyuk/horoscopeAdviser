import abc
from typing import Type

from server.horoscopes.base.fabrics import BaseRequestFabric
from server.horoscopes.base.scrappers import BaseScrapper
from server.horoscopes.base.sender import BaseRequestsSender


class BaseMethod(abc.ABC):
    """Base class for interacting and returning content."""

    requests_sender: Type[BaseRequestsSender] = BaseRequestsSender
    requests_fabric: Type[BaseRequestFabric]
    response_scrapper: Type[BaseScrapper]

    def execute(self, **kwargs) -> str:
        """Sends request and returns content."""
        request_fabric = self.requests_fabric(**kwargs)
        response_content = self.requests_sender(
            request_fabric=request_fabric
        ).get_decoded_content()

        return self.response_scrapper(html_page=response_content).scrap()
