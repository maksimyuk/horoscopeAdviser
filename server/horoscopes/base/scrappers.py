import abc

from bs4 import BeautifulSoup


class BaseScrapper(abc.ABC):
    """Base data-scrapper for getting data from string with HTML."""

    def __init__(self, html_page: str, **kwargs):
        self.html_page = html_page
        self.parser = self.init_parser()

    def init_parser(self) -> BeautifulSoup:
        """Returns initiated HTML parser."""
        return BeautifulSoup(self.html_page, "html.parser")

    @abc.abstractmethod
    def get_data_from_html_page(self) -> str:
        """Returns scrapped data from html_page"""
        return self.html_page

    def scrap(self) -> str:
        """Pick out horoscope data from HTML decoded page."""
        return self.get_data_from_html_page()


class BaseTagBasedScrapper(BaseScrapper):
    """Base data scrapper for getting data inside special tag."""

    @property
    @abc.abstractmethod
    def html_tag(self) -> str:
        """HTML-tag with content."""

    def get_tag_data(self) -> str:
        """Returns data from <p> html-tags."""
        tags_content = self.parser.find_all(self.html_tag)

        return " ".join((tag_content.text for tag_content in tags_content))

    def get_data_from_html_page(self) -> str:
        """Returns scrapped data from html_page"""
        return self.get_tag_data()


class BasePBasedScrapper(BaseTagBasedScrapper):
    """Base data-scrapper for getting data inside <p> tags of html."""

    html_tag = "p"
