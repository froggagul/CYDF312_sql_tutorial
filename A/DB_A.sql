create table PatientInfo
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
        FOREIGN KEY (infected_by REFERENCES PatientInfo(patient_id)),
	);

create table PatientRoute
    (
        patient_id  INTEGER,
        global_num  INTEGER DEFAULT 999999999,
        date TEXT DEFAULT '9999-12-31',
        province TEXT DEFAULT 'None',
        city TEXT DEFAULT 'None',
        type TEXT DEFAULT 'None',
        latitude REAL DEFAULT 0,
        longitude REAL DEFAULT 0,
        FOREIGN KEY (patient_id REFERENCES PatientInfo(patient_id)),
    );