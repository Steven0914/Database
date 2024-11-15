import mysql.connector
from config import DB_INFO

connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="pooling",
    pool_size=5,
    **DB_INFO
)

def get_connection():
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    return connection, cursor

def close_connection(connection, cursor):
    cursor.close()
    if connection.is_connected():
        connection.close()