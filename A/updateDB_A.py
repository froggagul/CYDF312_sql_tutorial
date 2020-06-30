import sqlite3
#db connect
db = sqlite3.connect('DB_A.sqlite')
cursor = db.cursor()

sql = '''
update PatientInfo
set birth_year = 9999
where birth_year not like '____'
'''

cursor.execute(sql)
tuples = cursor.fetchall()

for tuple in tuples:
    print(tuple)

cursor.close()
db.commit()
db.close()