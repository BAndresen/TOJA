import tkinter
from datetime import datetime
from pathlib import Path
from typing import Union
import os

from views.new_job import NewJob
from views.job_profile import JobProfile
from views.home_view import HomeView
from views.new_event import NewEvent
from model import Model


class Controller:
    def __init__(self, view: HomeView, model: Model):
        self.today = datetime.today().date()
        self.new_job = None
        self.view = view
        self.model = model

        # HomeView Button Commands
        self.view.events_button.configure(command=self.event_frame_button)
        self.view.home_button.configure(command=self.home_frame_button)
        self.view.analytics_button.configure(command=self.analytics_frame_button)
        self.view.new_job_button.configure(command=self.open_job_submit)

        # HomeView ListBox
        self.view.job_list_box.bind('<Double-Button-1>', self.open_job_profile)
        self.view.job_list_box.bind('<Return>', self.open_job_profile)
        self.update_home_listbox()

    def update_home_listbox(self):
        # self.view.job_list_box.delete("all")  # ------ CTKlistbox
        self.view.job_list_box.delete(0, tkinter.END)  # -------tkinter Listbox

        home_listbox = self.model.get_all()
        for item in home_listbox:
            # self.view.job_list_box.insert("END", f"{item[0]} | {item[1]} | {item[2]}")  # ------ CTKlistbox
            self.view.job_list_box.insert(tkinter.END, f"{item[0]} | {item[1]} | {item[2]}")  # ----- tkinter Listbox

    def open_job_profile(self) -> None:
        event_str = (self.view.job_list_box.get(self.view.job_list_box.curselection()))
        self.job_id = (event_str.split())[0]
        self.job_profile = JobProfile(self.view)
        results = self.model.get_job_data(self.job_id)
        self.job_profile.delete_button.configure(command=self.delete)

        self.job_profile.company_name_user.configure(text=results[0])
        self.job_profile.company_web_user.configure(text=results[1])
        self.job_profile.position_user.configure(text=results[2])
        self.job_profile.location_user.configure(text=results[3])
        self.job_profile.commitment_user.configure(text=results[4])
        self.job_profile.work_type_user.configure(text=results[5])
        self.job_profile.salary_top_user.configure(text=results[6])
        self.job_profile.salary_bottom_user.configure(text=results[7])
        self.job_profile.salary_type_user.configure(text=results[8])
        self.job_profile.resume_user.configure(text=results[9])

        self.job_profile.job_description_label.configure(text=self.model.open_job_description(results[10]))
        self.update_event_listbox()


    def delete(self):
        self.model.delete_job(self.job_id)
        self.job_profile.jp_window.destroy()
        self.update_home_listbox()

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

    def open_job_submit(self):
        self.new_job = NewJob(self.view)
        self.new_job.submit_button.configure(command=self.submit_new_job)

    def open_new_event(self):
        self.new_job.aj_window.destroy()
        self.open_new_event = NewEvent(self.view)

    def submit_new_job(self):
        self.company = self.new_job.company_name_entry.get()
        self.position = self.new_job.position_title_entry.get()
        self.job_file = f'{self.today}_{self.new_job.company_name_entry.get()}_{self.new_job.position_title_entry.get()}.txt',
        job_text = self.new_job.job_description_textbox.get("1.0", "end-1c")
        self.job_file = self.check_job_file(self.job_file, job_text)
        self.model.add_new_job(
            self.position,
            self.company,
            self.new_job.company_website_entry.get(),
            self.new_job.job_location_entry.get(),
            self.new_job.job_type_entry.get(),
            self.new_job.location_type_entry.get(),
            self.new_job.salary_top_entry.get(),
            self.new_job.salary_bottom_entry.get(),
            self.new_job.salary_type_entry.get(),
            self.new_job.resume_version_entry.get(),
            self.job_file,
            1,
            self.new_job.day_entry.get(),
            self.new_job.time_entry.get(),
            self.new_job.note_entry.get("1.0", "end-1c"),
            self.new_job.event_entry.get(),
            None,
        )
        if self.job_file:
            self.model.save_job_description(self.job_file,job_text)

        self.update_home_listbox()
        self.new_job.aj_window.destroy()

    def check_job_file(self, job_file, job_text) -> Union[str, None]:
        if job_text == "":
            return None
        else:
            return job_file[0]

    def update_event_listbox(self):
        self.job_profile.event_scroll.delete(0, tkinter.END)

        event_listbox = self.model.get_event(self.job_id)
        for item in event_listbox:
            self.job_profile.event_scroll.insert(tkinter.END, f"{item[0]} | {item[1]} | {item[3]} | {item[2]}")  # ----- tkinter Listbox

