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