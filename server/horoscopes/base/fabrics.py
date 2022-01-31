
import abc
from typing import Any
from server.horoscopes.enums import HoroscopeSigns

import requests


OptionalAnyDictType = dict[str, Any] | None


class BaseRequestFabric(abc.ABC):
    """
    Base fabric for requests. Fabric creates requests.

    Request object by given params, but nor send them.
    """

    @property
    @abc.abstractmethod
    def base_url(self) -> str:
        """Base url for requests."""

    def __init__(self, params: OptionalAnyDictType = None, data: OptionalAnyDictType = None, method='GET: str', **kwargs):
        """Init Fabric by request URL, params, data, method."""
        self.params = params
        self.data = data
        self.method = method

    def prepare_request_url(self) -> str:
        """Return prepared url for request."""
        return self.base_url

    def create(self) -> requests.Request:
        """Returns created Request object ready-to send."""
        return requests.Request(
            method=self.method,
            url=self.prepare_request_url(),
            params=self.params,
            data=self.data,
        )


class SignDrivenRequestFabric(BaseRequestFabric):
    """Fabric of requests with possibility of transferring the sign as parameter."""

    def __init__(self, sign: HoroscopeSigns, **kwargs):
        """Init Fabric of request with given sign."""
        super().__init__(**kwargs)
        self.sign = sign
