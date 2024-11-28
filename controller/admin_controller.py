from config import ADMIN_PASSWORD
from database.init_db import initialize_database
from service.admin_service import add_student, add_club, change_supervisor, get_club_info, change_president, \
    add_professor, get_student_list, get_professor_list


def admin_menu(cursor, connection):
    password = input("비밀번호를 입력하세요: ")

    login_successful = False
    if password == ADMIN_PASSWORD:
        login_successful = True

    if not login_successful:
        print("로그인 실패! 이전 메뉴로 돌아갑니다.\n")
        return

    print("\n로그인 성공! 관리자 메뉴로 이동합니다.")

    while True:
        print("\n===== 관리자 메뉴 =====")
        print("1. 데이터베이스 초기화")
        print("2. 학생 추가")
        print("3. 동아리 생성")
        print("4. 동아리 지도 교수 변경")
        print("5. 전체 동아리 통계 보기")
        print("6. 동아리 회장 변경")
        print("7. 교수 추가")
        print("8. 학생 리스트 조회")
        print("9. 교수 리스트 조회")
        print("99. 이전 메뉴로 돌아가기")

        try:
            choice = input("관리자 메뉴에서 무엇을 하시겠습니까?: ")
            if choice == '1':
                initialize_database()
                print("데이터베이스가 초기화되었습니다.")
            elif choice == '2':
                add_student(cursor, connection)
            elif choice == '3':
                add_club(cursor, connection)
            elif choice == '4':
                change_supervisor(cursor, connection)
            elif choice == '5':
                get_club_info(cursor)
            elif choice == '6':
                change_president(cursor, connection)
            elif choice == '7':
                add_professor(cursor, connection)
            elif choice == '8':
                get_student_list(cursor)
            elif choice == '9':
                get_professor_list(cursor)
            elif choice == '99':
                print("이전 메뉴로 돌아갑니다.\n")
                break
            else:
                print("잘못된 입력입니다. 1~9 사이의 숫자를 입력해주세요.")
        except Exception as e:
            print(f"에러 발생: {e}")