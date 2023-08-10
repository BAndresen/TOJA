import customtkinter

from user_interface import NewJobInputs, JobDescription, HomeWindow, Job
from database import Database
from views.sql_file_path import CREATE_JOB_APP_TABLE_SQL

# Database File Path
DATABASE_FILE_PATH = \
    'C:/Users/brend/PycharmProjects/Job_Application_Tracking/toja/job_application_database.db'

# Job Description File Path
JOB_DESCRIPTION_DIRECTORY = \
    'C:/Users/brend/PycharmProjects/Job_Application_Tracking/toja/job_descriptions/'


if __name__ == '__main__':
    database = Database(DATABASE_FILE_PATH,
                        JOB_DESCRIPTION_DIRECTORY,
                        CREATE_JOB_APP_TABLE_SQL)
    job = Job()
    root = customtkinter.CTk()
    home_window = HomeWindow(root, job, database)
    root.mainloop()
    database.close_db_connections()
