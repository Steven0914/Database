from database.connect_db import get_connection, close_connection

def main():
    try:
        connection, cursor = get_connection()
        print("DB 연결 성공")


        close_connection(connection, cursor)
        print("DB 종료 성공")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()