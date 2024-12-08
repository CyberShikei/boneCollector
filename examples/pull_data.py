from collectors.api_collector import APICollector
#from collectors.scraper import WebScraper
from cleaning.cleaner import DataCleaner
import pandas as pd

import sys
from datetime import datetime

# Get today's date
today = datetime.today().date()

# API Collection
api_url = "https://api.nasa.gov" # Add your API URL
api_key = "" # Add your API key here
endpoint = "planetary/apod"
params = {
    "api_key": api_key,
    "start_date": today  # Optional: start date
}

# Create an instance of APICollector
api_collector = APICollector(base_url=api_url, default_params={"api_key": api_key})

# Fetch data from the NASA API (GET request)
data = api_collector.fetch_data(endpoint=endpoint, params=params)

# Check the fetched data
if not data:
    print("Error: Failed to retrieve data.")
    sys.exit(1)

# Data Cleaning Example
normalized_data = pd.json_normalize(data)
raw_data = pd.DataFrame(normalized_data)  # Assuming API returned JSON that can be converted to a DataFrame
cleaner = DataCleaner(dataframe=raw_data)
#cleaner.clean_missing_values(strategy="fill", fill_value="Unknown")
#cleaner.remove_duplicates()
cleaner.sanitize_column_names()
cleaned_data = cleaner.dataframe
print("Cleaned Data:", cleaned_data.head())
#data_dict = cleaned_data.to_dict(orient='records')
#print("Data Dict:\n", data_dict)

# Write DataFrame to JSON file
cleaned_data.to_json('data.json', orient='records', lines=True)
