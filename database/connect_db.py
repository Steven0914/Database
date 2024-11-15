import mysql.connector
from config import DB_INFO

try:
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(
        pool_name="pooling",
        pool_size=5,
        **DB_INFO
    )
except mysql.connector.Error as e:
    print(f"커넥션 풀 생성 실패: {e}")
    connection_pool = None
    raise

def get_connection():
    try:
        connection = connection_pool.get_connection()
        cursor = connection.cursor()
        return connection, cursor
    except mysql.connector.Error as e:
        print(f"DB 연결 에러: {e}")
        raise

def close_connection(connection, cursor):
    cursor.close()
    if connection.is_connected():
        connection.close()