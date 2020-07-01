import sqlite3
from datetime import timedelta, date

#db connect
db = sqlite3.connect('DB_B.sqlite')
cursor = db.cursor()

sql = '''
    with result
    as (
        select date, test, confirmed
        from time
        where date = ?
    )
    select (cast(confirmed as float) * 100 /cast(test as float)) as percentage
    from result
    '''

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2020, 3, 3)
end_date = date(2020, 5, 31)
maxDate = '2020-03-03'
maxRatio = 0
prevRatio = 0
for single_date in daterange(start_date, end_date):
    d = single_date.strftime("%Y-%m-%d")
    cursor.execute(sql, [d])
    tuples = cursor.fetchall()
    if maxRatio < tuples[0][0] - prevRatio:
        if prevRatio != 0:
            maxDate = d
            maxRatio = tuples[0][0] - prevRatio
    prevRatio = tuples[0][0]
sql = '''
    select age, confirmed, deceased
    from TimeAge
    where date = ?
    '''
cursor.execute(sql, [maxDate])
tuples = cursor.fetchall()
totConfirm = 0
totDeceased = 0
for tuple in tuples:
    totConfirm += tuple[1]
    totDeceased += tuple[2]
for tuple in tuples:
    print(tuple[0] + ' ' +  str(int(tuple[1] * 100 / totConfirm)) + '% ' + str(int(tuple[2] * 100 / totDeceased)) + '%')
cursor.close()
db.commit()
db.close()