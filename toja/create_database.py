import sqlite3
import datetime
from typing import Union


def create_toja_database(cursor: sqlite3.Cursor) -> None:
    # Create the user table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            total_points INTEGER DEFAULT 0
        )
    ''')

    # Create the job table
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
            FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE ON UPDATE CASCADE
        )
    ''')

    # Create the event table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS event (
            event_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE,
            time DATE,
            note TEXT,
            status_id INTEGER NOT NULL,
            contact_id INTEGER,
            job_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (job_id) REFERENCES job(job_id) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (status_id) REFERENCES status(status_id) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (contact_id) REFERENCES contact(contact_id) ON DELETE CASCADE ON UPDATE CASCADE
        )
    ''')

    # Create the status table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS status (
            status_id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT,
            points INTEGER
        )
    ''')

    # Create the contact table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contact (
            contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone TEXT,
            position TEXT,
            job_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (job_id) REFERENCES job(job_id) ON DELETE CASCADE ON UPDATE CASCADE
            FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE ON UPDATE CASCADE
        )
    ''')


def add_user(cursor: sqlite3.Cursor, conn: sqlite3.connect, name: str, points: int) -> None:
    query = '''
    INSERT INTO user(
    first_name,
    total_points
    )
    VALUES (?,?)
    '''
    insert = (name, points)
    cursor.execute(query, insert)
    conn.commit()


def add_job(cursor: sqlite3.Cursor, conn: sqlite3.connect, position: str, company: str, website: str, location: str,
            commitment: str, work_type: str, salary_top: int, salary_bottom: int,
            salary_type: str,
            resume_version: float, job_description_file: str, user_id: int) -> None:
    query = '''
    INSERT INTO job(
        position,
        company,
        website,
        location,
        commitment,
        work_type,
        salary_top,
        salary_bottom,
        salary_type,
        resume_version,
        job_description_file,
        user_id
        )
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
    '''
    insert = (position, company, website, location, commitment, work_type, salary_top, salary_bottom, salary_type,
              resume_version, job_description_file, user_id)
    cursor.execute(query, insert)
    conn.commit()


def add_event(cursor: sqlite3.Cursor, conn: sqlite3.connect, date: str, time: str,
              note: Union[str, None],
              status_id: int, contact_id: Union[int, None], job_id: int, user_id: int) -> None:
    query = '''
    INSERT INTO event(
        date,
        time,
        note,
        status_id,
        contact_id,
        job_id,
        user_id
        )
    VALUES (?,?,?,?,?,?,?)
    '''
    insert = (date, time, note, status_id, contact_id, job_id, user_id)
    cursor.execute(query, insert)
    conn.commit()


def date_change(unit: int, day=False, hour=False, add=False) -> str:
    """Change day or hour by unit. default subtract, add=True to add unit time.
    Used to insert relevant datetime values into new sample database"""
    previous_time = None
    current_time = datetime.datetime.now()
    if day:
        day_change = datetime.timedelta(days=unit)
        if add:
            previous_time = (current_time + day_change).strftime('%Y-%m-%d')
        else:
            previous_time = (current_time - day_change).strftime('%Y-%m-%d')
    if hour:
        day_change = datetime.timedelta(hours=unit)
        if add:
            previous_time = (current_time + day_change).strftime('%I:%M%p')
        else:
            previous_time = (current_time - day_change).strftime('%I:%M%p')

    return previous_time


def add_contact(cursor: sqlite3.Cursor, conn: sqlite3.connect, first_name: str, last_name: str, email: str, phone: str,
                position: str, job_id: int, user_id: int) -> None:
    query = '''
    INSERT INTO contact(
        first_name,
        last_name,
        email,
        phone,
        position,
        job_id,
        user_id
        )
    VALUES (?,?,?,?,?,?,?)
    '''
    insert = (first_name, last_name, email, phone, position, job_id, user_id)
    cursor.execute(query, insert)
    conn.commit()


def add_status(cursor: sqlite3.Cursor, conn: sqlite3.connect, status: str, points: int) -> None:
    query = '''
    INSERT INTO status(
    status,
    points
    )
    VALUES (?,?)
    '''
    insert = (status, points)
    cursor.execute(query, insert)
    conn.commit()


def add_sample_data(cursor: sqlite3.Cursor, conn: sqlite3.connect):
    add_user(cursor, conn, "brendan", 0)

    add_job(cursor, conn, "Software Engineer", "Tech Innovators", "www.techinnovators.com", "San Francisco",
            "Full-time", "Engineering", 120000, 95000, "Annual", 2, "software_engineer_description.txt", 1),
    add_job(cursor, conn, "Data Analyst", "Data Insights Inc.", "www.datainsights.com", "New York", "Part-time",
            "Data Science", 90000, 70000, "Annual", 1, "data_analyst_description.txt", 1),
    add_job(cursor, conn, "Web Developer", "Web Solutions Ltd.", "www.websolutions.com", "London", "Full-time",
            "Development", 110000, 85000, "Annual", 1, "web_developer_description.txt", 1),
    add_job(cursor, conn, "UX Designer", "UserXperience Labs", "www.uxlabs.com", "Seattle", "Full-time", "Design",
            100000, 80000, "Annual", 2, "ux_designer_description.txt", 1),
    add_job(cursor, conn, "DevOps Engineer", "Cloud Innovations", "www.cloudinnovations.com", "Austin", "Full-time",
            "Engineering", 130000, 100000, "Annual", 1, "devops_engineer_description.txt", 1)

    add_event(cursor, conn, date_change(1, day=True), date_change(1, hour=True),  None, 1, 1, 1, 1)
    add_event(cursor, conn, date_change(3, day=True), date_change(5, hour=True),  None, 2, 2, 2, 1)
    add_event(cursor, conn, date_change(4, day=True), date_change(3, hour=True),  None, 3, 3, 3, 1)
    add_event(cursor, conn, date_change(5, day=True, add=True), date_change(1, hour=True), None, 4, 4, 4,
              1)

    add_contact(cursor, conn, "John", "Smith", "john.smith@example.com", "123-456-7890", "Hiring Manager", 1, 1)
    add_contact(cursor, conn, "Jane", "Doe", "jane.doe@example.com", "987-654-3210", "Recruitment Lead", 2, 1)
    add_contact(cursor, conn, "Michael", "Johnson", "michael.johnson@example.com", "555-123-4567", "Talent Acquisition",
                3, 1)
    add_contact(cursor, conn, "Sarah", "Williams", "sarah.williams@example.com", "222-333-4444", "HR Manager", 4, 1)
    add_contact(cursor, conn, "David", "Brown", "david.brown@example.com", "111-222-3333", "Head of HR", 4, 1)
    add_status(cursor, conn, "prospect", 1)
    add_status(cursor, conn, "applied", 2)
    add_status(cursor, conn, "submit_form", 3)
    add_status(cursor, conn, "interview", 10)
    add_status(cursor, conn, "offer", 50)
    add_status(cursor, conn, "offer_accepted", 50)
    add_status(cursor, conn, "meeting", 50)


