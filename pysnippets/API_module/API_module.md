# API Module Documentation

This documentation provides an overview of the code snippets included in the API module. The module consists of four main components: API requests, path parameters, query parameters, and response handling.

## Files

1. [api_requests.py](#file:api_requests.py-context)
2. [path_params.py](#file:path_params.py-context)
3. [query_params.py](#file:query_params.py-context)
4. [response_handling.py](#file:response_handling.py-context)

## api_requests.py

This file contains functions to make HTTP requests with retry logic and logging.

### Functions

- `get(url, params=None, headers=None)`: Sends a GET request with optional query parameters and headers.
- `post(url, data=None, headers=None)`: Sends a POST request with optional JSON data and headers.
- `put(url, data=None, headers=None)`: Sends a PUT request with optional JSON data and headers.
- `delete(url, headers=None)`: Sends a DELETE request with optional headers.
- `get_with_path_params(base_url, path_params, headers=None)`: Sends a GET request with path parameters.

### Usage

1. Import the necessary functions:
    ```python
    from api_requests import get, post, put, delete, get_with_path_params
    ```

2. Use the functions to make HTTP requests:
    ```python
    response = get('https://api.example.com/resource')
    response = post('https://api.example.com/resource', data={'key': 'value'})
    response = put('https://api.example.com/resource/1', data={'key': 'new_value'})
    response = delete('https://api.example.com/resource/1')
    response = get_with_path_params('https://api.example.com/resource', {'id': 1})
    ```

## path_params.py

This file contains a function to construct URLs with path parameters.

### Functions

- `construct_url(base_url, path_params)`: Constructs a URL by appending URL-encoded path parameters to a base URL.

### Usage

1. Import the function:
    ```python
    from path_params import construct_url
    ```

2. Use the function to construct URLs:
    ```python
    url = construct_url('https://api.example.com/resource', {'id': 1})
    ```

## query_params.py

This file contains a function to serialize complex query parameters into a URL-encoded string.

### Functions

- `serialize_params(params)`: Serializes a dictionary of parameters into a URL-encoded query string.

### Usage

1. Import the function:
    ```python
    from query_params import serialize_params
    ```

2. Use the function to serialize query parameters:
    ```python
    query_string = serialize_params({'key1': 'value1', 'key2': 'value2'})
    ```

## response_handling.py

This file contains a function to handle HTTP responses, specifically for processing zip files.

### Functions

- `handle_response(response, save_path)`: Handles the response by checking the content type and processing zip files if necessary.

### Usage

1. Import the function:
    ```python
    from response_handling import handle_response
    ```

2. Use the function to handle HTTP responses:
    ```python
    handle_response(response, '/path/to/save')
    ```