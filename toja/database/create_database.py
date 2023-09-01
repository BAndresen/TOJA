import sqlite3


def create_toja_database(cursor: sqlite3.Cursor, conn: sqlite3.connect) -> None:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            total_points INTEGER DEFAULT 0
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS job (
            job_id INTEGER PRIMARY KEY AUTOINCREMENT,
            position TEXT,
            company TEXT,
            website TEXT,
            location TEXT,
            commitment TEXT,
            work_type TEXT,
            salary_top TEXT,
            salary_bottom TEXT,
            salary_type TEXT,
            resume_version TEXT,
            job_description_file TEXT,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES database(user_id) ON DELETE CASCADE ON UPDATE CASCADE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS event (
            event_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE,
            time DATE,
            note TEXT,
            status_id INTEGER NOT NULL,
            contact_id INTEGER,
            job_id INTEGER DEFAULT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (job_id) REFERENCES job(job_id) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (user_id) REFERENCES database(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (status_id) REFERENCES status(status_id) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (contact_id) REFERENCES contact(contact_id) ON DELETE CASCADE ON UPDATE CASCADE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS status (
            status_id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT,
            points INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contact (
            contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone TEXT,
            position TEXT,
            job_id INTEGER,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (job_id) REFERENCES job(job_id) ON DELETE CASCADE ON UPDATE CASCADE
            FOREIGN KEY (user_id) REFERENCES database(user_id) ON DELETE CASCADE ON UPDATE CASCADE
        )
    ''')

    insert_queries = [
        "INSERT INTO status(status, points) VALUES('rejected', 1);",
        "INSERT INTO status(status, points) VALUES('prospect', 1);",
        "INSERT INTO status(status, points) VALUES('follow_up', 2);",
        "INSERT INTO status(status, points) VALUES('applied', 3);",
        "INSERT INTO status(status, points) VALUES('meeting', 5);",
        "INSERT INTO status(status, points) VALUES('attend_event', 15);",
        "INSERT INTO status(status, points) VALUES('interview', 20);",
        "INSERT INTO status(status, points) VALUES('offer', 100);",
        "INSERT INTO status(status, points) VALUES('offer_accepted', 1000);",
    ]

    for query in insert_queries:
        cursor.execute(query)
    conn.commit()

