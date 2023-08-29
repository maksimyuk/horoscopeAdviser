import abc
import re

from bs4 import BeautifulSoup


class BaseScrapper(abc.ABC):
    """Base data-scrapper for getting data from string with HTML."""

    def __init__(self, html_page: str, **kwargs):
        self.html_page = html_page
        self.parser = self._init_parser()

    def _init_parser(self) -> BeautifulSoup:
        """Returns initiated HTML parser."""
        return BeautifulSoup(self.html_page, "html.parser")

    @abc.abstractmethod
    async def _get_data_from_html_page(self) -> str:
        """Returns scrapped data from html_page"""
        return self.html_page

    async def _prettify_raw_page_data(self, raw_page: str) -> str:
        cleaned_page = re.sub(r"[^\w\s.,?!–-]", "", raw_page)
        cleaned_page = cleaned_page.replace("\n", " ")
        cleaned_page = re.sub(" +", " ", cleaned_page)

        return cleaned_page

    async def scrap(self) -> str:
        """Pick out horoscope data from HTML decoded page."""
        raw_page = await self._get_data_from_html_page()

        pretty_page = await self._prettify_raw_page_data(raw_page)

        return pretty_page


class BaseTagBasedScrapper(BaseScrapper):
    """Base data scrapper for getting data inside special tag."""

    @property
    @abc.abstractmethod
    def html_tag(self) -> str:
        """HTML-tag with content."""

    async def get_tag_data(self) -> str:
        """Returns data from given html-tags."""
        tags_content = self.parser.find_all(self.html_tag)

        return " ".join((tag_content.text for tag_content in tags_content))

    async def _get_data_from_html_page(self) -> str:
        """Returns scrapped data from html_page"""
        return await self.get_tag_data()


class BasePBasedScrapper(BaseTagBasedScrapper):
    """Base data-scrapper for getting data inside <p> tags of html."""

    html_tag = "p"
