import query.president_query as query

def update_club_name(cursor, connection, club_name):
    try:
        cursor.execute(query.get_club_info, (club_name, ))
        club_info = cursor.fetchone()

        if not club_info:
            print("\n해당 동아리는 존재하지 않거나, 권한이 없습니다.")
            return

        current_name = club_info[0]

        print("\n===== 현재 동아리 정보 =====")
        print(f"동아리 명칭: {current_name}")
        print("===========================")

        new_name = input("새 동아리 명칭 (변경하지 않으려면 Enter): ") or current_name

        if new_name == current_name:
            print("\n변경할 정보가 없어 동아리 정보 변경을 취소합니다.")
            return

        if new_name == "":
            print("\n변경할 정보가 없어 동아리 정보 변경을 취소합니다.")
            return

        cursor.execute(query.update_club_name,(new_name, current_name))
        connection.commit()

        print("\n동아리 정보가 성공적으로 업데이트되었습니다.")

    except Exception as e:
        print(f"\n동아리 정보 변경 중 오류가 발생했습니다: {e}")