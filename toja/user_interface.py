import datetime
import tkinter
import customtkinter
# from toja_app import database
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from views.sql_file_path import INSERT_NEW_JOB_APP_SQL
from database import Database, load_sql_query


@dataclass
class Job:
    application_date = datetime,
    position_title = str,
    company_name = str,
    job_location = str,
    resume_version = float,
    salary_top = int,
    salary_bottom = int,
    app_platform = str,
    application_status = str,
    location_type = str,
    job_type = str,
    # job_file_name = str,


def open_new_jobs(root: customtkinter, job: Job, database: Database):
    NewJobInputs(root, job, database)


class HomeWindow:
    def __init__(self, root: customtkinter.CTk, job: Job, database: Database):
        self.job = job
        self.database = database
        # super().__init__()
        # self.minsize(width=1000, height=700)
        self.root = root
        self.root.title("Track and Optimize your Job Application Process")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.stat_board_frame = customtkinter.CTkFrame(self.root)
        self.stat_board_frame.grid(row=0, rowspan=2, column=1, padx=20, pady=20, sticky="nsew")

        self.stat_label = customtkinter.CTkLabel(self.stat_board_frame, text="stat board placeholder")
        self.stat_label.grid(row=0, column=0, padx=150, pady=150)

        self.calendar_frame = customtkinter.CTkFrame(self.root)
        self.calendar_frame.grid(row=2, columnspan=2, column=0, padx=20, pady=20, sticky="nsew")
        self.calendar_label_placeholder = (customtkinter.CTkLabel(
            self.calendar_frame, text="calendar placeholder"))
        self.calendar_label_placeholder.grid(row=0, column=0, padx=50, pady=50)

        self.button_frame = customtkinter.CTkFrame(self.root)
        self.button_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        self.new_job_button = customtkinter.CTkButton(self.button_frame, text="Add",
                                                      command=lambda: open_new_jobs(self.root, self.job, self.database))
        self.new_job_button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.new_job_button = customtkinter.CTkButton(self.button_frame, text="Update")
        self.new_job_button.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        self.new_job_button = customtkinter.CTkButton(self.button_frame, text="Analyze")
        self.new_job_button.grid(row=1, column=2, padx=20, pady=20, sticky="nsew")


class NewJobInputs:
    def __init__(self, home_window: HomeWindow, job: Job, database: Database):
        self.job = job
        self.database = database
        super().__init__()
        self.window = customtkinter.CTkToplevel(home_window)
        self.window.attributes('-topmost', True)
        self.window.title("Add Job Application Process")
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(0, weight=1)

        self.main_frame = customtkinter.CTkFrame(self.window)
        self.main_frame.grid(row=0, column=1, padx=50, pady=50, sticky="nsew")

        self.position_title_entry = customtkinter.CTkEntry(self.main_frame)
        self.position_title_entry.grid(row=0, column=1, padx=(5, 20), pady=20)
        self.position_title_label = customtkinter.CTkLabel(self.main_frame, text='Position Title')
        self.position_title_label.grid(row=0, column=0, padx=(20, 5), pady=10, sticky="e")

        self.company_name_entry = customtkinter.CTkEntry(self.main_frame)
        self.company_name_entry.grid(row=1, column=1, padx=(5, 20), pady=20)
        self.company_name_label = customtkinter.CTkLabel(self.main_frame, text='Company Name')
        self.company_name_label.grid(row=1, column=0, padx=(20, 5), pady=10, sticky="e")

        self.job_location_entry = customtkinter.CTkEntry(self.main_frame)
        self.job_location_entry.grid(row=2, column=1, padx=(5, 20), pady=20)
        self.job_location_label = customtkinter.CTkLabel(self.main_frame, text='Job Location')
        self.job_location_label.grid(row=2, column=0, padx=(20, 5), pady=10, sticky="e")

        self.resume_version_entry = customtkinter.CTkEntry(self.main_frame)
        self.resume_version_entry.grid(row=3, column=1, padx=(5, 20), pady=20)
        self.resume_version_label = customtkinter.CTkLabel(self.main_frame, text='Resume Version')
        self.resume_version_label.grid(row=3, column=0, padx=(20, 5), pady=10, sticky="e")

        self.salary_top_entry = customtkinter.CTkEntry(self.main_frame)
        self.salary_top_entry.grid(row=4, column=1, padx=(5, 20), pady=20)
        self.salary_top_label = customtkinter.CTkLabel(self.main_frame, text='Salary Top-End Range')
        self.salary_top_label.grid(row=4, column=0, padx=(20, 5), pady=10, sticky="e")

        self.salary_bottom_entry = customtkinter.CTkEntry(self.main_frame)
        self.salary_bottom_entry.grid(row=5, column=1, padx=(5, 20), pady=20)
        self.salary_bottom_label = customtkinter.CTkLabel(self.main_frame, text='Salary Bottom-End Range')
        self.salary_bottom_label.grid(row=5, column=0, padx=(20, 5), pady=10, sticky="e")

        self.app_platform_entry = customtkinter.CTkEntry(self.main_frame)
        self.app_platform_entry.grid(row=6, column=1, padx=(5, 20), pady=20)
        self.app_platform_label = customtkinter.CTkLabel(self.main_frame, text='Application Platform')
        self.app_platform_label.grid(row=6, column=0, padx=(20, 5), pady=10, sticky="e")

        self.location_type_entry = customtkinter.CTkEntry(self.main_frame)
        self.location_type_entry.grid(row=7, column=1, padx=(5, 20), pady=20)
        self.location_type_label = customtkinter.CTkLabel(self.main_frame, text='Location Type (remote,hybrid,onsite)')
        self.location_type_label.grid(row=7, column=0, padx=(20, 5), pady=10, sticky="e")

        self.job_type_entry = customtkinter.CTkEntry(self.main_frame)
        self.job_type_entry.grid(row=9, column=1, padx=(5, 20), pady=20)
        self.job_type_label = customtkinter.CTkLabel(self.main_frame,
                                                     text='Job Type (full-time, part-time, contract, freelance)')
        self.job_type_label.grid(row=9, column=0, padx=(20, 5), pady=10, sticky="e")

        submit_button = customtkinter.CTkButton(self.main_frame, text="Submit", command=self.submit_button)
        submit_button.grid(row=10, column=1, padx=20, pady=20)

    def submit_button(self):
        self.job.position_title = self.position_title_entry.get()
        self.job.company_name = self.company_name_entry.get()
        self.job.job_location = self.job_location_entry.get()
        self.job.resume_version = self.resume_version_entry.get()
        self.job.salary_top = self.salary_top_entry.get()
        self.job.salary_bottom = self.salary_bottom_entry.get()
        self.job.app_platform = self.app_platform_entry.get()
        self.job.location_type = self.location_type_entry.get()
        self.job.job_type = self.job_type_entry.get()

        self.database.add_job(self.job, INSERT_NEW_JOB_APP_SQL)
        self.window.destroy()


class JobDescription(tkinter.Tk):
    def __init__(self, job_file_path: str, job_file_name: str):
        self.job_description_file_name = job_file_name
        self.job_description_file_path = job_file_path
        super().__init__()
        self.minsize(height=500, width=500)
        self.paste_label = tkinter.Label(text="Paste Job Description")
        self.paste_label.pack()
        self.entry_box = tkinter.Text(width=50, height=30)
        self.entry_box.pack()
        self.submit_button = tkinter.Button(text="submit", command=self.submit_job_description)
        self.submit_button.pack()
        self.mainloop()

    def submit_job_description(self):
        job_description = self.entry_box.get("1.0", "end")
        with open(f"{self.job_description_file_path}{self.job_description_file_name}", "w") as file:
            file.write(job_description)

        self.destroy()
