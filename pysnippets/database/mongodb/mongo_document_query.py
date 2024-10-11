def query_documents(collection, filter_criteria=None, projection=None):
    """
    Queries documents from a MongoDB collection based on filters and projections.

    Args:
        collection: The MongoDB collection object.
        filter_criteria (dict, optional): The query filter.
        projection (dict, optional): The fields to include or exclude.

    Returns:
        list: List of documents matching the filter.
    """
    filter_criteria = filter_criteria or {}
    projection = projection or {}
    documents = collection.find(filter_criteria, projection)
    return list(documents)
