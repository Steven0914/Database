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



def apply_club(cursor, connection, student_id):
    try:
        club_name = input("\n가입 신청할 동아리 이름을 입력하세요: ")
        cursor.execute(query.find_club, (club_name,))
        result = cursor.fetchone()
        club_id = result[0]
        cursor.execute(query.apply_to_club, (club_id, student_id))
        connection.commit()
        print("\n동아리 신청이 완료되었습니다.")
    except Exception as e:
        if "Duplicate entry" in str(e):
            print("\n이미 가입 신청한 동아리입니다.")
        elif "a foreign key constraint fails" in str(e):
            print("\n존재하지 않는 동아리 번호이거나 잘못된 학번입니다.")
        else:
            print(f"\n동아리 가입 신청 중 오류가 발생했습니다: {e}")


def participate_activity(cursor, connection, student_id):
    try:
        cursor.execute(query.get_student_club, (student_id,))
        club_result = cursor.fetchone()

        if not club_result or not club_result[0]:
            print("소속된 동아리가 없습니다. 활동에 참여하려면 동아리에 가입하세요.")
            return
        소속동아리번호 = club_result[0]

        cursor.execute(query.get_available_activities, (소속동아리번호,))
        activities = cursor.fetchall()

        if not activities:
            print("소속된 동아리의 참여 가능한 활동이 없습니다.")
            return

        print("동아리 활동 참여 안내: 참여 가능한 활동은 오늘 이후의 활동 중 참여인원이 20명 미만인 활동입니다.\n")

        print("======== 참여 가능한 동아리 활동 리스트 ========")
        print(f"{'활동번호':<5} {'활동명':<10} {'날짜':<10} {'시간':<2} {'참여인원':<2}")
        print("=" * 50)
        for 활동번호, 활동명, 날짜, 활동시간, 참여인원 in activities:
            날짜 = 날짜.strftime("%Y-%m-%d")
            print(f"{활동번호:<5} {활동명:<10} {날짜:<10}    {활동시간:<2} {참여인원:<2}")
        print("=" * 50)

        활동번호 = input("참여할 활동의 활동번호를 입력하세요: ").strip()
        cursor.execute(query.check_activity_participation, (활동번호, student_id))
        already_participated = cursor.fetchone()

        if already_participated:
            print("이미 해당 활동에 참여 중입니다.")
            return

        cursor.execute(query.add_activity_participation, (활동번호, student_id))
        connection.commit()
        print(f"활동번호 {활동번호} 활동에 성공적으로 참여하였습니다.")

    except Exception as e:
        connection.rollback()
        print(f"동아리 활동 참여 중 오류가 발생했습니다: {e}")


def add_activity_content(cursor, connection, student_id):
    try:
        cursor.execute(query.get_participated_activities, (student_id,))
        activities = cursor.fetchall()

        if not activities:
            print("참여 중인 활동이 없습니다.")
            return

        print("======== 참여 중인 활동 리스트 ========")
        print(f"{'활동번호':<10} {'활동명':<15} {'날짜':<10} {'활동시간':<5}")
        print("=" * 50)
        for 활동번호, 활동명, 날짜, 활동시간 in activities:
            날짜 = 날짜.strftime("%Y-%m-%d")
            print(f"{활동번호:<10} {활동명:<15} {날짜:<10} {활동시간:<5}")
        print("=" * 50)

        활동번호 = input("내용을 추가할 활동의 활동번호를 입력하세요: ").strip()
        selected_activity = next((a for a in activities if str(a[0]) == 활동번호), None)

        if not selected_activity:
            print("잘못된 활동번호를 입력하였습니다.")
            return

        내용 = input("추가할 내용을 입력하세요: ").strip()
        if not 내용:
            print("내용이 비어있습니다. 다시 시도하세요.")
            return

        cursor.execute(query.add_activity_content, (활동번호, 내용))
        connection.commit()
        print(f"활동번호 {활동번호}의 내용이 성공적으로 추가되었습니다.")

    except Exception as e:
        connection.rollback()
        print(f"활동 내용 추가 중 오류가 발생했습니다: {e}")


def get_activity_list(cursor, 학번):
    try:
        cursor.execute(query.get_activity_list, (학번,))
        활동 = cursor.fetchall()

        if not 활동:
            print("참여한 활동이 없습니다.")
            return

        print("\n======== 내가 참여한 활동 목록 ========")
        for 활동번호, 활동명, 날짜, 시간, 내용, 주소, 장소유형, 참여학생수 in 활동:
            print(f"활동번호: {활동번호}")
            print(f"활동명: {활동명}")
            print(f"날짜: {날짜.strftime('%Y-%m-%d')}")
            print(f"시간: {시간}시간")
            내용 = 내용 or "활동 내용 없음"
            print(f"활동 내용:\n{내용}")
            주소 = 주소 or "장소 정보 없음"
            장소유형 = 장소유형 or "장소 유형 없음"
            print(f"장소: {주소} ({장소유형})")
            print(f"참여 학생 수: {참여학생수}명")
            print("-" * 50)
        print("=" * 50)

    except Exception as 오류:
        print(f"참여 활동 조회 중 오류가 발생했습니다: {오류}")


def update_student_info(cursor, connection, student_id):
    try:
        cursor.execute(query.get_student_info, (student_id,))
        current_info = cursor.fetchone()

        if not current_info:
            print("학생 정보를 찾을 수 없습니다.")
            return

        current_contact, current_password = current_info
        print("\n===== 개인정보 정보 수정 =====")
        new_contact = input("새로운 연락처를 입력하세요 (엔터: 기존 유지): ").strip()
        new_password = input("새로운 비밀번호를 입력하세요 (엔터: 기존 유지): ").strip()

        updated_contact = new_contact if new_contact else current_contact
        updated_password = new_password if new_password else current_password

        cursor.execute(query.update_student_info, (updated_contact, updated_password, student_id))
        connection.commit()

        if (updated_contact != current_contact) or (updated_password != current_password):
            print("\n정보가 성공적으로 수정되었습니다.")

        if updated_contact != current_contact:
            print(f"변경된 연락처: {updated_contact}")
        else:
            print("연락처는 변경되지 않았습니다.")

        if updated_password != current_password:
            print(f"변경된 비밀번호: {updated_password}")
        else:
            print("비밀번호는 변경되지 않았습니다.")

    except Exception as e:
        connection.rollback()
        print(f"정보 수정 중 오류가 발생했습니다: {e}")