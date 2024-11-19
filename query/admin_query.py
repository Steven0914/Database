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
INSERT INTO 학생 (이름, 연락처, 생일, 비밀번호, 소속학부번호, 소속동아리번호, 가입일)
VALUES (%s, %s, %s, %s, %s, %s, %s);
"""

# 회장이 아닌 학생 검색
find_student_without_president = """
SELECT 학번 
FROM 학생 
WHERE 학번 = %s
  AND 소속동아리번호 IS NULL
  AND 학번 NOT IN (
      SELECT 회장학번 
      FROM 동아리
      WHERE 회장학번 IS NOT NULL
  );
"""

# 지도하는 동아리가 없는 교수 검색
find_professor_without_supervise= """
SELECT 교번 
FROM 교수 
WHERE 교번 = %s
  AND 교번 NOT IN (
      SELECT 지도교수교번 
      FROM 동아리
      WHERE 지도교수교번 IS NOT NULL
);
"""

# 동아리 추가 및 회장의 동아리 가입
new_club = """
INSERT INTO 동아리 (명칭, 회장학번, 지도교수교번, 소속학부번호)
VALUES (%s, %s, %s, %s);
"""

# 학생의 소속 동아리 변경
change_club = """
UPDATE 학생
SET 소속동아리번호 = %s,
    가입일 = CURDATE()
WHERE 학번 = %s;
"""
# 동아리 이름으로 검색
find_club_by_name = """
SELECT 동아리번호 
FROM 동아리 
WHERE 명칭 = %s;
"""


# 지도교수 변경
update_supervisor = """
UPDATE 동아리
SET 지도교수교번 = %s
WHERE 동아리번호 = %s;
"""

# 동아리 정보 조회
get_club_info = """
SELECT  d.동아리번호, d.명칭, 
        s1.이름 AS 회장이름,
        p.이름 AS 지도교수이름,
        COUNT(DISTINCT s2.학번) AS 회원수,
        COUNT(DISTINCT a.활동번호) AS 활동수
FROM 동아리 d
LEFT JOIN 학생 s1 ON d.회장학번 = s1.학번
LEFT JOIN 교수 p ON d.지도교수교번 = p.교번
LEFT JOIN 학생 s2 ON d.동아리번호 = s2.소속동아리번호
LEFT JOIN 활동 a ON d.동아리번호 = a.주관동아리번호
GROUP BY d.동아리번호, d.명칭, s1.이름, p.이름
ORDER BY d.명칭;
"""

# 학생이 어떤 동아리에 속해있는지 여부 확인
check_student_in_club = """
SELECT 학번 
FROM 학생
WHERE 학번 = %s AND 소속동아리번호 = %s;
"""

# 회장 변경
update_president = """
UPDATE 동아리
SET 회장학번 = %s
WHERE 동아리번호 = %s;
"""

# 교수 존재 여부 확인
check_professor = """
SELECT 교번 
FROM 교수 
WHERE 이메일 = %s;
"""

# 교수 추가
insert_professor = """
INSERT INTO 교수 (이름, 이메일, 임용일, 소속학부번호)
VALUES (%s, %s, %s, %s);
"""

# 교수 연구분야 추가
insert_research_area = """
INSERT INTO 교수연구분야 (교번, 연구분야)
VALUES (%s, %s);
"""

# 학생 리스트 조회
get_student_list = """
SELECT s.학번, s.이름, h.학부명, d.명칭 AS 소속동아리명, s.가입일
FROM 학생 s
JOIN 학부 h ON s.소속학부번호 = h.학부번호
LEFT JOIN 동아리 d ON s.소속동아리번호 = d.동아리번호
ORDER BY s.학번;
"""

# 교수 리스트 조회
get_professor_list = """
SELECT p.교번, p.이름, h.학부명, p.이메일, 
       p.임용일, GROUP_CONCAT(r.연구분야 SEPARATOR ', ') AS 연구분야
FROM 교수 p
JOIN 학부 h ON p.소속학부번호 = h.학부번호
LEFT JOIN 교수연구분야 r ON p.교번 = r.교번
GROUP BY p.교번, p.이름, h.학부명, p.이메일, p.임용일
ORDER BY p.교번;
"""