
from view import HomeView, NewJob
from model import Model


class Controller:
    def __init__(self, view: HomeView, model: Model):

        self.new_job = None
        self.view = view
        self.database = model

        # frames
        self.view.events_button.configure(command=self.event_frame_button)
        self.view.home_button.configure(command=self.home_frame_button)
        self.view.analytics_button.configure(command=self.analytics_frame_button)

        self.view.new_job_button.configure(command=self.submit_button)

    def run(self):
        self.view.mainloop()

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

    def submit_button(self):
        self.new_job = NewJob(self.view)
        self.new_job.submit_button.configure(command=self.submit_data)

    def submit_data(self):
        print('submit_data')




