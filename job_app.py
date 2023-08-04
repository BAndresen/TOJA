import datetime
import sqlite3
import sys


def create_new_table():
    conn = sqlite3.connect('job_application_database.db')
    cursor = conn.cursor()
    create_table = '''
    
    CREATE TABLE job_application (
        id INTEGER PRIMARY KEY,
        application_date TEXT,
        position_title TEXT,
        company TEXT,
        job_location TEXT,
        resume_version INTEGER,
        application_platform TEXT,
        application_status TEXT,
        work_type TEXT,
        job_type TEXT,
        job_description_file_path TEXT
        )
    '''
    cursor.execute(create_table)


class JobApplication:
    def __init__(self):
        print('\nEnter Application Details Below or Leave Blank\n')
        self.application_date = datetime.date.today()
        self.position_title = input('Enter the Position Title: ').lower()
        self.company = input('Enter the Company Name: ').lower()
        self.job_location = input('Enter the Job Location: ')
        try:
            self.resume_version = float(input('Enter the Resume Version: '))
        except ValueError:
            self.resume_version = None
        self.application_platform = input('Enter the Application Platform: ').lower()
        self.application_status = "submitted"
        self.work_type = input('Location Type (remote,hybrid,onsite): ').lower()
        self.job_type = input('Job Type (full-time, part-time, contract, freelance): ').lower()
        self.job_description_file_name = f"{self.application_date}_{self.position_title}_{self.company}.txt"
        print('Paste Job Description Text and press CTRL-D or CTRL-Z when done: ')
        self.job_description_paste_text = sys.stdin.read()

        # Connect to DataBase
        self.conn = sqlite3.connect('job_application_database.db')
        self.cursor = self.conn.cursor()

        with open(f"job_descriptions/{self.job_description_file_name}", "w") as job_desc:
            job_desc.write(self.job_description_paste_text)

    def add_to_database(self):
        insert_query = '''
        INSERT INTO job_application (
        application_date,
        position_title,
        company,
        job_location,
        resume_version,
        application_platform,
        application_status,
        work_type,
        job_type,
        job_description_file_path
        )
        VALUES (?,?,?,?,?,?,?,?,?,?)
        
        '''

        data = (
            self.application_date,
            self.position_title,
            self.company,
            self.job_location,
            self.resume_version,
            self.application_platform,
            self.application_status,
            self.work_type,
            self.job_type,
            self.job_description_file_name
        )

        self.cursor.execute(insert_query, data)
        self.conn.commit()
        self.conn.close()


new_job = JobApplication()
new_job.add_to_database()
print("Successfully Entered Job Application to DataBase")
