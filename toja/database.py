import datetime
import os
import sqlite3


def load_sql_query(file_name: str) -> str:
    with open(file_name, "r") as sql_file:
        # print(type(sql_file.read()))
        return sql_file.read()


class DatabaseConnection:
    def __init__(self, db_file_path, create_table):
        self.db_file_path = db_file_path

        # Check if database exists, if not create
        self.create_job_application_table = (load_sql_query(create_table))
        if not os.path.exists(self.db_file_path):
            self.conn = sqlite3.connect(self.db_file_path)
            self.cursor = self.conn.cursor()
            self.cursor.execute(self.create_job_application_table)
        else:
            self.conn = sqlite3.connect(self.db_file_path)
            self.cursor = self.conn.cursor()

    def close_db_connections(self):
        self.conn.close()


class DatabaseQuery:
    def __init__(self, conn_database, job_description_directory):
        self.application_date = datetime.date.today()
        self.job_description_file_directory = job_description_directory
        self.conn = conn_database.conn
        self.cursor = conn_database.cursor
        # self.job_description_file_directory = conn_database.job_description_file_directory
        self.job_description_file_name = ''

    def add_to_database(self, job_inputs, insert_job_sql):

        insert_new_job_application = load_sql_query(insert_job_sql)
        job_file_name = f'{self.job_description_file_name}'
        application_status = "submitted"
        data = (
            self.application_date,
            job_inputs.position_title,
            job_inputs.company,
            job_inputs.job_location,
            job_inputs.resume_version,
            job_inputs.salary_top,
            job_inputs.salary_bottom,
            job_inputs.application_platform,
            application_status,
            job_inputs.work_type,
            job_inputs.job_type,
            job_file_name
        )

        self.cursor.execute(insert_new_job_application, data)
        self.conn.commit()

