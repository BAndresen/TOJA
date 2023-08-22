from pathlib import Path
import configparser

from views.home import HomeView
from model import Model
from controller import Controller, Config


def run_toja_app() -> None:
    user = Config()
    if user.is_user_new():
        user.initialize_user()

    model = Model(user.get_database(), user.get_job_description_dir())
    view = HomeView()
    controller = Controller(view, model)
    controller.run()


if __name__ == '__main__':
    run_toja_app()
