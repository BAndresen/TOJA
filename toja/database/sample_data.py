import sqlite3
from typing import Union
import datetime


# def add_user(cursor: sqlite3.Cursor, conn: sqlite3.connect, name: str, points: int) -> None:
#     query = '''
#     INSERT INTO user(
#     name,
#     total_points
#     )
#     VALUES (?,?)
#     '''
#     insert = (name, points)
#     cursor.execute(query, insert)
#     conn.commit()
#
#
# def add_job(cursor: sqlite3.Cursor, conn: sqlite3.connect, position: str, company: str, website: str, location: str,
#             commitment: str, work_type: str, salary_top: int, salary_bottom: int,
#             salary_type: str,
#             resume_version: float, job_description_file: str, user_id: int) -> None:
#     query = '''
#     INSERT INTO job(
#         position,
#         company,
#         website,
#         location,
#         commitment,
#         work_type,
#         salary_top,
#         salary_bottom,
#         salary_type,
#         resume_version,
#         job_description_file,
#         user_id
#         )
#     VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
#     '''
#     insert = (position, company, website, location, commitment, work_type, salary_top, salary_bottom, salary_type,
#               resume_version, job_description_file, user_id)
#     cursor.execute(query, insert)
#     conn.commit()
#
#
# def add_event(cursor: sqlite3.Cursor, conn: sqlite3.connect, date: str, time: str,
#               note: Union[str, None],
#               status_id: int, contact_id: Union[int, None], job_id: int, user_id: int) -> None:
#     query = '''
#     INSERT INTO event(
#         date,
#         time,
#         note,
#         status_id,
#         contact_id,
#         job_id,
#         user_id
#         )
#     VALUES (?,?,?,?,?,?,?)
#     '''
#     insert = (date, time, note, status_id, contact_id, job_id, user_id)
#     cursor.execute(query, insert)
#     conn.commit()
#
#
# def date_change(unit: int, day=False, hour=False, add=False) -> str:
#     """Change day or hour by unit. default subtract, add=True to add unit time.
#     Used to insert relevant datetime values into new sample database"""
#     previous_time = None
#     current_time = datetime.datetime.now()
#     if day:
#         day_change = datetime.timedelta(days=unit)
#         if add:
#             previous_time = (current_time + day_change).strftime('%Y-%m-%d')
#         else:
#             previous_time = (current_time - day_change).strftime('%Y-%m-%d')
#     if hour:
#         day_change = datetime.timedelta(hours=unit)
#         if add:
#             previous_time = (current_time + day_change).strftime('%I:%M%p')
#         else:
#             previous_time = (current_time - day_change).strftime('%I:%M%p')
#
#     return previous_time
#
#
# def add_contact(cursor: sqlite3.Cursor, conn: sqlite3.connect, first_name: str, last_name: str, email: str, phone: str,
#                 position: str, job_id: int, user_id: int) -> None:
#     query = '''
#     INSERT INTO contact(
#         first_name,
#         last_name,
#         email,
#         phone,
#         position,
#         job_id,
#         user_id
#         )
#     VALUES (?,?,?,?,?,?,?)
#     '''
#     insert = (first_name, last_name, email, phone, position, job_id, user_id)
#     cursor.execute(query, insert)
#     conn.commit()


# def add_sample_data(cursor: sqlite3.Cursor, conn: sqlite3.connect):
#     add_user(cursor, conn, "brendan", 0)
#
#     add_job(cursor, conn, "Software Engineer", "Tech Innovators", "www.techinnovators.com", "San Francisco",
#             "Full-time", "Engineering", 120000, 95000, "Annual", 2, "software_engineer_description.txt", 1),
#     add_job(cursor, conn, "Data Analyst", "Data Insights Inc.", "www.datainsights.com", "New York", "Part-time",
#             "Data Science", 90000, 70000, "Annual", 1, "data_analyst_description.txt", 1),
#     add_job(cursor, conn, "Web Developer", "Web Solutions Ltd.", "www.websolutions.com", "London", "Full-time",
#             "Development", 110000, 85000, "Annual", 1, "web_developer_description.txt", 1),
#     add_job(cursor, conn, "UX Designer", "UserXperience Labs", "www.uxlabs.com", "Seattle", "Full-time", "Design",
#             100000, 80000, "Annual", 2, "ux_designer_description.txt", 1),
#     add_job(cursor, conn, "DevOps Engineer", "Cloud Innovations", "www.cloudinnovations.com", "Austin", "Full-time",
#             "Engineering", 130000, 100000, "Annual", 1, "devops_engineer_description.txt", 1)
#
#     add_event(cursor, conn, date_change(1, day=True), date_change(1, hour=True), None, 1, 1, 1, 1)
#     add_event(cursor, conn, date_change(3, day=True), date_change(5, hour=True), None, 2, 2, 2, 1)
#     add_event(cursor, conn, date_change(4, day=True), date_change(3, hour=True), None, 3, 3, 3, 1)
#     add_event(cursor, conn, date_change(5, day=True, add=True), date_change(1, hour=True), None, 4, 4, 4,
#               1)
#
#     add_contact(cursor, conn, "John", "Smith", "john.smith@example.com", "123-456-7890", "Hiring Manager", 1, 1)
#     add_contact(cursor, conn, "Jane", "Doe", "jane.doe@example.com", "987-654-3210", "Recruitment Lead", 2, 1)
#     add_contact(cursor, conn, "Michael", "Johnson", "michael.johnson@example.com", "555-123-4567", "Talent Acquisition",
#                 3, 1)
#     add_contact(cursor, conn, "Sarah", "Williams", "sarah.williams@example.com", "222-333-4444", "HR Manager", 4, 1)
#     add_contact(cursor, conn, "David", "Brown", "david.brown@example.com", "111-222-3333", "Head of HR", 4, 1)


def sample_data(cursor: sqlite3.Cursor, conn: sqlite3.connect):
    job_insert = """
        INSERT INTO job (position, company, website, location, commitment, work_type, salary_top, salary_bottom, salary_type, resume_version, job_description_file, user_id)
        VALUES
            ('Software Engineer', 'TechCo', 'www.techco.com', 'San Francisco, CA', 'Full-Time', 'Onsite', 120000, 90000, 'Annual', '1.1', NULL, 1),
            ('Data Scientist', 'DataTech', 'www.datatech.com', 'New York, NY', 'Part-Time', 'Remote', 95000, 75000, 'Annual', '1.2', NULL, 1),
            ('Frontend Developer', 'WebSolutions', 'www.websolutions.com', 'Seattle, WA', 'Full-Time', 'Hybrid', 110000, 85000, 'Annual', '1.1', NULL, 1),
            ('DevOps Engineer', 'CloudOps', 'www.cloudops.com', 'Austin, TX', 'Full-Time', 'Onsite', 130000, 100000, 'Annual', '1.2', NULL, 1),
            ('UI/UX Designer', 'DesignIt', 'www.designit.com', 'Los Angeles, CA', 'Contract', 'Remote', 85000, 65000, 'Annual', '1.1', NULL, 1),
            ('Backend Developer', 'CodeCraft', 'www.codecraft.com', 'San Francisco, CA', 'Full-Time', 'Onsite', 125000, 95000, 'Annual', '1.1', NULL, 1),
            ('Machine Learning Engineer', 'AI Innovations', 'www.aiinnovations.com', 'New York, NY', 'Full-Time', 'Hybrid', 140000, 110000, 'Annual', '1.2', NULL, 1),
            ('Mobile App Developer', 'AppGenius', 'www.appgenius.com', 'Seattle, WA', 'Part-Time', 'Remote', 90000, 70000, 'Annual', '1.1', NULL, 1),
            ('QA Tester', 'TestMasters', 'www.testmasters.com', 'Austin, TX', 'Contract', 'Onsite', 95000, 75000, 'Annual', '1.2', NULL, 1),
            ('Product Designer', 'InnovateUX', 'www.innovateux.com', 'Los Angeles, CA', 'Full-Time', 'Hybrid', 115000, 90000, 'Annual', '1.1', NULL, 1),
            ('Software Engineer', 'CodeTech', 'www.codetech.com', 'San Francisco, CA', 'Full-Time', 'Onsite', 130000, 100000, 'Annual', '1.1', NULL, 1),
            ('Data Analyst', 'DataInsights', 'www.datainsights.com', 'New York, NY', 'Part-Time', 'Remote', 97000, 77000, 'Annual', '1.2', NULL, 1),
            ('Full Stack Developer', 'WebWizards', 'www.webwizards.com', 'Seattle, WA', 'Full-Time', 'Hybrid', 120000, 95000, 'Annual', '1.1', NULL, 1),
            ('Cloud Architect', 'CloudSolutions', 'www.cloudsolutions.com', 'Austin, TX', 'Full-Time', 'Onsite', 140000, 110000, 'Annual', '1.2', NULL, 1),
            ('UI Designer', 'PixelPerfect', 'www.pixelperfect.com', 'Los Angeles, CA', 'Contract', 'Remote', 87000, 67000, 'Annual', '1.1', NULL, 1);
    """
    cursor.execute(job_insert)
    conn.commit()
