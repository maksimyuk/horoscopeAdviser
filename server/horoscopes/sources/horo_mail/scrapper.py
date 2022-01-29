
import requests
from bs4 import BeautifulSoup


class HoroMailRequester:
    # Seems to set base.

    def get_sign_url(self) -> str:
        """Returns url for horoscope source."""
        return 'https://horo.mail.ru/prediction/aries/today/'

    def get_horoscope_source_content(self) -> str:
        response = requests.get(self.get_sign_url())
        return response.content.decode()


class HoroMailScrapper:
    """Scrapper for horo mail. Returns content of horoscope sign."""

    def get_horoscope(self, content: str):
        soup = BeautifulSoup(content, 'html.parser')

        content_paragraphs = soup.find_all('p')
        return ''.join((content_paragraph.text for content_paragraph in content_paragraphs))
