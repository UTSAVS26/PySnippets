import psycopg2
import mysql.connector

def connect_to_mysql(host, user, password, database):
    """
    Connects to a MySQL database.

    Args:
        host (str): The database server address.
        user (str): The username for the database.
        password (str): The password for the user.
        database (str): The name of the database to connect to.

    Returns:
        mysql.connector.connection.MySQLConnection: Connection object if successful.
    """
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connection

def connect_to_postgresql(host, user, password, database):
    """
    Connects to a PostgreSQL database.

    Args:
        host (str): The database server address.
        user (str): The username for the database.
        password (str): The password for the user.
        database (str): The name of the database to connect to.

    Returns:
        psycopg2.extensions.connection: Connection object if successful.
    """
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connection
