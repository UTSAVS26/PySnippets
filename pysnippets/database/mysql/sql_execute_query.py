def execute_query(connection, query, params=None):
    """
    Executes a SQL query (SELECT, INSERT, UPDATE, DELETE).

    Args:
        connection: The database connection object.
        query (str): The SQL query to execute.
        params (tuple, optional): The parameters for the query.

    Returns:
        list: The result of a SELECT query, or None for other queries.
    """
    cursor = connection.cursor()
    cursor.execute(query, params)
    
    if query.strip().upper().startswith('SELECT'):
        result = cursor.fetchall()
    else:
        connection.commit()
        result = None
    
    cursor.close()
    return result
