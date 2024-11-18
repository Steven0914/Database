import query.admin_query as query

def add_student(cursor, connection):
    try:
        학번 = int(input("학번을 입력하세요: "))
        이름 = input("이름을 입력하세요: ")
        연락처 = input("연락처를 입력하세요 (ex. 010-1234-5678): ")
        생일 = input("생일을 입력하세요 (ex.: YYYY-MM-DD): ")
        비밀번호 = input("비밀번호를 입력하세요: ")

        학부명 = input("소속 학부명을 입력하세요: ")
        cursor.execute(query.find_department, (학부명,))
        학부결과 = cursor.fetchone()
        if not 학부결과:
            raise ValueError(f"'{학부명}' 학부를 찾을 수 없습니다.")
        소속학부번호 = 학부결과[0]

        동아리명 = input("소속 동아리명을 입력하세요 (없으면 Enter): ").strip()
        if not 동아리명:
            소속동아리번호 = None
        else:
            cursor.execute(query.find_club, (동아리명,))
            동아리결과 = cursor.fetchone()
            if not 동아리결과:
                raise ValueError(f"'{동아리명}' 동아리를 찾을 수 없습니다.")
            소속동아리번호 = 동아리결과[0]

        가입일 = input("가입일을 입력하세요 (형식: YYYY-MM-DD, 없으면 Enter): ")
        가입일 = 가입일 if 가입일 else None

        cursor.execute(query.insert_student, (학번, 이름, 연락처, 생일, 비밀번호, 소속학부번호, 소속동아리번호, 가입일))
        connection.commit()

        print("학생이 성공적으로 추가되었습니다.")

    except ValueError as ve:
        print(f"입력 오류: {ve}")
    except Exception as e:
        connection.rollback()
        print(f"학생 추가 중 오류가 발생했습니다: {e}")


def add_club(cursor, connection):
    try:
        동아리번호 = int(input("동아리 번호를 입력하세요: "))
        명칭 = input("동아리 명칭을 입력하세요: ")

        회장학번 = int(input("회장의 학번을 입력하세요: "))
        cursor.execute(query.find_student_without_president, (회장학번,))
        회장결과 = cursor.fetchone()
        if not 회장결과:
            raise ValueError(f"학번 {회장학번}에 해당하는 학생을 찾을 수 없거나 이미 회장인 학생입니다.")

        지도교수교번 = int(input("지도 교수의 교번을 입력하세요: "))
        cursor.execute(query.find_professor_without_supervise, (지도교수교번,))
        교수결과 = cursor.fetchone()
        if not 교수결과:
            raise ValueError(f"교번 {지도교수교번}에 해당하는 교수를 찾을 수 없거나 이미 지도하는 동아리가 있습니다.")

        학부명 = input("소속 학부명을 입력하세요: ")
        cursor.execute(query.find_department, (학부명,))
        학부결과 = cursor.fetchone()
        if not 학부결과:
            raise ValueError(f"'{학부명}' 학부를 찾을 수 없습니다.")
        소속학부번호 = 학부결과[0]

        cursor.execute(query.new_club, (동아리번호, 명칭, 회장학번, 지도교수교번, 소속학부번호))
        connection.commit()

        print("동아리가 성공적으로 추가되었습니다.")

    except ValueError as ve:
        print(f"입력 오류: {ve}")
    except Exception as e:
        connection.rollback()
        print(f"동아리 추가 중 오류가 발생했습니다: {e}")

