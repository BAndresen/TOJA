
from toja.views.home_view import HomeView
from model import Model
from controller import Controller
from pathlib import Path

BASE_DIRECTORY = Path(__file__).resolve().parent
DATABASE_FILE_PATH = Path(*[BASE_DIRECTORY, 'database/toja_database.db'])
JOB_DESCRIPTION_DIRECTORY = Path(*[BASE_DIRECTORY], 'job_descriptions')


def run_toja_app() -> None:
    model = Model(DATABASE_FILE_PATH)
    view = HomeView()
    controller = Controller(view, model)
    controller.run()


if __name__ == '__main__':
    run_toja_app()
