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

    def get_content(self) -> bytes:
        """Returns raw content of response."""
        response = self.get_response()
        return response.content

    def get_decoded_content(self) -> str:
        """Returns decoded content of response."""
        # Change to decorator
        content = self.get_content()
        return content.decode("utf-8")
