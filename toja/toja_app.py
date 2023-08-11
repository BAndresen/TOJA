import customtkinter

from user_interface import HomeWindow, Job
from database import Database
from sql_query.sql_file_path import CREATE_JOB_APP_TABLE_SQL
from pathlib import Path

BASE_DIRECTORY = Path(__file__).resolve().parent
DATABASE_FILE_PATH = Path(*[BASE_DIRECTORY, 'job_application_database.db'])
JOB_DESCRIPTION_DIRECTORY = Path(*[BASE_DIRECTORY], 'job_descriptions')


def run_toja_app():
    database = Database(DATABASE_FILE_PATH,
                        JOB_DESCRIPTION_DIRECTORY,
                        CREATE_JOB_APP_TABLE_SQL)
    job = Job()
    root = customtkinter.CTk()
    HomeWindow(root, job, database)
    root.mainloop()
    database.close_db_connections()


if __name__ == '__main__':
    run_toja_app()
