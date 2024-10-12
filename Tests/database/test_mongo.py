import unittest
from unittest.mock import patch, MagicMock
from pysnippets.database.mongodb.mongo_connection_manager import *
from pysnippets.database.mongodb.mongo_index_management import *
from pysnippets.database.mongodb.mongo_document_update import *
from pysnippets.database.mongodb.mongo_document_query import *
from pysnippets.database.mongodb.mongo_document_insertion import *


class TestMongoDBSnippets(unittest.TestCase):

    @patch("pymongo.MongoClient")
    def test_connect_to_mongodb(self, mock_mongo_client):
        mock_client = MagicMock()
        mock_mongo_client.return_value = mock_client

        client = connect_to_mongodb("mongodb://localhost:27017")

        mock_mongo_client.assert_called_once_with("mongodb://localhost:27017")
        self.assertEqual(client, mock_client)

    @patch("pymongo.collection.Collection.insert_one")
    def test_insert_document(self, mock_insert_one):
        mock_collection = MagicMock()
        mock_insert_one.return_value.inserted_id = "some_id"

        document = {"name": "Alice", "age": 30}
        result = insert_document(mock_collection, document)

        mock_insert_one.assert_called_once_with(document)
        self.assertEqual(result, "some_id")

    @patch("pymongo.collection.Collection.find")
    def test_query_documents(self, mock_find):
        mock_collection = MagicMock()
        mock_find.return_value = [{"name": "Alice"}, {"name": "Bob"}]

        filter_criteria = {"age": {"$gt": 25}}
        result = query_documents(mock_collection, filter_criteria)

        mock_find.assert_called_once_with(filter_criteria, {})
        self.assertEqual(result, [{"name": "Alice"}, {"name": "Bob"}])

    @patch("pymongo.collection.Collection.update_one")
    def test_update_document_single(self, mock_update_one):
        mock_collection = MagicMock()
        mock_update_one.return_value.raw_result = {"nModified": 1}

        filter_criteria = {"name": "Alice"}
        update_data = {"age": 31}
        result = update_document(
            mock_collection, filter_criteria, update_data, multiple=False
        )

        mock_update_one.assert_called_once_with(filter_criteria, {"$set": update_data})
        self.assertEqual(result, {"nModified": 1})

    @patch("pymongo.collection.Collection.update_many")
    def test_update_document_multiple(self, mock_update_many):
        mock_collection = MagicMock()
        mock_update_many.return_value.raw_result = {"nModified": 2}

        filter_criteria = {"age": {"$lt": 40}}
        update_data = {"status": "updated"}
        result = update_document(
            mock_collection, filter_criteria, update_data, multiple=True
        )

        mock_update_many.assert_called_once_with(filter_criteria, {"$set": update_data})
        self.assertEqual(result, {"nModified": 2})

    @patch("pymongo.collection.Collection.create_index")
    def test_create_index(self, mock_create_index):
        mock_collection = MagicMock()
        mock_create_index.return_value = "name_1"

        result = create_index(mock_collection, "name", unique=True)

        mock_create_index.assert_called_once_with([("name", 1)], unique=True)
        self.assertEqual(result, "name_1")

    @patch("pymongo.collection.Collection.drop_index")
    def test_drop_index(self, mock_drop_index):
        mock_collection = MagicMock()

        drop_index(mock_collection, "name_1")

        mock_drop_index.assert_called_once_with("name_1")


if __name__ == "__main__":
    unittest.main()
