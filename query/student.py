student_login = '''
SELECT 이름 
FROM 학생 
WHERE 학번 = %s AND 비밀번호 = %s;
'''