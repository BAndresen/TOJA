import customtkinter

from user_interface import NewJobInputs, JobDescription, HomeWindow, Job
from database import Database

# Database File Path
DATABASE_FILE_PATH = \
    'C:/Users/brend/PycharmProjects/Job_Application_Tracking/toja/job_application_database.db'

# Job Description File Path
JOB_DESCRIPTION_DIRECTORY = \
    'C:/Users/brend/PycharmProjects/Job_Application_Tracking/toja/job_descriptions/'

# Views
CREATE_JOB_APP_TABLE_SQL = \
    'C:/Users/brend/PycharmProjects/Job_Application_Tracking/toja/views/create_new_job_application_table.sql'
INSERT_NEW_JOB_APP_SQL = \
    'C:/Users/brend/PycharmProjects/Job_Application_Tracking/toja/views/insert_new_job_application.sql'

if __name__ == '__main__':
    database = Database(DATABASE_FILE_PATH,
                        JOB_DESCRIPTION_DIRECTORY,
                        CREATE_JOB_APP_TABLE_SQL)
    job = Job()
    root = customtkinter.CTk()
    home_window = HomeWindow(root, job)
    root.mainloop()

    # # NewJobInputs()
    # program_run = True
    # while program_run:
    #     print("\nMenu:\n"
    #           "1) ADD New Job Application\n"
    #           "2) UPDATE Job Application\n"
    #           "3) GENERATE Job Analytics\n"
    #           "4) Settings\n"
    #           "5) QUIT")
    #
    #     try:
    #         users_menu_select = int(input("\nEnter Number: "))
    #
    #         if users_menu_select == 1:
    #             # Get Job Description Inputs from User
    #             job_inputs = NewJobInputs()
    #
    #             database.job_description_file_name = \
    #                 f'{database.application_date}_{job_inputs.position_title}_{job_inputs.company}.txt'
    #
    #             # Window to allow Copy/Paste of Paste Job Description
    #             job_description = JobDescription(database.job_description_file_directory,
    #                                              database.job_description_file_name)
    #
    #             # Insert user data into database
    #             database.add_job(job_inputs, INSERT_NEW_JOB_APP_SQL)
    #
    #         elif users_menu_select == 2:
    #             print("feature coming soon")
    #         elif users_menu_select == 3:
    #             print("feature coming soon")
    #         elif users_menu_select == 4:
    #             print("feature coming soon")
    #         elif users_menu_select == 5:
    #             program_run = False
    #         else:
    #             print("Invalid Entry")
    #
    #     except ValueError:
    #         print("Enter Valid Number")

    database.close_db_connections()
