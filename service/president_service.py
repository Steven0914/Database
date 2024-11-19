from datetime import datetime

import query.president_query as query


def update_club_name(cursor, connection, club_name):
    try:

        if not club_name:
            print("\n해당 동아리는 존재하지 않거나, 권한이 없습니다.")
            return

        print("\n===== 현재 동아리 정보 =====")
        print(f"동아리 명칭: {club_name}")
        print("===========================")

        new_name = input("새 동아리 명칭 (변경하지 않으려면 Enter): ") or club_name

        if new_name == club_name:
            print("\n변경할 정보가 없어 동아리 정보 변경을 취소합니다.")
            return

        cursor.execute(query.update_club_name,(new_name, club_name))
        connection.commit()

        print("\n동아리 정보가 성공적으로 업데이트되었습니다.")

    except Exception as e:
        print(f"\n동아리 정보 변경 중 오류가 발생했습니다: {e}")


def create_activity(cursor, connection, club_name):
    try:
        cursor.execute(query.get_club_id, (club_name,))
        club_info = cursor.fetchone()

        if not club_info:
            print("\n해당 동아리는 존재하지 않습니다.")
            return

        club_id = club_info[0]

        print("\n===== 활동 정보 입력 =====")
        activity_name = input("활동명: ").strip()
        if not activity_name:
            print("\n활동명을 입력해야 합니다.")
            return

        activity_date = input("활동 날짜 (예시 : YYYY-MM-DD): ").strip()
        try:
            activity_date = datetime.strptime(activity_date, "%Y-%m-%d").date()
        except ValueError:
            print("\n날짜 형식이 올바르지 않습니다.")
            return

        activity_duration = input("활동 시간 (단위: 시간): ").strip()
        try:
            activity_duration = int(activity_duration)
            if activity_duration <= 0:
                raise ValueError("활동 시간은 양의 정수여야 합니다.")
        except ValueError:
            print("\n활동 시간 형식이 올바르지 않습니다.")
            return

        cursor.execute(query.create_activity, (activity_name, activity_date, activity_duration, club_id))
        connection.commit()

        cursor.execute("SELECT LAST_INSERT_ID();")
        activity_id = cursor.fetchone()[0]

        print("\n활동이 성공적으로 생성되었습니다.")
        print(f"활동 번호: {activity_id}")
        print(f"활동명: {activity_name}")
        print(f"활동 날짜: {activity_date}")
        print(f"활동 시간: {activity_duration}시간")

    except Exception as e:
        connection.rollback()
        print(f"\n활동 생성 중 오류가 발생했습니다: {e}")



def manage_apply(cursor, connection,club_name):
    try:
        cursor.execute(query.get_club_id, (club_name,))
        동아리결과 = cursor.fetchone()
        if not 동아리결과:
            raise ValueError(f"'{club_name}' 동아리는 존재하지 않습니다.")

        동아리번호 = 동아리결과[0]

        cursor.execute(query.get_waiting_students , (동아리번호,))
        가입대기목록 = cursor.fetchall()

        if not 가입대기목록:
            print(f"동아리 '{club_name}'에 가입 대기 중인 학생이 없습니다.")
            return

        print("\n===== 가입 대기 목록 =====")
        print(f"{'학번':<10} {'이름':<20}")
        print("=" * 30)
        for 학번, 이름 in 가입대기목록:
            print(f"{학번:<10} {이름:<20}")
        print("=" * 30)

        while True:
            학번 = input("가입 승인/거절할 학번을 입력하세요 (종료하려면 'q' 입력): ").strip()
            if 학번.lower() == 'q':
                print("가입 관리가 종료되었습니다.")
                break

            학번 = int(학번)
            cursor.execute(query.check_student_exist_in_gd, (동아리번호, 학번))
            대기결과 = cursor.fetchone()
            if not 대기결과:
                print(f"학번 {학번}은 가입 대기 목록에 없습니다.")
                continue

            결정 = input("승인하려면 'y', 거절하려면 'n'을 입력하세요: ").strip().lower()
            if 결정 == 'y':
                cursor.execute(query.approve_membership, (동아리번호, 학번))
                cursor.execute(query.delete_all_applications, (학번,))
                connection.commit()
                print(f"학번 {학번} 학생이 '{club_name}' 동아리에 가입되었습니다.")
            elif 결정 == 'n':
                cursor.execute(query.delete_applicant, (동아리번호, 학번))
                connection.commit()
                print(f"학번 {학번} 학생의 가입 신청이 거절되었습니다.")
            else:
                print("잘못된 입력입니다. 다시 시도하세요.")

    except ValueError as ve:
        print(f"입력 오류: {ve}")
    except Exception as e:
        connection.rollback()
        print(f"가입 관리 중 오류가 발생했습니다: {e}")