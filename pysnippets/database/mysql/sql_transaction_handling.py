def execute_transaction(connection, queries):
    """
    Executes multiple SQL queries in a transaction with commit and rollback.

    Args:
        connection: The database connection object.
        queries (list): A list of SQL queries to execute.

    Returns:
        bool: True if transaction was committed, False if rolled back.
    """
    cursor = connection.cursor()
    try:
        for query in queries:
            cursor.execute(query)
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        print(f"Transaction failed: {e}")
        return False
    finally:
        cursor.close()
