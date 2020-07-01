import sqlite3
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
    from (select patient_id, count(distinct city) as countCity
	  from PatientRoute
	  GROUP BY patient_id
	) as FilteredPatientRoute LEFT JOIN PatientInfo
	WHERE FilteredPatientRoute.patient_id = PatientInfo.patient_id and countCity > 1
	GROUP BY age, infection_case, state
	)
GROUP BY age, infection_case
)
select age, infection_case,
 isolated*100.0/(isolated + released + deceased) as isolatedPercentage,
 released*100.0/(isolated + released + deceased) as releasedPercentage,
 deceased*100.0/(isolated + released + deceased) as deceasedPercentage
from cte
'''

cursor.execute(sql)
tuples = cursor.fetchall()

for tuple in tuples:
    age = tuple[0]
    place = tuple[1]
    isolatedPercentage = tuple[2]
    releasedPercentage = tuple[3]
    deceasedPercentage = tuple[4]
    print(tuple[0] + ' ' + tuple[1] + ' ' + str(int(tuple[2])) + '% ' + str(int(tuple[3])) + '% ' + str(int(tuple[4])) + '%')

cursor.close()
db.commit()
db.close()