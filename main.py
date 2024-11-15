from controller.menu import start_menu
from database.connect_db import get_connection, close_connection
from database.init_db import initialize_database


def main():
    try:
        # DB 초기화
        initialize_database()

        # DB 연결
        connection, cursor = get_connection()

        # 메뉴 시작
        start_menu(connection, cursor)

        # DB 연결 종료
        close_connection(connection, cursor)
    except Exception as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    main()