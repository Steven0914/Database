import mysql.connector
from config import DB_INFO

try:
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(
        pool_name="pooling",
        pool_size=5,
        **DB_INFO
    )
except mysql.connector.Error as e:
    # 데이터베이스가 존재하지 않을 때
    if e.errno == 1049:
        try:
            # 데이터베이스 생성을 위한 임시 연결
            db_info_without_database = DB_INFO.copy()
            db_info_without_database.pop('database', None)
            connection = mysql.connector.connect(**db_info_without_database)
            cursor = connection.cursor()

            # 데이터베이스 생성
            cursor.execute(f"CREATE DATABASE {DB_INFO['database']}")
            print(f"데이터베이스 '{DB_INFO['database']}' 생성 성공.")

            cursor.close()
            connection.close()

            # 다시 커넥션 풀 생성
            connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="pooling",
                pool_size=5,
                **DB_INFO
            )

        except mysql.connector.Error as e:
            print(f"데이터베이스 생성 실패: {e}")
            connection_pool = None
            raise
    else:
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