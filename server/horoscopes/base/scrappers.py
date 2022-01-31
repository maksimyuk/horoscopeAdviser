import abc


class BaseScrapper(abc.ABC):
    """Base data-scrapper for getting data from string with HTML."""

    def __init__(self, html_page: str):
        self.html_page = html_page

    @abc.abstractmethod
    def scrap(self) -> str:
        """Pick out horoscope data from HTML decoded page."""
