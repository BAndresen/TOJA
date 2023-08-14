from view import HomeWindow
from model import Database


class Controller:
    def __init__(self, root: HomeWindow, database: Database):
        self.view = root
        self.database = database

        self.view.events_button.configure(command=self.event_frame_button)
        self.view.home_button.configure(command=self.home_frame_button)
        self.view.analytics_button.configure(command=self.analytics_frame_button)

    def event_frame_button(self):
        self.view.home_frame.grid_forget()
        self.view.event_frame.grid(row=0, column=1, sticky="nsew")

    def home_frame_button(self):
        self.view.event_frame.grid_forget()
        self.view.home_frame.grid(row=0, column=1, sticky="nsew")

    def analytics_frame_button(self):
        pass
