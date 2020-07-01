COVID-19 virus is spread worldwide in 2020. The Korea Centers for Disease Control and Prevention (KCDC) makes daily announcements of confirmed cases, isolates, deaths and recovered persons. ncov.mohw.go.kr

To understand the virus better with data, the DS4C (Data Science for COVID-19) Project has been initiated by Korean students and institutions, which releases updated data every two weeks. Data sets are published in CSV file format, some of which have missing and mismatched data.

Our goal in this Project #2 is to create a database based on the data provided by DS4C and to conduct simple data analysis.

2020년 현재 전 세계적으로 문제가 되는 신종코로나바이러스(COVID-19) 바이러스에 대하여 한국의 질병관리본부(KCDC)에서는 매일 확진자와 격리대상자, 사망자, 회복된 인원에 대한 발표를 웹페이지(http://ncov.mohw.go.kr/)에 공개한다.

이를 국내 대학생 및 기관 들이 힘을 합쳐 ‘DS4C (Data Science for COVID-19) Project’라는 데이터 생성 프로젝트로 각종 신종 코로나바이러스에 관련된 데이터와 정책들을 phasing 하여 데이터 세트를 공개했다. 프로젝트는 2주마다 데이터를 수집하여 공개한다. 데이터 세트는 CSV 파일 포맷으로 공개 돼 있으며 이 중 일부 결측치 및 mismatched 데이터들이 존재한다.

이번 Project#2는 신종 코로나바이러스 데이터 세트를 Database 화하여 데이터의 관계성과 무결성 등을 개선하고 간단한 데이터 분석을 진행하고자 한다.



CSV files
====
* PatientInfo.csv
  - Epidemiological data of COVID-19 patients in South Korea
* PatientRoute.csv
  - Route data of COVID-19 patients in South Korea
* Time.csv
  - Time series data of COVID-19 status in South Korea
* TimeAge.csv
  - Time series data of COVID-19 status in terms of the age in South Korea
* TimeGender.csv
  - Time series data of COVID-19 status in terms of gender in South Korea
* TimeProvince.csv
  - Time series data of COVID-19 status in terms of the Province in South Korea  
Columns info: see csv_information.xlsx



Questions (sqlite DB, Python 사용) 
====

A [50]. PatientInfo.csv, PatientRoute.csv를 활용하여 Dataset을 Sqlite DB로 작성하시오
* [10] csv_information.xlsx에 주어진 constraint (PK = Primary Key, FK = Foreign Key, NN = Not Null, U = Unique, Default =  기본값)를 충족하는 DB schema를 작성하고 csv 파일 데이터를 DB table에 입력하는 python 파일 작성 Table 이름 = csv 파일 이름 (대소문자 유지, 확장자 제외)  
제출: createDB_A.py, (DB_A.sqlite)
* [10] PatientInfo.csv의 birth_year, infected_by, contact_number, age, symptoms_onset_date 컬럼에는 다른 값들과는 범주나 형태가 다른 이상치가 존재한다. 이상치의 경우 데이터 관계성이나 무결성에 문제를 일으킬 수 있다. 해당 컬럼 존재하는 다른 값들과 비교하여 이상치를 알맞게 수정하라 (DB update 포함). 이 부분에 대해 간략히 기술하시오. 고 해당 부분에 대하여 정리하여 가술하시오.
Update query 제출 필요 없음 DB_A.sqlite 의 데이터는 update 함  
제출: 보고서 DB_A_fix.pdf, (DB_A.sqlite)
* [10] PatientInfo.csv에는 state와 birth_year 컬럼을 참조하되 무결성 조건에 어긋나는 값을 가진 컬럼들이 있다.
‘age’에는 누락된 값이 있는 부분이 있다. ‘birth_year’의 값을 참조하여 ‘age’의 데이터를 UPDATE하는 sqlite 쿼리문을 작성하시오.(나이 : 2020 - ‘birth_year’+1, age_group : (age Xs: X+0 ~ X+9, (X : 0,10,20,30,40,50,60,70,80)))  
제출: DB_A_fix2.py, DB_A.sqlite
* [10] PatientRoute.csv에는 확진자의 이동 동선이 나타나 있다. 확진자 중 city를 2지역 이상 이동한 자들을 age그룹에 따른 infection_case별 격리,회복, 사망 비율을 출력하는 python code를 작성하시오 같은 city 은 하나로 count. 예: '구로구 -> 동대문구 -> 구로구' : 2지역  
age그룹에 속하지 않는 나이는 None그룹으로 계산.  
출력 예)  
40s etc 50% 45% 5%,  
40s Coupang 60% 40% 0%,  
40s Church 70% 20% 10%,  
....  
제출: query_A.py
[10] 위 쿼리를 1000 번 실행하여 그 평균 실행 시간을 출력하는 python code를 작성하시오. 쿼리 최적화 및 코드 최적화 필요. 쿼리 결과를 화면에 출력해야 함.
평균 실행시간은 초 단위로 소수점 6째 자리까지 출력 (시간 순서에 따른 차등 점수 부여)  
제출: query_A_batch.py


B. [30]. Time.csv, TimeAge.csv, TimeGender.csv, TimeProvince.csv 를 활용하여 Dataset을 sqlite DB로 작성하시오
* [10] csv_information.xlsx에 주어진 constraint 를 충족하는 DB schema를 작성하고 csv 파일 데이터를 DB table에 입력하는 python 파일 작성 (데이터 수집 방식이 3월 2일부터 변경됨에 따라 평가방식이 변경되었다. DB에서 3월 2일 이전 데이터를 제외하고 작성하시오.)  
제출: createDB_B.py, (DB_B.sqlite)
* [10] 5월 5일의 확진율(confirmed/test)을 구하여 % 단위로 출력하는 python code를 작성하시오.  
제출: query1_B.py
* [10] 3월 3일부터 5월 31일까지 일일 감염율이 전날 대비 가장 확진율이 많이 늘어난 날의 전체의 연령대별(10s~80s) 확진, 사망 비율을 구하는 python code를 작성하시오.  
출력예시  
2020-03-03 0s 5% 0%  
2020-03-03 10s 15% 0%  
2020-03-03 20s 35% 0.1%  
제출: query2_B.py