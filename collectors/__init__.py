# data_collector/collectors/__init__.py

from .api_collector import APICollector
from .scraper import WebScraper

# Define what is imported when `from collectors import *` is used
__all__ = ["APICollector", "WebScraper"]
