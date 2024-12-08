# BoneCollector

BoneCollector is a Python package designed for basic ETL (Extract, Transform, Load) tasks. It provides utilities for collecting data from various sources, cleaning it, and storing it in a database. The package is modular and easy to extend, making it suitable for a variety of data engineering workflows.

<p align="center">
  <a href="https://pypi.org/project/requests/"><img alt="Requests" src="https://img.shields.io/badge/requests-2.28.0-brightgreen?style=flat-square" /></a>
  <a href="https://pypi.org/project/beautifulsoup4/"><img alt="BeautifulSoup4" src="https://img.shields.io/badge/beautifulsoup4-4.11.0-blue?style=flat-square" /></a>
  <a href="https://pypi.org/project/pandas/"><img alt="Pandas" src="https://img.shields.io/badge/pandas-1.4.0-blue?style=flat-square" /></a>
  <a href="https://pypi.org/project/sqlalchemy/"><img alt="SQLAlchemy" src="https://img.shields.io/badge/sqlalchemy-2.0.0-blue?style=flat-square" /></a>
  <a href="https://pypi.org/project/psycopg2-binary/"><img alt="psycopg2-binary" src="https://img.shields.io/badge/psycopg2--binary-2.9.0-blue?style=flat-square" /></a>
</p>

## Features

### Data Collectors
- **API Collector (`collectors/api_collector.py`)**: Fetches data from APIs.
- **Scraper (`collectors/scraper.py`)**: Extracts data from web pages.

### Data Cleaning
- **Cleaner (`cleaning/cleaner.py`)**: Processes and cleans raw data for further use.

### Database Operations
- **Connector (`database/db_connector.py`)**: Connects to databases.
- **Operations (`database/db_operations.py`)**: Performs common database tasks like inserting, updating, and querying data.

### Utilities
- **Logger (`utils/logger.py`)**: Provides consistent and customizable logging for your workflows.
- **Config Loader (`utils/config_loader.py`)**: Handles configuration settings.

## Installation

Clone the repository and install the package locally:
```bash
git clone https://github.com/yourusername/boneCollector.git
cd boneCollector
pip install .
