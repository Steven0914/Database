import query.student_query as query

def get_info(cursor, user_id):
    try:
        cursor.execute(query.get_info, (user_id,))
        result = cursor.fetchone()

        if not result:
            print("본인 정보를 찾을 수 없습니다.")
            return

        학번, 이름, 소속학부, 소속동아리, 연락처, 생일, 가입일 = result

        print("\n===== 본인 정보 =====")
        print(f"학번: {학번}")
        print(f"이름: {이름}")
        print(f"소속 학부: {소속학부}")
        print(f"소속 동아리: {소속동아리 if 소속동아리 else '없음'}")
        print(f"연락처: {연락처}")
        print(f"생일: {생일.strftime('%Y-%m-%d')}")
        print(f"가입일: {가입일.strftime('%Y-%m-%d') if 가입일 else '미가입'}")
        print("===================")
    except Exception as e:
        print(f"본인 정보 조회 중 오류가 발생했습니다: {e}")


def get_club_list(cursor):
    try:
        cursor.execute(query.get_club_list)
        results = cursor.fetchall()

        if not results:
            print("등록된 동아리가 없습니다.")
            return

        print("\n=================== 동아리 리스트 ===================")
        print(f"{'동아리명':<20} {'회장':<15} {'지도교수':<15}")
        print("=" * 50)

        for row in results:
            동아리명, 동아리회장, 지도교수 = row
            동아리회장 = 동아리회장 if 동아리회장 else "없음"
            지도교수 = 지도교수 if 지도교수 else "없음"
            print(f"{동아리명:<20} {동아리회장:<15} {지도교수:<15}")
        print("=" * 50)
    except Exception as e:
        print(f"동아리 리스트 조회 중 오류가 발생했습니다: {e}")