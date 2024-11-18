# 학부 번호 검색
find_department = """
SELECT 학부번호 
FROM 학부 
WHERE 학부명 = %s;
"""

# 동아리 번호 검색
find_club = """
SELECT 동아리번호 
FROM 동아리 
WHERE 명칭 = %s;
"""

# 학생 추가
insert_student = """
INSERT INTO 학생 (학번, 이름, 연락처, 생일, 비밀번호, 소속학부번호, 소속동아리번호, 가입일)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
"""

# 회장이 아닌 학생 검색
find_student_without_president = '''
SELECT 학번 
FROM 학생 
WHERE 학번 = %s
  AND 학번 NOT IN (
      SELECT 회장학번 
      FROM 동아리
      WHERE 회장학번 IS NOT NULL
);
'''

# 지도하는 동아리가 없는 교수 검색
find_professor_without_supervise= '''
SELECT 교번 
FROM 교수 
WHERE 교번 = %s
  AND 교번 NOT IN (
      SELECT 지도교수교번 
      FROM 동아리
      WHERE 지도교수교번 IS NOT NULL
);
'''

# 동아리 추가
new_club = """
INSERT INTO 동아리 (동아리번호, 명칭, 회장학번, 지도교수교번, 소속학부번호)
VALUES (%s, %s, %s, %s, %s);
"""