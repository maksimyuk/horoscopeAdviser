from services.scrappers.base import BaseScrapper


class GetTodaySignScrapper(BaseScrapper):
    _main_id = "eje_text"

    async def _get_data_from_html_page(self) -> str:
        """Returns scrapped data from html_page"""
        main_content = self.parser.find(id=self._main_id)

        return "".join(each_child.text for each_child in main_content.find_all("p"))
