import requests
from server.horoscopes.base.fabrics import BaseRequestFabric
from server.horoscopes.base.utils import send_request


class BaseRequestsSender:
    """Base sender for requests made by RequestFabric."""

    def __init__(self, request_fabric: BaseRequestFabric):
        """Sender initiates by instantiated request fabric."""
        self.request_fabric = request_fabric

    def create_request(self) -> requests.Request:
        """Returns created request Object."""
        return self.request_fabric.create()

    def get_response(self) -> requests.Response:
        """Returns response to sent request."""
        request = self.create_request()
        return send_request(request)

    @staticmethod
    def get_response_encoding(response: requests.Response) -> str:
        """Returns response encoding or default."""
        return response.encoding if response.encoding else "utf-8"

    def get_decoded_content(self) -> str:
        """Returns decoded content of response."""
        response = self.get_response()
        encoding = self.get_response_encoding(response)

        return response.content.decode(encoding)
