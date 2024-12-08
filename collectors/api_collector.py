import requests
import logging

logger = logging.getLogger(__name__)

class APICollector:
    def __init__(self, base_url, headers=None, default_params=None):
        self.base_url = base_url
        self.headers = headers or {}
        self.default_params = default_params or {}

    def fetch_data(self, endpoint, params=None, method='GET'):
        """
        Fetch data from the API.

        :param endpoint: API endpoint to query (e.g., 'planetary/apod').
        :param params: Additional parameters for the request.
        :param method: HTTP method ('GET', 'POST', etc.). Default is 'GET'.
        :return: Response data in JSON format or None on failure.
        """
        url = f"{self.base_url}/{endpoint}"
        all_params = self.default_params.copy()  # Start with default params
        if params:
            all_params.update(params)  # Update with params provided for the request
        
        try:
            if method.upper() == 'GET':
                response = requests.get(url, headers=self.headers, params=all_params)
            elif method.upper() == 'POST':
                response = requests.post(url, headers=self.headers, data=all_params)
            elif method.upper() == 'PUT':
                response = requests.put(url, headers=self.headers, data=all_params)
            # Add more HTTP methods as needed (DELETE, PATCH, etc.)

            response.raise_for_status()  # Raise HTTPError for bad responses
            return response.json()  # Assuming the API returns JSON data
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching data from {url}: {e}")
            return None

