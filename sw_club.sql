-- 외래 키 제약 조건 비활성화
SET FOREIGN_KEY_CHECKS = 0;

-- 테이블 삭제
DROP TABLE IF EXISTS 활동내용;
DROP TABLE IF EXISTS 활동참여;
DROP TABLE IF EXISTS 가입대기;
DROP TABLE IF EXISTS 활동장소;
DROP TABLE IF EXISTS 활동;
DROP TABLE IF EXISTS 동아리;
DROP TABLE IF EXISTS 교수연구분야;
DROP TABLE IF EXISTS 교수;
DROP TABLE IF EXISTS 학부;
DROP TABLE IF EXISTS 학생;

-- 테이블 생성
CREATE TABLE 학생 (
                    학번 INT PRIMARY KEY,
                    이름 VARCHAR(50) NOT NULL,
                    연락처 VARCHAR(13) NOT NULL,
                    생일 DATE NOT NULL,
                    비밀번호 VARCHAR(30) NOT NULL,
                    소속학부번호 INT NOT NULL,
                    소속동아리번호 INT,
                    가입일 DATE,
                    FOREIGN KEY (소속학부번호) REFERENCES 학부(학부번호),
                    FOREIGN KEY (소속동아리번호) REFERENCES 동아리(동아리번호)
);

CREATE TABLE 학부 (
                    학부번호 INT PRIMARY KEY,
                    학부명 VARCHAR(100) NOT NULL
);

CREATE TABLE 교수 (
                    교번 INT PRIMARY KEY,
                    이름 VARCHAR(50) NOT NULL,
                    이메일 VARCHAR(100) NOT NULL,
                    임용일 DATE NOT NULL,
                    소속학부번호 INT NOT NULL,
                    FOREIGN KEY (소속학부번호) REFERENCES 학부(학부번호)
);

CREATE TABLE 교수연구분야 (
                        교번 INT,
                        연구분야 VARCHAR(100),
                        PRIMARY KEY (교번, 연구분야),
                        FOREIGN KEY (교번) REFERENCES 교수(교번)
);

CREATE TABLE 동아리 (
                     동아리번호 INT PRIMARY KEY,
                     명칭 VARCHAR(100) NOT NULL,
                     회장학번 INT,
                     지도교수교번 INT,
                     소속학부번호 INT NOT NULL,
                     FOREIGN KEY (회장학번) REFERENCES 학생(학번),
                     FOREIGN KEY (지도교수교번) REFERENCES 교수(교번),
                     FOREIGN KEY (소속학부번호) REFERENCES 학부(학부번호)
);

CREATE TABLE 활동 (
                    활동번호 INT PRIMARY KEY,
                    활동명 VARCHAR(100) NOT NULL,
                    날짜 DATE,
                    활동시간 TIME,
                    주관동아리번호 INT NOT NULL,
                    FOREIGN KEY (주관동아리번호) REFERENCES 동아리(동아리번호)
);

CREATE TABLE 활동장소 (
                      활동번호 INT,
                      주소 VARCHAR(200),
                      장소유형 VARCHAR(50),
                      PRIMARY KEY (활동번호),
                      FOREIGN KEY (활동번호) REFERENCES 활동(활동번호)
);

CREATE TABLE 가입대기 (
                      동아리번호 INT,
                      학번 INT,
                      PRIMARY KEY (동아리번호, 학번),
                      FOREIGN KEY (동아리번호) REFERENCES 동아리(동아리번호),
                      FOREIGN KEY (학번) REFERENCES 학생(학번)
);

CREATE TABLE 활동참여 (
                      활동번호 INT,
                      학번 INT,
                      PRIMARY KEY (활동번호, 학번),
                      FOREIGN KEY (활동번호) REFERENCES 활동(활동번호),
                      FOREIGN KEY (학번) REFERENCES 학생(학번)
);

CREATE TABLE 활동내용 (
                      활동번호 INT,
                      내용 TEXT,
                      PRIMARY KEY (활동번호),
                      FOREIGN KEY (활동번호) REFERENCES 활동(활동번호)
);

-- 외래 키 제약 조건 활성화
SET FOREIGN_KEY_CHECKS = 1;