import datetime
import sqlite3
import sys
import os
from dataclasses import dataclass
import tkinter

from user_interface import JobInputs, JobDescriptionUI
from models import JobApplication

@dataclass
class SqlQueries:
    create_table = '''
        CREATE TABLE job_application (
        application_date,
        position_title,
        company,
        job_location,
        resume_version,
        salary_top,
        salary_bottom,
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
        salary_top,
        salary_bottom,
        application_platform,
        application_status,
        work_type,
        job_type,
        job_description_file_path
        )
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        '''


class InitializeTOJA:
    def __init__(self):

        self.db_file_name = 'toja/job_application_database.db'
        self.job_description_file_directory = "C:/Users/brend/PycharmProjects/Job_Application_Tracking/toja/job_descriptions/"

        # Development database and job description

        # self.db_file_name = '../tests/test_job_application_database.db'
        # self.job_description_file_directory = "../tests/test_job_descriptions/"

        # Check if database exists, if not create
        # print(os.path.dirname(self.db_file_name))

        if not os.path.exists(self.db_file_name):
            self.conn = sqlite3.connect(self.db_file_name)
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql_queries.create_table)
        else:
            self.conn = sqlite3.connect(self.db_file_name)
            self.cursor = self.conn.cursor()

    def close_db_connections(self):
        self.conn.close()


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
                job_app = JobApplication(init_toja,user_inputs)
                job_descript_paste = JobDescriptionUI(init_toja, job_app)
                job_app.add_to_database(sql_queries)
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
