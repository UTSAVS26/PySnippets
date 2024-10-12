def insert_document(collection, document):
    """
    Inserts a document into a MongoDB collection.

    Args:
        collection: The MongoDB collection object.
        document (dict): The document to insert.

    Returns:
        ObjectId: The ID of the inserted document.
    """
    result = collection.insert_one(document)
    return result.inserted_id
