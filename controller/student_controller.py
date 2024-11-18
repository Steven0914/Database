import query.student_query as query


def student_menu(cursor, connection):
    user_id = input("학번을 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")

    cursor.execute(query.student_login, (user_id, password))
    result = cursor.fetchone()

    if result is None:
        print("로그인 실패! 학번 또는 비밀번호가 잘못되었습니다.\n")
        return

    student_name = result[0]
    print(f"\n환영합니다, {student_name}님!")

    while True:
        print("\n===== 학생 메뉴 =====")
        print("0. 본인 정보 조회")
        print("1. 동아리 가입 신청")
        print("2. 개인 정보 변경")
        print("3. 동아리 활동 참여")
        print("4. 동아리 리스트 조회")
        print("5. 본인이 참여한 활동 조회")

        print("99. 이전 메뉴로 돌아가기")

        try:
            choice = input("학생 메뉴에서 무엇을 하시겠습니까?: ")

            if choice == '0':
                print("본인 정보 조회")
            elif choice == '1':
                print("동아리 가입 신청")
            elif choice == '2':
                print("개인 정보 변경")
            elif choice == '3':
                print("동아리 활동 참여")
            elif choice == '4':
                print("동아리 리스트 조회")
            elif choice == '5':
                print("본인이 참여한 활동 조회")
            elif choice == '6':
                print("동아리 탈퇴(동아리 소속시에만 가능)")
            elif choice == '99':
                print("이전 메뉴로 돌아갑니다.\n")
                break
            else:
                print("잘못된 입력입니다. 1~6 사이의 숫자를 입력해주세요.")
        except Exception as e:
            print(f"에러 발생: {e}")