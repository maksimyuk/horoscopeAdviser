
import pytest
from server.horoscopes.base.scrappers import BaseScrapper, BaseTagBasedScrapper


HTML_CONTENT_EXAMPLE = """
    <!DOCTYPE html>
    <html lang="ru-RU">
        <head></head>
        <body>
            <div>
                <li>List1</li>
                <p>Par1.</p>
                <p>Par2.</p>
                <li>List2</li>
            </div>
        </body>
    </html>
    """


@pytest.fixture()
def html_page() -> str:
    """OK response with content."""
    return HTML_CONTENT_EXAMPLE


class SimpleScrapper(BaseScrapper):
    """Simple scrapper for test purposes."""

    def get_data_from_html_page(self) -> str:
        return "test"


class TestBaseScrapper:
    """Tests for checking work of base scrapper."""

    @pytest.fixture()
    def scrapper(self, html_page) -> SimpleScrapper:
        return SimpleScrapper(html_page)

    def test_init_scrapper(self, scrapper):
        """Check instantiated scrapper have got html_page and parser as attributes."""

        assert scrapper.html_page
        assert scrapper.parser

    def test_get_data_from_html_page(self, scrapper):
        """Check returning data from html_page."""
        data = scrapper.get_data_from_html_page()

        assert data == "test"

    def test_scrap(self, scrapper):
        """Check scrap returns pick outed data from html_page."""
        scrapped_data = scrapper.scrap()

        assert scrapped_data == "test"


class SimpleTagBasedScrapper(BaseTagBasedScrapper):
    """Simple tag-based scrapper for test purposes."""
    html_tag = 'li'


class TestBaseTagBasedScrapper:
    """Tests for checking work of base tag-based scrapper."""

    @pytest.fixture()
    def scrapper(self, html_page) -> SimpleTagBasedScrapper:
        """Returns instance of SimpleTagBasedScrapper."""
        return SimpleTagBasedScrapper(html_page)

    def test_get_tag_data(self, scrapper):
        """Check tag data is correct."""
        tag_data = scrapper.get_tag_data()

        assert tag_data == 'List1 List2'


class PTagBasedScrapper(BaseTagBasedScrapper):
    """Simple tag-based scrapper for test purposes."""
    html_tag = 'p'


class TestBasePBasedScrapper:
    """Tests for checking work of base data-scrapper inside <p> tags."""

    @pytest.fixture()
    def scrapper(self, html_page) -> PTagBasedScrapper:
        """Returns instance of SimpleTagBasedScrapper."""
        return PTagBasedScrapper(html_page)

    def test_get_tag_data(self, scrapper):
        """Check tag data is correct."""
        tag_data = scrapper.get_tag_data()

        assert tag_data == 'Par1. Par2.'
