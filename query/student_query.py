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