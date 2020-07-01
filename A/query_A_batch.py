import sqlite3
import time
import timeit
#db connect
db = sqlite3.connect('DB_A.sqlite')

sql = '''
select age, infection_case, state, count(*)
from (select patient_id, count(distinct city) as countCity
	  from PatientRoute
	  GROUP BY patient_id
	) as FilteredPatientRoute LEFT JOIN PatientInfo
WHERE FilteredPatientRoute.patient_id = PatientInfo.patient_id and countCity > 1
GROUP BY age, infection_case, state
'''


for row in db.execute(sql):
    print(row)

db.commit()
db.close()