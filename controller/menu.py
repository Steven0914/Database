from controller.admin import admin_menu
from controller.president import president_menu
from controller.student import student_menu


def start_menu (connection, cursor):
    print(r'''
===================================================================
:......::::...::...:::::::......:::........:::.......:::........:::          
:'######::'##:::::'##:::::'######::'##:::::::'##::::'##:'########::
'##... ##: ##:'##: ##::::'##... ##: ##::::::: ##:::: ##: ##.... ##:
 ##:::..:: ##: ##: ##:::: ##:::..:: ##::::::: ##:::: ##: ##:::: ##:
. ######:: ##: ##: ##:::: ##::::::: ##::::::: ##:::: ##: ########::
:..... ##: ##: ##: ##:::: ##::::::: ##::::::: ##:::: ##: ##.... ##:
'##::: ##: ##: ##: ##:::: ##::: ##: ##::::::: ##:::: ##: ##:::: ##:
. ######::. ###. ###:::::. ######:: ########:. #######:: ########::
:......::::...::...:::::::......:::........:::.......:::........:::          
===================================================================
SoftWare CLUB Management System                            (v1.0.0)
    ''')

    while True:
        print("===== 역할 선택 =====")
        print("1. 관리자")
        print("2. 동아리 회장")
        print("3. 학생")
        print("4. 프로그램 종료")

        try:
            choice = input("어떤 사용자로 접속할까요?: ")

            if choice == '1':
                admin_menu(cursor, connection)
            elif choice == '2':
                president_menu(cursor, connection)
            elif choice == '3':
                student_menu(cursor, connection)
            elif choice == '4':
                print("프로그램이 종료됩니다.")
                break
            else:
                print("잘못된 입력입니다. 1~4 사이의 올바른 역할을 선택해주세요.")
        except Exception as e:
            print(f"에러 발생: {e}")
            continue