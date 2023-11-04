
from views.home import HomeView
from views.theme import Theme
from model import Model
from config import Config
from controller import Controller


def run_toja_app():
    theme = Theme()
    config = Config(theme)
    new_user = False
    if config.is_user_new():
        config.initialize_user()  # stores config data in config.ini
        new_user = True

    model = Model(config)
    view = HomeView(theme)
    if new_user:
        # welcome_window, user can select sample data or create new user
        controller = Controller(view, model, new_user=True)
    else:
        controller = Controller(view, model)
    controller.run()


if __name__ == '__main__':
    run_toja_app()
