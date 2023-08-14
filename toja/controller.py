from view import HomeWindow
from model import Database


class Controller:
    def __init__(self, root: HomeWindow, database: Database):
        self.view = root
        self.database = database
