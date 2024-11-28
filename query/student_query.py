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


# 소속된 동아리의 참여 가능한 활동 리스트 조회
get_available_activities = """
SELECT a.활동번호, a.활동명, a.날짜, a.활동시간, COUNT(ap.학번) AS 참여인원
FROM 활동 a
LEFT JOIN 활동참여 ap ON a.활동번호 = ap.활동번호
WHERE a.날짜 > CURDATE()
  AND a.주관동아리번호 = %s
GROUP BY a.활동번호
HAVING 참여인원 < 20
ORDER BY a.날짜 ASC;
"""

# 학생의 소속 동아리 확인
get_student_club = """
SELECT 소속동아리번호
FROM 학생
WHERE 학번 = %s;
"""

# 활동 참여 여부 확인
check_activity_participation = """
SELECT 학번
FROM 활동참여
WHERE 활동번호 = %s AND 학번 = %s;
"""

# 활동 참여 등록
add_activity_participation = """
INSERT INTO 활동참여 (활동번호, 학번)
VALUES (%s, %s);
"""


# 참여 중인 활동 조회
get_participated_activities = """
SELECT a.활동번호, a.활동명, a.날짜, a.활동시간
FROM 활동참여 ap, 활동 a
WHERE ap.학번 = %s AND ap.활동번호 = a.활동번호;
"""

# 활동 내용 추가
add_activity_content = """
INSERT INTO 활동내용 (활동번호, 내용)
VALUES (%s, %s);
"""

# 활동 참여자 정보 조회
get_activity_list = """
SELECT  a.활동번호, a.활동명, a.날짜, a.활동시간,
        GROUP_CONCAT(DISTINCT ac.내용 SEPARATOR '\n') AS 활동내용,
        j.주소, j.장소유형, COUNT(DISTINCT ap.학번) AS 참여학생수
FROM 활동참여 ap
JOIN 활동 a ON ap.활동번호 = a.활동번호
LEFT JOIN 활동내용 ac ON a.활동번호 = ac.활동번호
LEFT JOIN 활동장소 j ON a.활동번호 = j.활동번호
WHERE ap.학번 = %s
GROUP BY a.활동번호, a.활동명, a.날짜, a.활동시간, j.주소, j.장소유형
ORDER BY a.날짜 ASC;
"""


# 학생 정보 수정
update_student_info = """
UPDATE 학생
SET 연락처 = %s, 비밀번호 = %s
WHERE 학번 = %s;
"""

# 학생 비밀정보 조회
get_student_info = """
SELECT 연락처, 비밀번호
FROM 학생
WHERE 학번 = %s;
"""

# 학생의 소속 동아리 조회
check_club_exist = """
SELECT c.명칭
FROM 학생 s
JOIN 동아리 c ON s.소속동아리번호 = c.동아리번호
WHERE s.학번 = %s;
"""

# 학생의 동아리 탈퇴
leave_club = """
UPDATE 학생
SET 소속동아리번호 = NULL, 가입일 = NULL
WHERE 학번 = %s;
"""