
import pytest
from server.horoscopes.sources.horo_mail.scrappers import (
    TodayPredictionScrapper,
)


@pytest.fixture()
def ok_html_prediction() -> str:
    """OK response with content."""
    return """
    <!DOCTYPE html>
    <html lang="ru-RU">
        <head></head>
        <body>
            <li>List1</li>
            <p>Par1.</p>
            <p>Par2.</p>
            <li>List2</li>
        </body>
    </html>
    """


class TestTodayPredictionScrapper:
    """Tests for today prediction scrapper."""

    def test_ok_prediction(self, ok_html_prediction):
        """Check extracting data with <p> tags."""
        scrapped_data = TodayPredictionScrapper(ok_html_prediction).scrap()

        assert scrapped_data
        assert scrapped_data == 'Par1. Par2.'

    def test_empty_prediction(self):
        """Check no failure on empty html page."""
        scrapped_data = TodayPredictionScrapper('').scrap()

        assert not scrapped_data
