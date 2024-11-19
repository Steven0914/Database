# 회장 로그인
president_login = """
SELECT d.명칭, s.이름
FROM 동아리 d
JOIN 학생 s ON d.회장학번 = s.학번
WHERE s.학번 = %s AND s.비밀번호 = %s;
"""

# 동아리 정보 조회
get_club_info = """
SELECT 명칭
FROM 동아리
WHERE 명칭 = %s;
"""

# 동아리 이름 변경
update_club_name = """
UPDATE 동아리
SET 명칭 = %s
WHERE 명칭 = %s;
"""