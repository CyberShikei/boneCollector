from bs4 import BeautifulSoup
import requests
import logging

logger = logging.getLogger(__name__)

class WebScraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_page(self, path):
        """
        Fetches the content of a web page from the specified path relative to the base URL.

        Args:
            path (str): The relative path to the resource on the base URL.

        Returns:
            str: The HTML content of the page if the request is successful.
            None: If an error occurs during the request.

        Raises:
            None: Logs an error if the request fails.
        """ 
        url = f"{self.base_url}{path}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching page {url}: {e}")
            return None

    def parse_page(self, html_content, parser="html.parser"):
            """
        Parses HTML content using the specified parser.

        Args:
            html_content (str): The HTML content to parse.
            parser (str, optional): The parser to use for parsing the HTML content.
                Defaults to "html.parser". Common alternatives include "lxml" or "html5lib".

        Returns:
            BeautifulSoup: A BeautifulSoup object representing the parsed HTML content, 
                allowing for further manipulation and data extraction.
            None: If an error occurs during parsing.

        Raises:
            None: Logs an error message if parsing fails.
        """
        try:
            soup = BeautifulSoup(html_content, parser)
            return soup
        except Exception as e:
            logger.error(f"Error parsing HTML content: {e}")
            return None
