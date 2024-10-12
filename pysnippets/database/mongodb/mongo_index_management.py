def create_index(collection, field, unique=False):
    """
    Creates an index on a specified field in a MongoDB collection.

    Args:
        collection: The MongoDB collection object.
        field (str): The field to create the index on.
        unique (bool, optional): If True, creates a unique index.

    Returns:
        str: The name of the created index.
    """
    index_name = collection.create_index([(field, 1)], unique=unique)
    return index_name

def drop_index(collection, index_name):
    """
    Drops a specific index from a MongoDB collection.

    Args:
        collection: The MongoDB collection object.
        index_name (str): The name of the index to drop.

    Returns:
        None
    """
    collection.drop_index(index_name)
