import unittest
from unittest.mock import patch, MagicMock
from pysnippets.database.mysql.sql_connection_manager import *
from pysnippets.database.mysql.sql_transaction_handling import *
from pysnippets.database.mysql.sql_schema_creation import *
from pysnippets.database.mysql.sql_execute_query import *
from pysnippets.database.mysql.sql_data_insertion import *


class TestMySQLSnippets(unittest.TestCase):

    @patch("mysql.connector.connect")
    def test_connect_to_mysql(self, mock_connect):
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        connection = connect_to_mysql("localhost", "user", "password", "database")

        mock_connect.assert_called_once_with(
            host="localhost", user="user", password="password", database="database"
        )
        self.assertEqual(connection, mock_connection)

    @patch("mysql.connector.connect")
    def test_execute_query(self, mock_connect):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        query = "SELECT * FROM users"
        mock_cursor.fetchall.return_value = [(1, "Alice")]

        result = execute_query(mock_connection, query)

        mock_cursor.execute.assert_called_once_with(query, None)
        self.assertEqual(result, [(1, "Alice")])

    @patch("mysql.connector.connect")
    def test_bulk_insert(self, mock_connect):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        data = [(1, "Alice"), (2, "Bob")]
        table = "users"
        bulk_insert(mock_connection, table, data)

        mock_cursor.executemany.assert_called_once()
        self.assertEqual(mock_connection.commit.call_count, 1)

    @patch("mysql.connector.connect")
    def test_execute_transaction(self, mock_connect):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        queries = ["INSERT INTO users (id, name) VALUES (3, 'Charlie')"]
        result = execute_transaction(mock_connection, queries)

        mock_cursor.execute.assert_called_with(queries[0])
        self.assertTrue(result)
        self.assertEqual(mock_connection.commit.call_count, 1)

    @patch("mysql.connector.connect")
    def test_create_table(self, mock_connect):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        create_table_query = "CREATE TABLE users (id INT, name VARCHAR(100))"
        create_table(mock_connection, create_table_query)

        mock_cursor.execute.assert_called_once_with(create_table_query)
        self.assertEqual(mock_connection.commit.call_count, 1)


if __name__ == "__main__":
    unittest.main()
