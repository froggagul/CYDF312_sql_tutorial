import sqlite3
#db connect
db = sqlite3.connect('DB_B.sqlite')
cursor = db.cursor()
#create table if not exists
cursor.execute('''
    create table if not exists Time
	(
        date Text,
        time    INTEGER DEFAULT 0,
        test    INTEGER DEFAULT 0,
        negative    INTEGER DEFAULT 0,
        confirmed   INTEGER DEFAULT 0,
        released    INTEGER DEFAULT 0,
        deceased    INTEGER DEFAULT 0,
        PRIMARY KEY (date)
	);
''')
cursor.execute('''
    create table if not exists TimeAge
    (
        date Text NOT NULL,
        time    INTEGER DEFAULT 0,
        age     TEXT DEFAULT 'None',
        confirmed   INTEGER DEFAULT 0,
        deceased    INTEGER DEFAULT 0,
        FOREIGN KEY (date) REFERENCES Time(date)
    );
''')
cursor.execute('''
    create table if not exists TimeGender
    (
        date Text NOT NULL,
        time    INTEGER DEFAULT 0,
        sex     TEXT DEFAULT 'None',
        confirmed   INTEGER DEFAULT 0,
        deceased    INTEGER DEFAULT 0,
        FOREIGN KEY (date) REFERENCES Time(date)
    );
''')
cursor.execute('''
    create table if not exists TimeProvince
    (
        date Text NOT NULL,
        time    INTEGER DEFAULT 0,
        province    TEXT DEFAULT 'None',
        confirmed   INTEGER DEFAULT 0,
        released    INTEGER DEFAULT 0,
        deceased    INTEGER DEFAULT 0,
        FOREIGN KEY (date) REFERENCES Time(date)
    );
''')

# insert data
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for table in tables:
    tableName = table[0]
    src = tableName + '.csv'
    f = open(src, 'r')
    rows = [item.strip('\n') for item in f]
    attribute = rows[0].split(',')
    del rows[0]
    # make query and data
    for row in rows:
        tempAttribute = ''
        tempQuestion = ''
        tempData = tuple()
        data = tuple(row.split(','))
        for index in range(len(data)):
            if data[index] != '':
                tempData = tempData + (data[index],)
                if (len(tempQuestion) == 0):
                    tempQuestion = '?'
                else:
                    tempQuestion += ', ?'
                if (len(tempAttribute) == 0):
                    tempAttribute = attribute[index]
                else:
                    tempAttribute += ', ' + attribute[index]
        query = 'insert into ' + tableName + ' (' + tempAttribute + ') values (' + tempQuestion + ');'
        print(query)
        cursor.execute(query, tempData)
    f.close()

cursor.close()
db.commit()
db.close()