DROP TABLE IF EXISTS ta;
DROP TABLE IF EXISTS instructor;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS survey;

CREATE TABLE ta (
    cuid TEXT PRIMARY KEY NOT NULL,
    lastname TEXT NOT NULL,
    firstname TEXT NOT NULL,
    current_course TEXT,
    email TEXT NOT NULL
);

CREATE TABLE instructor (
    faculty_id TEXT PRIMARY KEY NOT NULL,
    lastname TEXT NOT NULL,
    firstname TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE course (
    cct TEXT PRIMARY KEY NOT NULL,
    course_code TEXT NOT NULL,
    term TEXT NOT NULL,
    num_tas INTEGER,
    instructor1_id TEXT NOT NULL,
    instructor2_id TEXT,
    ta01_id TEXT,
    ta02_id TEXT,
    ta03_id TEXT,
    ta04_id TEXT,
    ta05_id TEXT
);

CREATE TABLE survey (
    ta_cct_index TEXT PRIMARY KEY NOT NULL,
    ta_cuid TEXT NOT NULL,
    cct TEXT NOT NULL,
    semester_index INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    topic_1 TEXT,
    response_1 INTEGER,
    topic_2 TEXT,
    response_2 INTEGER,
    topic_3 TEXT,
    response_3 INTEGER,
    performance_rating INTEGER,
    comment TEXT
);