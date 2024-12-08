from collectors.api_collector import APICollector
import pandas as pd

# API Collection
api_url = "https://api.nasa.gov"
api_key = "5LE6KjhNYXV7RbQtgwmDBPtGaChFO7MRIdndDlrp"
endpoint = "planetary/apod"
params = {
    "api_key": api_key,
    "start_date": "2023-11-01",  # Optional: start date
    "end_date": "2023-11-10"     # Optional: end date
}

# Create an instance of APICollector
api_collector = APICollector(base_url=api_url, default_params={"api_key": api_key})

# Fetch data from the NASA API (GET request)
data = api_collector.fetch_data(endpoint=endpoint, params=params)

# Print the fetched data or process it further
if data:
    print(data)
else:
    print("Failed to retrieve data.")



# Example of a POST request (for illustration purposes)
# Assuming an endpoint and data for POST request
# post_endpoint = "some/other/endpoint"
# post_data = {"key": "value"}
# post_response = api_collector.fetch_data(endpoint=post_endpoint, params=post_data, method='POST')

