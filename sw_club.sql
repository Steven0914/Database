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
                    학번 INT AUTO_INCREMENT PRIMARY KEY,
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
                    학부번호 INT AUTO_INCREMENT PRIMARY KEY,
                    학부명 VARCHAR(100) NOT NULL
);

CREATE TABLE 교수 (
                    교번 INT AUTO_INCREMENT PRIMARY KEY,
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
                     동아리번호 INT AUTO_INCREMENT PRIMARY KEY,
                     명칭 VARCHAR(100) NOT NULL UNIQUE,
                     회장학번 INT,
                     지도교수교번 INT,
                     소속학부번호 INT NOT NULL,
                     FOREIGN KEY (회장학번) REFERENCES 학생(학번),
                     FOREIGN KEY (지도교수교번) REFERENCES 교수(교번),
                     FOREIGN KEY (소속학부번호) REFERENCES 학부(학부번호)
);

CREATE TABLE 활동 (
                    활동번호 INT AUTO_INCREMENT PRIMARY KEY,
                    활동명 VARCHAR(100) NOT NULL,
                    날짜 DATE,
                    활동시간 INT,
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


INSERT INTO 학부 (학부번호, 학부명) VALUES
                               (1, '소프트웨어학부'),
                               (2, '컴퓨터공학부'),
                               (3, '전자공학부');

INSERT INTO 교수 (교번, 이름, 이메일, 임용일, 소속학부번호) VALUES
                                              (2001, '이건명', 'kmlee@cbnu.ac.kr', '2003-03-01', 1),
                                              (2002, '홍장의', 'jehong@chungbuk.ac.kr', '2005-05-15', 1),
                                              (2003, '최경주', 'kjcheoi@chungbuk.ac.kr', '2006-08-20', 1),
                                              (2004, '류관희', 'khyoo@chungbuk.ac.kr', '2007-09-10', 1),
                                              (2005, '이재성', 'jasonlee@cbnu.ac.kr', '2009-11-25', 1),
                                              (2006, '이종연', 'jongyun@chungbuk.ac.kr', '2010-01-30', 1),
                                              (2007, '아지즈', 'aziz@chungbuk.ac.kr', '2013-04-18', 1),
                                              (2008, '조오현', 'ohyunjo@cbnu.ac.kr', '2015-06-22', 1),
                                              (2009, '노서영', 'rsyoung@cbnu.ac.kr', '2017-07-05', 1),
                                              (2010, '조희승', 'heesn@chungbuk.ac.kr', '2019-09-14', 1),
                                              (2011, '이의종', 'kongjjagae@chungbuk.ac.kr', '2021-10-19', 1),
                                              (2012, '정지훈', 'jh.jeong@chungbuk.ac.kr', '2022-03-01', 1),
                                              (2013, '홍신', 'hongshin@chungbuk.ac.kr', '2024-03-01', 1),
                                              (2014, '강윤석', 'dyskang@cbnu.ac.kr', '2024-09-01', 1),
                                              (3001, '서영훈', 'yhseo@chungbuk.ac.kr', '2010-03-01', 2),
                                              (3002, '김미혜', 'mhkim@chungbuk.ac.kr', '2012-05-15', 2),
                                              (3003, '김성진', 'ksj@chungbuk.ac.kr', '2013-08-20', 2),
                                              (3004, '박수창', 'cewinter@cbnu.ac.kr', '2015-09-10', 2),
                                              (3005, '조겨리', 'kyurijo@chungbuk.ac.kr', '2016-11-25', 2),
                                              (3006, '김봉재', 'bjkim@chungbuk.ac.kr', '2018-01-30', 2),
                                              (3007, '정영섭', 'ysjay@chungbuk.ac.kr', '2019-04-18', 2),
                                              (4001, '서보석', 'boseok@cbnu.ac.kr', '2010-06-15', 3),
                                              (4002, '서재원', 'sjwon@chungbuk.ac.kr', '2011-07-20', 3),
                                              (4003, '김형원', 'hwkim@chungbuk.ac.kr', '2013-09-10', 3),
                                              (4004, '김승구', 'kimsk@chungbuk.ac.kr', '2015-11-25', 3),
                                              (4005, '심상훈', 'shsim@cbnu.ac.kr', '2016-01-30', 3),
                                              (4006, '반유석', 'ban@cbnu.ac.kr', '2018-04-18', 3),
                                              (4007, '손표웅', 'unknown@cbnu.ac.kr', '2019-06-22', 3);


INSERT INTO 교수연구분야 (교번, 연구분야) VALUES
                                  (2001, '인공지능'),
                                  (2002, '소프트웨어공학'),
                                  (2003, '영상처리'),
                                  (2004, '컴퓨터 그래픽스'),
                                  (2004, '콘텐츠'),
                                  (2005, '자연언어처리'),
                                  (2005, '정보검색'),
                                  (2006, '데이터베이스'),
                                  (2007, 'Data Analytics'),
                                  (2008, '컴퓨터네트워크'),
                                  (2009, '데이터 컴퓨팅'),
                                  (2010, '시스템 소프트웨어'),
                                  (2011, '자가-적응 소프트웨어'),
                                  (2012, '기계 지능'),
                                  (2013, '소프트웨어 분석'),
                                  (2013, '검증'),
                                  (2014, '데이터 마이닝'),
                                  (2014, '그래프 머신러닝'),
                                  (3001, '자연언어처리'),
                                  (3002, '유비쿼터스'),
                                  (3002, '게임'),
                                  (3003, '컴퓨터아키텍쳐'),
                                  (3004, '컴퓨터 통신'),
                                  (3004, '멀티미디어 시스템'),
                                  (3005, '생물정보학'),
                                  (3005, '머신러닝'),
                                  (3006, '시스템소프트웨어'),
                                  (3006, '임베디드 시스템'),
                                  (3006, '모바일 시스템'),
                                  (3007, '데이터마이닝'),
                                  (3007, '인공지능'),
                                  (4001, '디지털통신'),
                                  (4001, '군통신'),
                                  (4001, '통신신호처리'),
                                  (4002, '영상처리'),
                                  (4002, '동영상 표준화'),
                                  (4003, '통신칩설계'),
                                  (4003, 'USN 연구'),
                                  (4003, '디지털 및 아날로그 혼성신호 집적회로 설계'),
                                  (4003, 'SoC 설계'),
                                  (4003, '임베디드 시스템 연구'),
                                  (4004, '무선 네트워크'),
                                  (4004, '임베디드 시스템'),
                                  (4005, '초고주파 집적회로'),
                                  (4005, '시스템'),
                                  (4006, '기계학습'),
                                  (4006, '인공지능'),
                                  (4007, '연구분야 미정');


INSERT INTO 학생 (학번, 이름, 연락처, 생일, 비밀번호, 소속학부번호, 소속동아리번호, 가입일) VALUES
                                                                 (2020039001, '조민우', '010-1234-0001', '2000-01-01', 'password1', 1, 1, '2020-03-15'),
                                                                 (2020039002, '황재찬', '010-1234-0002', '2000-02-02', 'password2', 1, 2, '2020-03-20'),
                                                                 (2020039003, '오승주', '010-1234-0003', '2000-03-03', 'password3', 1, 3, '2020-03-25'),
                                                                 (2020039004, '박준유', '010-1234-0004', '2000-04-04', 'password4', 1, 4, '2020-04-01'),
                                                                 (2020039005, '정한울', '010-1234-0005', '2000-05-05', 'password5', 1, 5, '2020-04-05'),
                                                                 (2020039006, '이우영', '010-1234-0006', '2000-06-06', 'password6', 1, 6, '2020-04-10'),
                                                                 (2020039007, '최가은', '010-1234-0007', '2000-07-07', 'password7', 1, 7, '2020-04-15'),
                                                                 (2020039008, '김철수', '010-1234-0008', '2000-08-08', 'password8', 1, NULL, NULL),
                                                                 (2020039009, '이영희', '010-1234-0009', '2000-09-09', 'password9', 1, NULL, NULL),
                                                                 (2020040001, '박민수', '010-1234-0010', '2000-10-10', 'password10', 2, NULL, NULL),
                                                                 (2020040002, '최지우', '010-1234-0011', '2000-11-11', 'password11', 2, NULL, NULL),
                                                                 (2020041001, '정호석', '010-1234-0012', '2000-12-12', 'password12', 3, NULL, NULL),
                                                                 (2020041002, '강다니엘', '010-1234-0013', '2001-01-13', 'password13', 3, NULL, NULL),
                                                                 (2020039010, '김지수', '010-1234-0014', '2001-02-14', 'password14', 1, NULL, NULL),
                                                                 (2020039011, '박지민', '010-1234-0015', '2001-03-15', 'password15', 1, NULL, NULL),
                                                                 (2020040003, '이수민', '010-1234-0016', '2001-04-16', 'password16', 2, NULL, NULL),
                                                                 (2020040004, '김유나', '010-1234-0017', '2001-05-17', 'password17', 2, NULL, NULL),
                                                                 (2020041003, '최민호', '010-1234-0018', '2001-06-18', 'password18', 3, NULL, NULL),
                                                                 (2020041004, '장원영', '010-1234-0019', '2001-07-19', 'password19', 3, NULL, NULL),
                                                                 (2020039012, '한지민', '010-1234-0020', '2001-08-20', 'password20', 1, NULL, NULL),
                                                                 (2020039013, '서강준', '010-1234-0021', '2001-09-21', 'password21', 1, NULL, NULL),
                                                                 (2020040005, '신민아', '010-1234-0022', '2001-10-22', 'password22', 2, NULL, NULL),
                                                                 (2020040006, '유아인', '010-1234-0023', '2001-11-23', 'password23', 2, NULL, NULL),
                                                                 (2020041005, '김고은', '010-1234-0024', '2001-12-24', 'password24', 3, NULL, NULL),
                                                                 (2020041006, '박보검', '010-1234-0025', '2002-01-25', 'password25', 3, NULL, NULL),
                                                                 (2020039014, '전지현', '010-1234-0026', '2002-02-26', 'password26', 1, NULL, NULL),
                                                                 (2020039015, '이동욱', '010-1234-0027', '2002-03-27', 'password27', 1, NULL, NULL),
                                                                 (2020040007, '수지', '010-1234-0028', '2002-04-28', 'password28', 2, NULL, NULL),
                                                                 (2020040008, '송중기', '010-1234-0029', '2002-05-29', 'password29', 2, NULL, NULL),
                                                                 (2020041007, '아이유', '010-1234-0030', '2002-06-30', 'password30', 3, NULL, NULL);

INSERT INTO 동아리 (동아리번호, 명칭, 회장학번, 지도교수교번, 소속학부번호) VALUES
                                                      (1, '턱스', 2020039001, 2009, 1),
                                                      (2, '엠시스', 2020039002, 2008, 1),
                                                      (3, '샘마루', 2020039003, 2007, 1),
                                                      (4, '큐빅', 2020039004, 2005, 1),
                                                      (5, '네스트넷', 2020039005, 2001, 1),
                                                      (6, 'PDA', 2020039006, 2002, 1),
                                                      (7, '노바', 2020039007, 2003, 1);

SET FOREIGN_KEY_CHECKS = 1;