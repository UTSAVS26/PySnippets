def update_document(collection, filter_criteria, update_data, multiple=False):
    """
    Updates one or more documents in a MongoDB collection.

    Args:
        collection: The MongoDB collection object.
        filter_criteria (dict): The query filter to match documents.
        update_data (dict): The update data.
        multiple (bool, optional): If True, updates all matching documents.

    Returns:
        dict: The update result details.
    """
    if multiple:
        result = collection.update_many(filter_criteria, {'$set': update_data})
    else:
        result = collection.update_one(filter_criteria, {'$set': update_data})
    return result.raw_result
