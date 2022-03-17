import abc
from typing import Any

import requests
from server.horoscopes.enums import HoroscopeSigns

OptionalAnyDictType = dict[str, Any] | None


class BaseRequestFabric(abc.ABC):
    """
    Base fabric for requests. Fabric creates requests
    Request object by given params, but nor send them.
    """

    @property
    @abc.abstractmethod
    def base_url(self) -> str:
        """Base url for requests."""

    def __init__(
        self,
        params: OptionalAnyDictType = None,
        data: OptionalAnyDictType = None,
        method: str = "GET",
        **kwargs,
    ):
        """Init Fabric by request URL, params, data, method."""
        self.params = params or {}
        self.data = data or {}
        self.method = method

    def prepare_request_url(self) -> str:
        """Return prepared url for request."""
        return self.base_url

    def prepare_params(self) -> dict[str, Any]:
        """Return prepared params for request."""
        return self.params

    def prepare_data(self) -> dict[str, Any]:
        """Return prepared data for request."""
        return self.data

    def create(self) -> requests.Request:
        """Returns created Request object ready-to send."""
        return requests.Request(
            method=self.method,
            url=self.prepare_request_url(),
            params=self.prepare_params(),
            data=self.prepare_data(),
        )


class SignDrivenRequestFabric(BaseRequestFabric, abc.ABC):
    """Fabric of requests with possibility of transferring the sign as parameter."""

    def __init__(self, sign: HoroscopeSigns, **kwargs):
        """Init Fabric of request with given sign."""
        super().__init__(**kwargs)
        self.sign = sign
