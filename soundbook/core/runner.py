from soundbook.core.handler import Config

from soundbook.modules.get_book import get_book
from soundbook.modules.get_url import get_url


class Runner:
    def __init__(self, config: Config):
        self.config = config

    def __str__(self) -> str:
        return f"{self.config}"

    def run(self):
        if self.config.book is not None:
            get_book(self.config.book)
        elif self.config.url is not None:
            get_url(self.config.url)
        else:
            print("No valid input")
