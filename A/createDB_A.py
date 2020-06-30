import sqlite3
#db connect
db = sqlite3.connect('DB_A.sqlite')
cursor = db.cursor()
#create table if not exists
cursor.execute('''
    create table if not exists PatientInfo
	(
        patient_id  INTEGER,
        global_num  INTEGER DEFAULT 999999999,
        sex     TEXT DEFAULT 'None',
        birth_year  INTEGER DEFAULT 9999,
        age TEXT DEFAULT 'None',
        country TEXT DEFAULT 'None',
        province TEXT DEFAULT 'None',
        city TEXT DEFAULT 'None',
        disease TEXT DEFAULT 'FALSE',
        infection_case TEXT DEFAULT 'etc',
        infection_order INTEGER DEFAULT 0, 
        infected_by INTEGER,
        contact_number INTEGER DEFAULT 0,
        symptom_onset_date TEXT DEFAULT '9999-12-31',
        confirmed_date TEXT DEFAULT '9999-12-31',
        released_date TEXT DEFAULT '9999-12-31',
        deceased_date TEXT DEFAULT '9999-12-31',
        state TEXT DEFAULT 'NONE',
        PRIMARY KEY (patient_id),
        FOREIGN KEY (infected_by) REFERENCES PatientInfo(patient_id)
	);
''')
cursor.execute('''
    create table if not exists PatientRoute
    (
        patient_id  INTEGER,
        global_num  INTEGER DEFAULT 999999999,
        date TEXT DEFAULT '9999-12-31',
        province TEXT DEFAULT 'None',
        city TEXT DEFAULT 'None',
        type TEXT DEFAULT 'None',
        latitude REAL DEFAULT 0,
        longitude REAL DEFAULT 0,
        FOREIGN KEY (patient_id) REFERENCES PatientInfo(patient_id)
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
    attribute = rows[0]
    print(attribute)
    del rows[0]
    for index in range(len((attribute.split(',')))):
        if index == 0:
            question = '?'
        else:
            question += ', ?'
    query = 'insert into ' + tableName + ' values (' + question + ');'

    for row in rows:
        try:
            data = tuple(row.split(','))
            newdata = tuple(None if x == '' else x for x in data)
            cursor.execute(query, newdata)
        except:
            print("error has occured at", row)
    f.close()

cursor.close()
db.commit()
db.close()