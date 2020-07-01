import sqlite3

def printState(age, place, a, b, c):
    tot = a + b + c
    print(age, place, str(int(a / tot * 100)) + '%', str(int(b / tot * 100)) + '%', str(int(c / tot * 100)) + '%')

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
#init value
#index: isolated 0 released 1 deceased 2
prevAge = tuples[0][0]
prevPlace = tuples[0][1]
states = [0, 0, 0]

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
    if prevAge != age or prevPlace != place:
        printState(prevAge, prevPlace, states[0], states[1], states[2])
        states = [0, 0, 0]
        prevAge = age
        prevPlace = place
    states[index] = value
printState(prevAge, prevPlace, states[0], states[1], states[2]) # last value

cursor.close()
db.commit()
db.close()