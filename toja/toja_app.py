from views.home import HomeView
from model import Model, Config
from controller import Controller


def run_toja_app():
    user = Config()
    if user.is_user_new():
        user.initialize_user()

    model = Model(user)
    view = HomeView()
    controller = Controller(view, model)
    controller.run()


if __name__ == '__main__':
    run_toja_app()
