import sqlite3
#db connect
db = sqlite3.connect('DB_B.sqlite')
cursor = db.cursor()

sql = '''
with result
as (
    select date, test, confirmed
    from time
    where date = '2020-05-05'
)
select (cast(confirmed as float) * 100 /cast(test as float)) as percentage
from result
'''

cursor.execute(sql)
tuples = cursor.fetchall()

for tuple in tuples:
    print(str(tuple[0]) + '%')

cursor.close()
db.commit()
db.close()