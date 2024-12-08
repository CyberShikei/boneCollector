# BoneCollector

BoneCollector is a Python package designed for basic ETL (Extract, Transform, Load) tasks. It provides utilities for collecting data from various sources, cleaning it, and storing it in a database. The package is modular and easy to extend, making it suitable for a variety of data engineering workflows.

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

