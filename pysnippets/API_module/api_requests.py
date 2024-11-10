import requests
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from query_params import serialize_params
from path_params import construct_url

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Setup retry strategy
retry_strategy = Retry(
    total=3,  # Total number of retries
    status_forcelist=[429, 500, 502, 503, 504],  # Status codes to retry
    allowed_methods=["HEAD", "GET", "PUT", "DELETE", "OPTIONS", "TRACE", "POST"],
    backoff_factor=1  # Backoff factor to apply between attempts
)
adapter = HTTPAdapter(max_retries=retry_strategy)

def get(url, params=None, headers=None):
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    try:
        if params:
            query_string = serialize_params(params)
            url = f"{url}?{query_string}"
        
        logging.debug(f"Sending GET request to {url} with headers {headers}")
        response = session.get(url, headers=headers)
        response.raise_for_status()
        logging.debug(f"Response received: {response.status_code} - {response.content[:100]}")
        return response
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None

def post(url, data=None, headers=None):
    response = requests.post(url, json=data, headers=headers)
    return response

def put(url, data=None, headers=None):
    response = requests.put(url, json=data, headers=headers)
    return response

def delete(url, headers=None):
    response = requests.delete(url, headers=headers)
    return response

def get_with_path_params(base_url, path_params, headers=None):
    try:
        url = construct_url(base_url, path_params)
        logging.debug(f"Sending GET request to {url} with headers {headers}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        logging.debug(f"Response received: {response.status_code} - {response.content[:100]}")
        return response
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None