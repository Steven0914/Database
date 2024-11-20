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

#현재 동아리의 가입 대기 중인 학생 조회
get_waiting_students = """
SELECT gd.학번, s.이름
FROM 가입대기 gd
JOIN 학생 s ON gd.학번 = s.학번
WHERE gd.동아리번호 = %s;
"""

# 이미 동아리가 있는지 확인
check_student_exist_in_gd = """
SELECT 학번 
FROM 가입대기 
WHERE 동아리번호 = %s AND 학번 = %s
"""

# 학생 동아리 가입 승인
approve_membership = """
UPDATE 학생
SET 소속동아리번호 = %s, 가입일 = CURDATE()
WHERE 학번 = %s;
"""

# 가입 승인시 해당 학생의 모든 가입 대기 목록 삭제
delete_all_applications = """
DELETE FROM 가입대기
WHERE 학번 = %s;
"""

# 가입 거절시 해당 학생 가입 대기 목록 삭제
delete_applicant = """
DELETE FROM 가입대기
WHERE 동아리번호 = %s AND 학번 = %s;
"""

# 동아리 활동 정보 리스트 조회
get_activity_info_list ="""
SELECT  a.활동번호, a.활동명, a.날짜, a.활동시간,
        GROUP_CONCAT(DISTINCT ac.내용 SEPARATOR '\n ') AS 활동내용,
        j.주소, j.장소유형
FROM 활동 a
LEFT JOIN 활동내용 ac ON a.활동번호 = ac.활동번호
LEFT JOIN 활동장소 j ON a.활동번호 = j.활동번호
WHERE a.주관동아리번호 = %s
GROUP BY a.활동번호
ORDER BY a.날짜 ASC;
"""

# 참여자 조회
get_participants = """
SELECT s.이름 
FROM 활동참여 ap, 학생 s
WHERE ap.활동번호 = %s AND ap.학번 = s.학번;
"""