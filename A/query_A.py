import sqlite3
#db connect
db = sqlite3.connect('DB_A.sqlite')
cursor = db.cursor()

sql = '''
select age, infection_case, state, count(*)
from (select patient_id, count(distinct city) as countCity
	  from PatientRoute
	  GROUP BY patient_id
	) as FilteredPatientRoute LEFT JOIN PatientInfo
WHERE FilteredPatientRoute.patient_id = PatientInfo.patient_id and countCity > 1
GROUP BY age, infection_case, state
'''

cursor.execute(sql)
tuples = cursor.fetchall()
ageDict = {
    "0s": {},
    "10s": {},
    "20s": {},
    "30s": {},
    "40s": {},
    "50s": {},
    "60s": {},
    "70s": {},
    "80s": {},
    "90s": {},
    "100s": {},
    "None": {},
}
#index: isolated 0 released 1 deceased 2
for tuple in tuples:
    age = tuple[0]
    place = tuple[1]
    state = tuple[2]
    value = tuple[3]
    if state == 'isolated':
        index = 0
    elif state == 'released':
        index = 1
    elif state == 'deceased':
        index = 2
    else:
        pass
    if place in ageDict[age]:
        ageDict[age][place][index] += value
    else:
        ageDict[age][place] = [0, 0, 0]
        ageDict[age][place][index] += value
print(ageDict)
ages = ageDict.keys()
for age in ages:
    places = ageDict[age].keys()
    for place in places:
        val = ageDict[age][place]
        tot = val[0] + val[1] + val[2]
        print(age, place, str(int(val[0] / tot * 100)) + '%', str(int(val[1] / tot * 100)) + '%', str(int(val[2] / tot * 100)) + '%')

cursor.close()
db.commit()
db.close()