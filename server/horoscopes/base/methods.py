import abc
from typing import Type

import requests

from server.horoscopes.base.fabrics import BaseRequestFabric
from server.horoscopes.base.scrappers import BaseScrapper
from server.horoscopes.base.sender import BaseRequestsSender
from server.settings.components.horoscope_adviser import SHOW_HOROSCOPE_SOURCE


class BaseMethod(abc.ABC):
    """Base class for interacting and returning content."""

    requests_sender: Type[BaseRequestsSender] = BaseRequestsSender
    requests_fabric: Type[BaseRequestFabric]
    response_scrapper: Type[BaseScrapper]

    def __init__(self, show_source: bool = SHOW_HOROSCOPE_SOURCE):
        self.show_source = show_source

    def get_source_info(self, request: requests.Request) -> str:
        """Returns info about source of request."""
        return f"Источник: {request.url}"

    def execute(self, show_source: bool = True, **kwargs) -> str:
        """Sends request and returns content."""
        request_fabric = self.requests_fabric(**kwargs)

        sender = self.requests_sender(request_fabric=request_fabric)
        response_content = sender.get_decoded_content()

        scrapped_content = self.response_scrapper(html_page=response_content).scrap()

        # show source of content
        if self.show_source:
            return "\n".join((scrapped_content, self.get_source_info(sender.request)))

        return scrapped_content
