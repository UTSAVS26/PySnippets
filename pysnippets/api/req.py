import requests
from requests.auth import HTTPBasicAuth
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# GET request
def GET(url, auth=None):
    if auth:
        return requests.get(url, auth=HTTPBasicAuth(*auth))
    return requests.get(url)

# POST request
def POST(url, data, auth=None):
    response = requests.post(url, data=data, auth=HTTPBasicAuth(*auth) if auth else None)
    log_request('POST', url, response)
    return response

# PUT request
def PUT(url, data, auth=None):
    if auth:
        return requests.put(url, data=data, auth=HTTPBasicAuth(*auth))
    return requests.put(url, data=data)

# DELETE request
def DELETE(url, auth=None):
    if auth:
        return requests.delete(url, auth=HTTPBasicAuth(*auth))
    return requests.delete(url)

# PATCH request
def PATCH(url, data, auth=None):
    if auth:
        return requests.patch(url, data=data, auth=HTTPBasicAuth(*auth))
    return requests.patch(url, data=data)

# OPTIONS request
def OPTIONS(url, auth=None):
    if auth:
        return requests.options(url, auth=HTTPBasicAuth(*auth))
    return requests.options(url)

# HEAD request
def HEAD(url, auth=None):
    if auth:
        return requests.head(url, auth=HTTPBasicAuth(*auth))
    return requests.head(url)

# SAFE GET request with error handling
def SAFE_GET(url, auth=None):
    try:
        if auth:
            response = requests.get(url, auth=HTTPBasicAuth(*auth))
        else:
            response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"Other error occurred: {err}"

# Universal request function
def request(method, url, data=None, auth=None):
    if method == 'GET':
        return GET(url, auth)
    elif method == 'POST':
        return POST(url, data, auth)
    elif method == 'PUT':
        return PUT(url, data, auth)
    elif method == 'DELETE':
        return DELETE(url, auth)
    elif method == 'PATCH':
        return PATCH(url, data, auth)
    elif method == 'OPTIONS':
        return OPTIONS(url, auth)
    elif method == 'HEAD':
        return HEAD(url, auth)
    else:
        raise ValueError('Invalid method')

# Extra Features

# GET request with custom headers
def GET_with_headers(url, headers=None, auth=None):
    if auth:
        return requests.get(url, headers=headers, auth=HTTPBasicAuth(*auth))
    return requests.get(url, headers=headers)

# POST request with custom headers
def POST_with_headers(url, data, headers=None, auth=None):
    if auth:
        return requests.post(url, data=data, headers=headers, auth=HTTPBasicAuth(*auth))
    return requests.post(url, data=data, headers=headers)

# GET request with timeout
def GET_with_timeout(url, timeout=10, auth=None):
    if auth:
        return requests.get(url, timeout=timeout, auth=HTTPBasicAuth(*auth))
    return requests.get(url, timeout=timeout)

# POST request with timeout
def POST_with_timeout(url, data, timeout=10, auth=None):
    if auth:
        return requests.post(url, data=data, timeout=timeout, auth=HTTPBasicAuth(*auth))
    return requests.post(url, data=data, timeout=timeout)

# Retry mechanism for requests
def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

# GET request with retry mechanism
def GET_with_retry(url, auth=None):
    session = requests_retry_session()
    if auth:
        return session.get(url, auth=HTTPBasicAuth(*auth))
    return session.get(url)

# POST request with retry mechanism
def POST_with_retry(url, data, auth=None):
    session = requests_retry_session()
    if auth:
        return session.post(url, data=data, auth=HTTPBasicAuth(*auth))
    return session.post(url, data=data)

# Logging requests
def log_request(method, url, response):
    logging.info(f"{method} request to {url} - Status Code: {response.status_code}")

# GET request with logging
def GET(url, auth=None):
    response = requests.get(url, auth=HTTPBasicAuth(*auth) if auth else None)
    log_request('GET', url, response)
    return response

# POST request with logging
def POST(url, data, auth=None):
    response = requests.post(url, data=data, auth=HTTPBasicAuth(*auth) if auth else None)
    log_request('POST', url, response)
    return response

# GET request with custom User-Agent
def GET_with_user_agent(url, user_agent, auth=None):
    headers = {'User-Agent': user_agent}
    if auth:
        return requests.get(url, headers=headers, auth=HTTPBasicAuth(*auth))
    return requests.get(url, headers=headers)

# POST request with custom User-Agent
def POST_with_user_agent(url, data, user_agent, auth=None):
    headers = {'User-Agent': user_agent}
    if auth:
        return requests.post(url, data=data, headers=headers, auth=HTTPBasicAuth(*auth))
    return requests.post(url, data=data, headers=headers)

# GET request with query parameters
def GET_with_params(url, params, auth=None):
    if auth:
        return requests.get(url, params=params, auth=HTTPBasicAuth(*auth))
    return requests.get(url, params=params)

# POST request with query parameters
def POST_with_params(url, data, params, auth=None):
    if auth:
        return requests.post(url, data=data, params=params, auth=HTTPBasicAuth(*auth))
    return requests.post(url, data=data, params=params)

# GET request with session management
session = requests.Session()

def GET_with_session(url, auth=None):
    if auth:
        return session.get(url, auth=HTTPBasicAuth(*auth))
    return session.get(url)

# POST request with session management
def POST_with_session(url, data, auth=None):
    if auth:
        return session.post(url, data=data, auth=HTTPBasicAuth(*auth))
    return session.post(url, data=data)

# POST request for file upload
def POST_file(url, file_path, auth=None):
    files = {'file': open(file_path, 'rb')}
    if auth:
        return requests.post(url, files=files, auth=HTTPBasicAuth(*auth))
    return requests.post(url, files=files)

# Download file
def download_file(url, file_path, auth=None):
    if auth:
        response = requests.get(url, auth=HTTPBasicAuth(*auth), stream=True)
    else:
        response = requests.get(url, stream=True)
    with open(file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    return file_path