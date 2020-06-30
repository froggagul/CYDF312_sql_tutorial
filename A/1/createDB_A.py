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