# main.py
import requests
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APIClient:
    """
    Python API client for interacting with a RESTful API.
    """

    def __init__(self, base_url):
        """
        Initialize the API client with a base URL.

        Args:
            base_url (str): The base URL of the API.
        """
        self.base_url = base_url

    def get(self, endpoint, params=None):
        """
        Send a GET request to the API.

        Args:
            endpoint (str): The endpoint to send the request to.
            params (dict, optional): The query parameters to include in the request. Defaults to None.

        Returns:
            dict: The JSON response from the API.
        """
        try:
            response = requests.get(f"{self.base_url}{endpoint}", params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as err:
            logger.error(f"Request error occurred: {err}")
            raise

    def post(self, endpoint, data):
        """
        Send a POST request to the API.

        Args:
            endpoint (str): The endpoint to send the request to.
            data (dict): The data to include in the request body.

        Returns:
            dict: The JSON response from the API.
        """
        try:
            response = requests.post(f"{self.base_url}{endpoint}", json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as err:
            logger.error(f"Request error occurred: {err}")
            raise

    def put(self, endpoint, data):
        """
        Send a PUT request to the API.

        Args:
            endpoint (str): The endpoint to send the request to.
            data (dict): The data to include in the request body.

        Returns:
            dict: The JSON response from the API.
        """
        try:
            response = requests.put(f"{self.base_url}{endpoint}", json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as err:
            logger.error(f"Request error occurred: {err}")
            raise

    def delete(self, endpoint):
        """
        Send a DELETE request to the API.

        Args:
            endpoint (str): The endpoint to send the request to.

        Returns:
            dict: The JSON response from the API.
        """
        try:
            response = requests.delete(f"{self.base_url}{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as err:
            logger.error(f"Request error occurred: {err}")
            raise


def main():
    base_url = "https://jsonplaceholder.typicode.com"
    client = APIClient(base_url)

    # Test GET request
    try:
        response = client.get("/posts")
        logger.info(f"GET response: {json.dumps(response, indent=4)}")
    except Exception as err:
        logger.error(f"Error occurred: {err}")

    # Test POST request
    try:
        data = {"title": "foo", "body": "bar", "userId": 1}
        response = client.post("/posts", data)
        logger.info(f"POST response: {json.dumps(response, indent=4)}")
    except Exception as err:
        logger.error(f"Error occurred: {err}")

    # Test PUT request
    try:
        data = {"title": "foo", "body": "bar", "userId": 1}
        response = client.put("/posts/1", data)
        logger.info(f"PUT response: {json.dumps(response, indent=4)}")
    except Exception as err:
        logger.error(f"Error occurred: {err}")

    # Test DELETE request
    try:
        response = client.delete("/posts/1")
        logger.info(f"DELETE response: {json.dumps(response, indent=4)}")
    except Exception as err:
        logger.error(f"Error occurred: {err}")


if __name__ == "__main__":
    main()