import customtkinter

from view import HomeWindow
from model import Database
from controller import Controller
from pathlib import Path

BASE_DIRECTORY = Path(__file__).resolve().parent
DATABASE_FILE_PATH = Path(*[BASE_DIRECTORY, 'database/job_application_database.db'])
JOB_DESCRIPTION_DIRECTORY = Path(*[BASE_DIRECTORY], 'job_descriptions')


def run_toja_app():
    database = Database(DATABASE_FILE_PATH)
    root = customtkinter.CTk()
    home_window = HomeWindow(root)
    Controller(home_window, database)
    database.close_db_connections()
    root.mainloop()


if __name__ == '__main__':
    run_toja_app()
