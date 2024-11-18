# 학부 번호 검색
find_department = """
SELECT 학부번호 FROM 학부 WHERE 학부명 = %s;
"""

# 동아리 번호 검색
find_club = """
SELECT 동아리번호 FROM 동아리 WHERE 명칭 = %s;
"""

# 학생 추가
insert_student = """
INSERT INTO 학생 (학번, 이름, 연락처, 생일, 비밀번호, 소속학부번호, 소속동아리번호, 가입일)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
"""