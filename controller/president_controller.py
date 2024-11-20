import query.president_query as query
from service.president_service import update_club_name, create_activity, manage_apply, get_activity_list


def president_menu(cursor, connection):
    try:
        user_id = input("학번을 입력하세요: ")
        user_name = input("비밀번호를 입력하세요: ")

        cursor.execute(query.president_login, (user_id, user_name))
        result = cursor.fetchone()

        if result is None:
            print("로그인 실패!\n")
            return

        club_name = result[0]
        president_name = result[1]
        print(f"\n환영합니다, {president_name}님! 현재 운영 중인 동아리는 '{club_name}'입니다.")

        while True:
            cursor.execute(query.president_login, (user_id, user_name))
            result = cursor.fetchone()
            club_name = result[0]
            print("\n===== 동아리 회장 메뉴 =====")
            print(f"운영 중인 동아리: {club_name}")
            print("1. 동아리 이름 변경")
            print("2. 동아리 활동 생성")
            print("3. 학생 동아리 가입 승인 및 거절")
            print("4. 운영 동아리의 활동 조회")
            print("5. 운영 동아리 인원 조회")
            print("6. 동아리 활동 조회")
            print("7. 동아리원 강퇴")
            print("8. 활동 정보 변경")
            print("9. 활동장소 변경")
            print("99. 이전 메뉴로 돌아가기")

            choice = input("회장 메뉴에서 무엇을 하시겠습니까?: ")

            if choice == '1':
                update_club_name(cursor, connection, club_name)
            elif choice == '2':
                create_activity(cursor, connection, club_name)
            elif choice == '3':
                manage_apply(cursor, connection, club_name)
            elif choice == '4':
                get_activity_list(cursor, club_name)
            elif choice == '5':
                print("운영 동아리 인원 조회")
            elif choice == '6':
                print("동아리 활동 조회")
            elif choice == '7':
                print("동아리원 강퇴")
            elif choice == '8':
                print("활동 정보 변경")
            elif choice == '9':
                print("활동장소 변경")

            elif choice == '99':
                print("이전 메뉴로 돌아갑니다.\n")
                break
            else:
                print("잘못된 입력입니다. 1~9 사이의 숫자를 입력해주세요.")
    except Exception as e:
                print(f"에러 발생: {e}")