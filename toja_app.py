import datetime
import sqlite3
import sys
import os
from dataclasses import dataclass
import tkinter


@dataclass
class SqlQueries:
    create_table = '''
        CREATE TABLE job_application (
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
    '''

    insert_new_app = '''
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


class InitializeTOJA:
    def __init__(self):
        self.db_file_name = 'job_application_database.db'

        # Development database
        # self.db_file_name = 'dev_job_application_database.db'

        # Check if database exists, if not create
        if not os.path.exists(self.db_file_name):
            self.conn = sqlite3.connect(self.db_file_name)
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql_queries.create_table)
        else:
            self.conn = sqlite3.connect(self.db_file_name)
            self.cursor = self.conn.cursor()

    def close_db_connections(self):
        self.conn.close()


class JobInputs:
    def __init__(self):
        print('\nEnter Application Details Below or Leave Blank\n')
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

    # with open(f"job_descriptions/{self.job_description_file_name}", "w") as job_desc:
    #     job_desc.write(self.job_description_paste_text)
    #

# class JobDescription


class JobApplication:
    def __init__(self):
        self.application_date = datetime.date.today()
        # self.position_title = input('Enter the Position Title: ').lower()
        # self.company = input('Enter the Company Name: ').lower()
        # self.job_location = input('Enter the Job Location: ')
        # try:
        #     self.resume_version = float(input('Enter the Resume Version: '))
        # except ValueError:
        #     self.resume_version = None
        # self.application_platform = input('Enter the Application Platform: ').lower()
        self.application_status = "submitted"
        # self.work_type = input('Location Type (remote,hybrid,onsite): ').lower()
        # self.job_type = input('Job Type (full-time, part-time, contract, freelance): ').lower()

        # self.job_description_file_name = f"{self.application_date}_{self.position_title}_{self.company}.txt"
        # print('Paste Job Description Text and press CTRL-D or CTRL-Z when done: ')
        # self.job_description_paste_text = sys.stdin.read()
        self.job_description_file_name = "blank"
        self.conn = init_toja.conn
        self.cursor = init_toja.cursor


        # with open(f"job_descriptions/{self.job_description_file_name}", "w") as job_desc:
        #     job_desc.write(self.job_description_paste_text)

    def add_to_database(self):
        data = (
            self.application_date,
            user_inputs.position_title,
            user_inputs.company,
            user_inputs.job_location,
            user_inputs.resume_version,
            user_inputs.application_platform,
            self.application_status,
            user_inputs.work_type,
            user_inputs.job_type,
            self.job_description_file_name
        )

        self.cursor.execute(sql_queries.insert_new_app, data)
        self.conn.commit()
        print(f"{user_inputs.position_title} position at {user_inputs.company} Successfully Entered")


if __name__ == '__main__':
    sql_queries = SqlQueries()
    init_toja = InitializeTOJA()

    program_run = True
    while program_run:
        print("\nMenu:\n"
              "1) ADD New Job Application\n"
              "2) UPDATE Job Application\n"
              "3) GENERATE Job Analytics\n"
              "4) Settings\n"
              "5) QUIT")

        try:
            users_menu_select = int(input("\nEnter Number: "))

            if users_menu_select == 1:
                user_inputs = JobInputs()
                new_job = JobApplication()
                new_job.add_to_database()
                sys.exit()

            elif users_menu_select == 2:
                print("feature coming soon")
            elif users_menu_select == 3:
                print("feature coming soon")
            elif users_menu_select == 4:
                print("feature coming soon")
            elif users_menu_select == 5:
                program_run = False
            else:
                print("Invalid Entry")

        except ValueError:
            print("Enter Valid Number")

    init_toja.close_db_connections()
