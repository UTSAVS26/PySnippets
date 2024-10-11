def create_table(connection, create_table_query):
    """
    Creates a table with the given SQL query.

    Args:
        connection: The database connection object.
        create_table_query (str): SQL query to create a table.

    Returns:
        None
    """
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
