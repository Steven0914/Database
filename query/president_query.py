president_login = """
SELECT d.명칭, s.이름
FROM 동아리 d
JOIN 학생 s ON d.회장학번 = s.학번
WHERE s.학번 = %s AND s.비밀번호 = %s;
"""