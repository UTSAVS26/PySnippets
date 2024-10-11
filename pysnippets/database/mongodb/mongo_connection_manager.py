from pymongo import MongoClient

def connect_to_mongodb(uri):
    """
    Connects to a MongoDB instance.

    Args:
        uri (str): MongoDB URI string.

    Returns:
        pymongo.MongoClient: MongoDB connection object.
    """
    client = MongoClient(uri)
    return client
