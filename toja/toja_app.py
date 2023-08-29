from views.home import HomeView
from model import Model, Config
from controller import Controller


def run_toja_app():
    user = Config()
    new_user = False
    if user.is_user_new():
        user.initialize_user()  # stores path to database in config.ini
        new_user = True

    model = Model(user)
    view = HomeView()
    if new_user:
        # welcome_window, user can select sample data or create new database
        controller = Controller(view, model, new_user=True)
    else:
        controller = Controller(view, model)
    controller.run()


if __name__ == '__main__':
    run_toja_app()
