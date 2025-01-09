# PySnippets API Library

This library provides a set of functions to make HTTP requests using the `requests` library in Python. It includes support for various HTTP methods, custom headers, timeouts, retry mechanisms, session management, file uploads, and downloads.

## Installation

To use this library, you need to have `requests` installed. You can install it using pip:

```sh
pip install requests
```

## Usage

### Basic requests

```sh
from pysnippets.api import GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD, SAFE_GET

# GET request
response = GET('https://api.example.com/data')
print(response.json())

# POST request
response = POST('https://api.example.com/data', data={'key': 'value'})
print(response.json())

# PUT request
response = PUT('https://api.example.com/data/1', data={'key': 'new_value'})
print(response.json())

# DELETE request
response = DELETE('https://api.example.com/data/1')
print(response.status_code)

# PATCH request
response = PATCH('https://api.example.com/data/1', data={'key': 'updated_value'})
print(response.json())

# OPTIONS request
response = OPTIONS('https://api.example.com/data')
print(response.headers)

# HEAD request
response = HEAD('https://api.example.com/data')
print(response.headers)

# SAFE GET request with error handling
response = SAFE_GET('https://api.example.com/data')
print(response)
```

### Custom Headers

```sh
from pysnippets.api import GET_with_headers, POST_with_headers

# GET request with custom headers
response = GET_with_headers('https://api.example.com/data', headers={'Custom-Header': 'value'})
print(response.json())

# POST request with custom headers
response = POST_with_headers('https://api.example.com/data', data={'key': 'value'}, headers={'Custom-Header': 'value'})
print(response.json())
```

### Timeout Handling

```sh
from pysnippets.api import GET_with_timeout, POST_with_timeout

# GET request with timeout
response = GET_with_timeout('https://api.example.com/data', timeout=5)
print(response.json())

# POST request with timeout
response = POST_with_timeout('https://api.example.com/data', data={'key': 'value'}, timeout=5)
print(response.json())
```

### Retry Mechanism

```sh
from pysnippets.api import GET_with_retry, POST_with_retry

# GET request with retry mechanism
response = GET_with_retry('https://api.example.com/data')
print(response.json())

# POST request with retry mechanism
response = POST_with_retry('https://api.example.com/data', data={'key': 'value'})
print(response.json())
```

### File Upload

```sh
from pysnippets.api import POST_file

# POST request for file upload
response = POST_file('https://api.example.com/upload', file_path='path/to/file.txt')
print(response.json())
```

### File Download

```sh
from pysnippets.api import download_file

# Download file
file_path = download_file('https://example.com/file.zip', 'local_file.zip')
print(f'File downloaded to {file_path}')
```
