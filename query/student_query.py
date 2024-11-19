# 학생 로그인
student_login = """
SELECT 이름, 학번
FROM 학생 
WHERE 학번 = %s AND 비밀번호 = %s;
"""

# 본인 정보 조회(학부 동아리가 NULL일 경우를 위해 LEFT JOIN 사용)
get_info = """
SELECT s.학번, s.이름, d.학부명, c.명칭 AS 소속동아리, s.연락처, s.생일, s.가입일
FROM 학생 s
JOIN 학부 d ON s.소속학부번호 = d.학부번호
LEFT JOIN 동아리 c ON s.소속동아리번호 = c.동아리번호
WHERE s.학번 = %s;
"""

# 동아리 리스트 조회
get_club_list = """
SELECT 
    c.명칭 AS 동아리명,
    s.이름 AS 동아리회장,
    p.이름 AS 지도교수
FROM 
    동아리 c
LEFT JOIN 학생 s ON c.회장학번 = s.학번
LEFT JOIN 교수 p ON c.지도교수교번 = p.교번;
"""

# 동아리 가입 신청
apply_to_club = """
INSERT INTO 가입대기 (동아리번호, 학번)
VALUES (%s, %s);
"""

# 동아리 번호 검색
find_club = """
SELECT 동아리번호 
FROM 동아리 
WHERE 명칭 = %s;
"""