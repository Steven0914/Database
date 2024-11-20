# 동아리 관리 시스템

## 1. 프로젝트 소개
- 소프트웨어학부의 동아리를 관리하는 시스템입니다.
- 관리자, 동아리 회장, 일반 학생으로 구분되어 각각의 권한을 가집니다.


## 2. 프로젝트 구조
```
- Database Project
  - controller                      # Controller 파일
    - __init__.py
    - admin_controller.py           # 관리자 메뉴
    - menu.py                       # 초기 메뉴
    - president_controller.py       # 동아리 회장 메뉴
    - student_controller.py         # 일반 학생 메뉴
  - database                        # Database 관련 파일
    - __init__.py
    - connect_db.py                 # Database 연결 파일
    - init_db.py                    # Database 초기화 파일
  - query                           # SQL Query문
    - __init__.py
    - admin_query.py
    - president_query.py
    - student_query.py
  - service                         # Controller에서 호출하는 함수들
    - __init__.py
    - admin_service.py
    - president_service.py
    - student_service.py
  - config.py                       # 설정 파일(db, admin PW)
  - main.py                         # 프로그램 실행 파일
  - README.md                       # README 파일
  - sw_club.sql                     # Database 초기화 SQL 파일
```

## 3. 프로젝트 기능
### 1. 관리자


### 2. 동아리 회장


### 3. 일반 학생



## 4. 프로젝트 실행
1. main.py 파일을 실행합니다.
```bash
$ python main.py
```
2. 프로그램 시작시 config에 설정된 이름의 데이터베이스가 자동 생성됩니다.(이때 config db관련 정보가 설정 되어있어야 합니다.)
3. 관리자 모드로 접속하여 1번 기능으로 데이터베이스 초기화를 실행할 수 있습니다. 데이터베이스 초기화란 테이블 생성 및 초기 데이터 삽입을 의미합니다.
4. 그 이후 관리자, 동아리 회장, 일반 학생으로 접속하여 각각의 기능을 사용할 수 있습니다.

## 5. 테이블 구조
1. 학생
- 학번(PK), 이름, 연락처, 생일, 비밀번호, 소속학부번호(FK), 소속동아리번호(FK), 가입일
2. 학부
- 학부번호(PK), 학부명
3. 교수
- 교번(PK), 이름, 이메일, 임용일, 소속학부번호(FK)
4. 교수연구분야
- 교번(FK, PK), 연구분야(PK)
5. 동아리
- 동아리번호(PK), 명칭(UNIQUE), 회장학번(FK), 지도교수교번(FK), 소속학부번호(FK)
6. 활동
- 활동번호(PK), 활동명, 날짜, 활동시간, 주관동아리번호(FK)
7. 활동장소
- 활동번호(PK, FK), 주소, 장소유형
8. 가입대기
- 동아리번호(FK), 학번(FK), (PK = 동아리번호, 학번)
9. 활동참여
- 활동번호(FK), 학번(FK), (PK = 활동번호, 학번)
10.	활동내용
- 활동번호(FK), 내용(PK)