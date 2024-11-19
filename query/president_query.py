# 회장 로그인
president_login = """
SELECT d.명칭, s.이름
FROM 동아리 d
JOIN 학생 s ON d.회장학번 = s.학번
WHERE s.학번 = %s AND s.비밀번호 = %s;
"""


# 동아리 이름 변경
update_club_name = """
UPDATE 동아리
SET 명칭 = %s
WHERE 명칭 = %s;
"""

# 동아리 찾기
get_club_id = """
SELECT 동아리번호
FROM 동아리
WHERE 명칭 = %s;
"""

# 새로운 활동 생성
create_activity = """
INSERT INTO 활동 (활동명, 날짜, 활동시간, 주관동아리번호)
VALUES (%s, %s, %s, %s);
"""