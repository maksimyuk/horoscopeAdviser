
import requests
from server.horoscopes.base.clients import BaseClient
from server.horoscopes.sources.horo_mail.scrappers import (
    TodayPredictionScrapper,
)
from server.horoscopes.sources.horo_mail.settings import HORO_MAIL_URL


class HoroMailClient(BaseClient):
    """Client for interacting with https://horo.mail.ru/prediction"""

    def get_horoscope_by_sign(self, *args, **kwargs):
        """Returns content for prediction by sign for today."""
        request_object = self.create_request_object()

        response = self.make_request(request_object)
        response.raise_for_status()

        content = self.decode_content(response)
        return TodayPredictionScrapper(content).scrap()

    def get_requesting_url(self):
        """Returns URL to request."""
        return f'{HORO_MAIL_URL}/{self.sign.value.lower()}/today/'

    def create_request_object(self) -> requests.Request:
        """Build Request object by params."""

        return requests.Request(
            method='GET',
            url=self.get_requesting_url(),
        )

    def make_request(self, request: requests.Request) -> requests.Response:
        """Send request to web-site."""
        prepared_request = request.prepare()

        with requests.session() as session:
            return session.send(prepared_request)

    def decode_content(self, response: requests.Response) -> str:
        """Returns decoded content."""
        return response.content.decode('utf-8')
