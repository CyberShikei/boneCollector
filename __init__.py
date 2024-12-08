# data_collector/__init__.py

__version__ = "0.1.0"
__author__ = "Jaco Ferreira"

# Import core components to make them available at the package level
from .collectors.api_collector import APICollector
from .collectors.scraper import WebScraper
from .cleaning.cleaner import DataCleaner
from .database.db_connector import DBConnector
from .database.db_operations import DBOperations

# If you want to expose specific functionality when * is imported
__all__ = ["APICollector", "WebScraper", "DataCleaner", "DBConnector", "DBOperations"]
