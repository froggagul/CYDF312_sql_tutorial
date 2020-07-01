import sqlite3
import time
#db connect
db = sqlite3.connect('DB_A.sqlite')
cursor = db.cursor()
sql = '''
with cte
as (
	select age, infection_case, 
		sum(CASE WHEN state = 'isolated' THEN counts ELSE 0 END) AS isolated, 
		sum(CASE WHEN state = 'released' THEN counts ELSE 0 END) AS released,
		sum(CASE WHEN state = 'deceased' THEN counts ELSE 0 END) AS deceased
		from (
			select age, infection_case, state, count(*) as counts
			from(
				select patient_id, count(distinct city) as countCity
				from PatientRoute
				GROUP BY patient_id
				having countCity > 1
			) as FilteredPatientRoute INNER JOIN (
				select patient_id, age, infection_case, state
				from PatientInfo
			) as FilteredPatineInfo
		on FilteredPatientRoute.patient_id = FilteredPatineInfo.patient_id
		group by age, infection_case, state
	)
	GROUP BY age, infection_case
)
select age, infection_case,
 isolated*100.0/(isolated + released + deceased) as isolatedPercentage,
 released*100.0/(isolated + released + deceased) as releasedPercentage,
 deceased*100.0/(isolated + released + deceased) as deceasedPercentage
from cte
'''
count = 2000
start = time.time()
for i in range(count):
    cursor.execute(sql)
    tuples = cursor.fetchall()
    print(tuples)
stop = time.time()
avg = (stop-start) / count
print(round(avg, 6), "seconds")

db.commit()
db.close()