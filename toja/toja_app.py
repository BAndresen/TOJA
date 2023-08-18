from pathlib import Path

from views.home_view import HomeView
from model import Model
from controller import Controller

BASE_DIRECTORY = Path(__file__).resolve().parent
GRANDPARENT_DIRECTORY = Path(BASE_DIRECTORY).resolve().parent
DATABASE_FILE_PATH = Path(*[BASE_DIRECTORY, 'database\\toja_database.db'])
JOB_DESCRIPTION_DIRECTORY = Path(*[BASE_DIRECTORY, 'job_descriptions'])
TEST_JOB_DESCRIPTION_DIRECTORY = Path(*[GRANDPARENT_DIRECTORY], 'tests\\test_job_descriptions')


def run_toja_app() -> None:
    model = Model(DATABASE_FILE_PATH,
                  TEST_JOB_DESCRIPTION_DIRECTORY)
    # JOB_DESCRIPTION_DIRECTORY)
    # sample_data=True to add sample data

    view = HomeView()
    controller = Controller(view, model)
    controller.run()


if __name__ == '__main__':
    run_toja_app()
