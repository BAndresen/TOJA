from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from view import HomeWindow


# from view import HomeWindow, NewJob
from model import Database


class Controller:
    def __init__(self, root:HomeWindow, database: Database):
        self.add_job_description = None
        self.add_new_job = None
        self.view = root
        self.database = database

        # frames
        self.view.events_button.configure(command=self.event_frame_button)
        self.view.home_button.configure(command=self.home_frame_button)
        self.view.analytics_button.configure(command=self.analytics_frame_button)
        # self.view.submit_button.configure(command=self.submit_new_job)

    def event_frame_button(self):
        self.view.home_frame.grid_forget()
        self.view.analytics_frame.grid_forget()
        self.view.event_frame.grid(row=0, column=1, sticky="nsew")

    def home_frame_button(self):
        self.view.event_frame.grid_forget()
        self.view.analytics_frame.grid_forget()
        self.view.home_frame.grid(row=0, column=1, sticky="nsew")

    def analytics_frame_button(self):
        self.view.home_frame.grid_forget()
        self.view.event_frame.grid_forget()
        self.view.analytics_frame.grid(row=0, column=1, sticky="nsew")

    def submit_new_job(self):
        # self.new_job.root.destroy()
        print("submit")

        pass


