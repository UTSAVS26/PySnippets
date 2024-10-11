def bulk_insert(connection, table, data):
    """
    Inserts multiple rows into an SQL table.

    Args:
        connection: The database connection object.
        table (str): The name of the table to insert data into.
        data (list of tuple): A list of tuples representing the rows to insert.

    Returns:
        None
    """
    cursor = connection.cursor()
    placeholders = ', '.join(['%s'] * len(data[0]))
    query = f"INSERT INTO {table} VALUES ({placeholders})"
    cursor.executemany(query, data)
    connection.commit()
    cursor.close()
