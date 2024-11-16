def admin_menu(cursor, connection):
    user_id = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")

    # 로그인 로직

    login_successful = True
    if not login_successful:
        print("로그인 실패! 이전 메뉴로 돌아갑니다.\n")
        return

    while True:
        print("\n===== 관리자 메뉴 =====")
        print("1. 데이터베이스 초기화")
        print("2. 동아리 지도 교수 배정")
        print("3. 학생 추가")
        print("4. 학생 학부 변경")
        print("5. 동아리 생성")
        print("6. 전체 동아리 통계 보기")
        print("7. 동아리 회장 변경")
        print("8. 교수 추가")
        print("9. 이전 메뉴로 돌아가기")

        try:
            choice = input("관리자 메뉴에서 무엇을 하시겠습니까?: ")

            if choice == '1':
                print("데이터베이스 초기화")
            elif choice == '2':
                print("동아리 지도 교수 배정")
            elif choice == '3':
                print("학생 추가")
            elif choice == '4':
                print("학생 학부 변경")
            elif choice == '5':
                print("동아리 생성")
            elif choice == '6':
                print("전체 동아리 통계 보기")
            elif choice == '7':
                print("동아리 회장 변경")
            elif choice == '8':
                print("교수 추가")
            elif choice == '9':
                print("이전 메뉴로 돌아갑니다.\n")
                break
            else:
                print("잘못된 입력입니다. 1~9 사이의 숫자를 입력해주세요.")
        except Exception as e:
            print(f"에러 발생: {e}")