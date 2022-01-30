
from bs4 import BeautifulSoup

from server.horoscopes.base.scrappers import BaseScrapper


class TodayPredictionScrapper(BaseScrapper):
    """Scrapper horoscope for today."""

    def scrap(self) -> str:
        """"""
        soup = BeautifulSoup(self.html_page, 'html.parser')

        content_paragraphs = soup.find_all('p')
        return ' '.join((content_paragraph.text for content_paragraph in content_paragraphs))
