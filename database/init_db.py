from database.connect_db import get_connection, close_connection

def initialize_database():
    try:
        connection, cursor = get_connection()

        with open('sw_club.sql', 'r', encoding='utf-8') as f:
            sql_script = f.read()

        # 여러 SQL 문장을 실행하기 위해, 세미콜론으로 구분된 문장을 실행
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)

        # 변경사항 커밋
        connection.commit()
    except Exception as e:
        print(f"오류 발생: {e}")

    finally:
        close_connection(connection, cursor)