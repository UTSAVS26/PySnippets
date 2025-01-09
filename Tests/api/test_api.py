import unittest
from unittest.mock import patch, Mock
from pysnippets.api import (
    GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD, SAFE_GET,
    GET_with_headers, POST_with_headers, GET_with_timeout, POST_with_timeout,
    GET_with_retry, POST_with_retry, GET_with_user_agent, POST_with_user_agent,
    GET_with_params, POST_with_params, GET_with_session, POST_with_session,
    POST_file, download_file
)

class TestAPIRequests(unittest.TestCase):

    @patch('pysnippets.api.requests.get')
    def test_GET(self, mock_get):
        mock_get.return_value = Mock(status_code=200, json=lambda: {'key': 'value'})
        response = GET('https://api.example.com/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'key': 'value'})

    @patch('pysnippets.api.requests.post')
    def test_POST(self, mock_post):
        mock_post.return_value = Mock(status_code=201, json=lambda: {'key': 'value'})
        response = POST('https://api.example.com/data', data={'key': 'value'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'key': 'value'})

    @patch('pysnippets.api.requests.put')
    def test_PUT(self, mock_put):
        mock_put.return_value = Mock(status_code=200, json=lambda: {'key': 'updated_value'})
        response = PUT('https://api.example.com/data/1', data={'key': 'updated_value'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'key': 'updated_value'})

    @patch('pysnippets.api.requests.delete')
    def test_DELETE(self, mock_delete):
        mock_delete.return_value = Mock(status_code=204)
        response = DELETE('https://api.example.com/data/1')
        self.assertEqual(response.status_code, 204)

    @patch('pysnippets.api.requests.patch')
    def test_PATCH(self, mock_patch):
        mock_patch.return_value = Mock(status_code=200, json=lambda: {'key': 'patched_value'})
        response = PATCH('https://api.example.com/data/1', data={'key': 'patched_value'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'key': 'patched_value'})

    @patch('pysnippets.api.requests.options')
    def test_OPTIONS(self, mock_options):
        mock_options.return_value = Mock(status_code=200, headers={'Allow': 'GET, POST'})
        response = OPTIONS('https://api.example.com/data')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Allow', response.headers)

    @patch('pysnippets.api.requests.head')
    def test_HEAD(self, mock_head):
        mock_head.return_value = Mock(status_code=200, headers={'Content-Type': 'application/json'})
        response = HEAD('https://api.example.com/data')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Content-Type', response.headers)

    @patch('pysnippets.api.requests.get')
    def test_SAFE_GET(self, mock_get):
        mock_get.return_value = Mock(status_code=200, json=lambda: {'key': 'value'})
        response = SAFE_GET('https://api.example.com/data')
        self.assertEqual(response, {'key': 'value'})

    @patch('pysnippets.api.requests.get')
    def test_GET_with_headers(self, mock_get):
        mock_get.return_value = Mock(status_code=200, json=lambda: {'key': 'value'})
        response = GET_with_headers('https://api.example.com/data', headers={'Custom-Header': 'value'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'key': 'value'})

    @patch('pysnippets.api.requests.post')
    def test_POST_with_headers(self, mock_post):
        mock_post.return_value = Mock(status_code=201, json=lambda: {'key': 'value'})
        response = POST_with_headers('https://api.example.com/data', data={'key': 'value'}, headers={'Custom-Header': 'value'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'key': 'value'})

    @patch('pysnippets.api.requests.get')
    def test_GET_with_timeout(self, mock_get):
        mock_get.return_value = Mock(status_code=200, json=lambda: {'key': 'value'})
        response = GET_with_timeout('https://api.example.com/data', timeout=5)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'key': 'value'})

    @patch('pysnippets.api.requests.post')
    def test_POST_with_timeout(self, mock_post):
        mock_post.return_value = Mock(status_code=201, json=lambda: {'key': 'value'})
        response = POST_with_timeout('https://api.example.com/data', data={'key': 'value'}, timeout=5)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'key': 'value'})

    @patch('pysnippets.api.requests_retry_session')
    def test_GET_with_retry(self, mock_retry_session):
        mock_session = Mock()
        mock_retry_session.return_value = mock_session
        mock_session.get.return_value = Mock(status_code=200, json=lambda: {'key': 'value'})
        response = GET_with_retry('https://api.example.com/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'key': 'value'})

    @patch('pysnippets.api.requests_retry_session')
    def test_POST_with_retry(self, mock_retry_session):
        mock_session = Mock()
        mock_retry_session.return_value = mock_session
        mock_session.post.return_value = Mock(status_code=201, json=lambda: {'key': 'value'})
        response = POST_with_retry('https://api.example.com/data', data={'key': 'value'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'key': 'value'})

    @patch('pysnippets.api.requests.get')
    def test_GET_with_user_agent(self, mock_get):
        mock_get.return_value = Mock(status_code=200, json=lambda: {'key': 'value'})
        response = GET_with_user_agent('https://api.example.com/data', user_agent='MyApp/1.0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'key': 'value'})

    @patch('pysnippets.api.requests.post')
    def test_POST_with_user_agent(self, mock_post):
        mock_post.return_value = Mock(status_code=201, json=lambda: {'key': 'value'})
        response = POST_with_user_agent('https://api.example.com/data', data={'key': 'value'}, user_agent='MyApp/1.0')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'key': 'value'})

    @patch('pysnippets.api.requests.get')
    def test_GET_with_params(self, mock_get):
        mock_get.return_value = Mock(status_code=200, json=lambda: {'key': 'value'})
        response = GET_with_params('https://api.example.com/data', params={'key': 'value'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'key': 'value'})

    @patch('pysnippets.api.requests.post')
    def test_POST_with_params(self, mock_post):
        mock_post.return_value = Mock(status_code=201, json=lambda: {'key': 'value'})
        response = POST_with_params('https://api.example.com/data', data={'key': 'value'}, params={'param': 'value'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'key': 'value'})

    @patch('pysnippets.api.requests.Session.get')
    def test_GET_with_session(self, mock_get):
        mock_get.return_value = Mock(status_code=200, json=lambda: {'key': 'value'})
        response = GET_with_session('https://api.example.com/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'key': 'value'})

    @patch('pysnippets.api.requests.Session.post')
    def test_POST_with_session(self, mock_post):
        mock_post.return_value = Mock(status_code=201, json=lambda: {'key': 'value'})
        response = POST_with_session('https://api.example.com/data', data={'key': 'value'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'key': 'value'})

    @patch('pysnippets.api.requests.post')
    def test_POST_file(self, mock_post):
        mock_post.return_value = Mock(status_code=201, json=lambda: {'key': 'value'})
        response = POST_file('https://api.example.com/upload', 'path/to/file.txt')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'key': 'value'})

    @patch('pysnippets.api.requests.get')
    def test_download_file(self, mock_get):
        mock_get.return_value = Mock(status_code=200, iter_content=lambda chunk_size: [b'content'])
        file_path = download_file('https://example.com/file.zip', 'local_file.zip')
        self.assertEqual(file_path, 'local_file.zip')
        with open(file_path, 'rb') as file:
            self.assertEqual(file.read(), b'content')

if __name__ == '__main__':
    unittest.main()