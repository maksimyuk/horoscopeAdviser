
import abc


class BaseMethod(abc.ABC):
    """Base class for interacting and returning content."""

    requests_fabric = None

    def __init__(self, *args, **kwargs) -> None:
        """Init Method calls by args and kwargs."""

    def execute(self, *args, **kwargs) -> str:
        """Returns content."""
