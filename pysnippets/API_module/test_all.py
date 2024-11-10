import unittest
from unittest.mock import patch, MagicMock
from requests.exceptions import RequestException
from api_requests import get, post, put, delete, get_with_path_params
from query_params import serialize_params
from path_params import construct_url
from response_handling import handle_response

class TestAPIRequests(unittest.TestCase):

    @patch('requests.Session.get')
    def test_get_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b'{"key": "value"}'
        mock_get.return_value = mock_response

        response = get("https://jsonplaceholder.typicode.com/posts/1")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    @patch('requests.Session.get')
    def test_get_failure(self, mock_get):
        mock_get.side_effect = RequestException("Connection Error")

        response = get("https://jsonplaceholder.typicode.com/posts/1")
        self.assertIsNone(response)

    @patch('requests.post')
    def test_post(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_post.return_value = mock_response

        response = post("https://jsonplaceholder.typicode.com/posts", data={"key": "value"})
        self.assertEqual(response.status_code, 201)

    @patch('requests.put')
    def test_put(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_put.return_value = mock_response

        response = put("https://jsonplaceholder.typicode.com/posts/1", data={"key": "value"})
        self.assertEqual(response.status_code, 200)

    @patch('requests.delete')
    def test_delete(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 204
        mock_delete.return_value = mock_response

        response = delete("https://jsonplaceholder.typicode.com/posts/1")
        self.assertEqual(response.status_code, 204)

    @patch('requests.get')
    def test_get_with_path_params(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b'{"key": "value"}'
        mock_get.return_value = mock_response

        response = get_with_path_params("https://jsonplaceholder.typicode.com/posts", ["1"])
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

class TestQueryParams(unittest.TestCase):

    def test_serialize_params(self):
        params = {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3"
        }
        result = serialize_params(params)
        expected = "key1=value1&key2=value2&key3=value3"
        self.assertEqual(result, expected)

class TestPathParams(unittest.TestCase):

    def test_construct_url(self):
        base_url = "https://jsonplaceholder.typicode.com"
        path_params = ["posts", "1"]
        result = construct_url(base_url, path_params)
        expected = "https://jsonplaceholder.typicode.com/posts/1"
        self.assertEqual(result, expected)

class TestResponseHandling(unittest.TestCase):

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_handle_response_zip(self, mock_open):
        mock_response = MagicMock()
        mock_response.headers = {'Content-Type': 'application/zip'}
        mock_response.content = b'PK\x03\x04'  # Mock zip file content

        handle_response(mock_response, "/fake/path")
        mock_open.assert_called_once_with('temp.zip', 'wb')

    @patch('logging.info')
    def test_handle_response_non_zip(self, mock_logging_info):
        mock_response = MagicMock()
        mock_response.headers = {'Content-Type': 'application/json'}
        mock_response.content = b'{"key": "value"}'

        handle_response(mock_response, "/fake/path")
        mock_logging_info.assert_called_with("Response content type: {content_type} - no special handling applied.")

if __name__ == "__main__":
    unittest.main()