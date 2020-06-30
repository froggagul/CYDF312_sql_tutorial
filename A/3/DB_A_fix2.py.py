import sqlite3
#db connect
db = sqlite3.connect('DB_A.sqlite')
cursor = db.cursor()

sql = '''
update PatientInfo
set age = ((2020 - birth_year + 1)/10 * 10) || 's'
where age != ((2020 - birth_year + 1)/10 * 10) || 's' AND birth_year != 9999 AND age != 'None'
'''

cursor.execute(sql)

cursor.close()
db.commit()
db.close()