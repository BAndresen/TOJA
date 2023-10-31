import customtkinter
from tkcalendar import DateEntry

import toja.constants as constant
from .theme import Theme


class NewJob:
    def __init__(self, root, theme: Theme):
        self.root = root
        self.aj_window = customtkinter.CTkToplevel(root)
        self.aj_window.attributes('-topmost', 'true')
        self.aj_window.title("Add Job")

        self.main_frame = customtkinter.CTkFrame(self.aj_window)
        self.main_frame.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)

        self.main_job_frame = customtkinter.CTkFrame(self.main_frame)
        self.main_job_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.main_job_frame.grid_columnconfigure(0, weight=1)

        self.position_title_entry = customtkinter.CTkEntry(self.main_job_frame)
        self.position_title_entry.grid(row=0, column=1, padx=(5, 20), pady=(20,2))
        self.position_title_label = customtkinter.CTkLabel(self.main_job_frame, text='Position')
        self.position_title_label.grid(row=0, column=0, padx=(20, 5), pady=(20,2), sticky="e")

        self.company_name_entry = customtkinter.CTkEntry(self.main_job_frame)
        self.company_name_entry.grid(row=1, column=1, padx=(5, 20), pady=2)
        self.company_name_label = customtkinter.CTkLabel(self.main_job_frame, text='Company')
        self.company_name_label.grid(row=1, column=0, padx=(20, 5), pady=2, sticky="e")

        self.company_website_entry = customtkinter.CTkEntry(self.main_job_frame)
        self.company_website_entry.grid(row=2, column=1, padx=(5, 20), pady=2)
        self.company_website_label = customtkinter.CTkLabel(self.main_job_frame, text='Website')
        self.company_website_label.grid(row=2, column=0, padx=(20, 5), pady=2, sticky="e")

        self.job_location_entry = customtkinter.CTkEntry(self.main_job_frame)
        self.job_location_entry.grid(row=3, column=1, padx=(5, 20), pady=2)
        self.job_location_label = customtkinter.CTkLabel(self.main_job_frame, text='Location')
        self.job_location_label.grid(row=3, column=0, padx=(20, 5), pady=2, sticky="e")

        self.resume_version_entry = customtkinter.CTkEntry(self.main_job_frame)
        self.resume_version_entry.grid(row=4, column=1, padx=(5, 20), pady=2)
        self.resume_version_label = customtkinter.CTkLabel(self.main_job_frame, text='Resume Version')
        self.resume_version_label.grid(row=4, column=0, padx=(20, 5), pady=2, sticky="e")

        self.salary_top_entry = customtkinter.CTkEntry(self.main_job_frame)
        self.salary_top_entry.grid(row=5, column=1, padx=(5, 20), pady=2)
        self.salary_top_label = customtkinter.CTkLabel(self.main_job_frame, text='Salary Top-End')
        self.salary_top_label.grid(row=5, column=0, padx=(20, 5), pady=2, sticky="e")

        self.salary_bottom_entry = customtkinter.CTkEntry(self.main_job_frame)
        self.salary_bottom_entry.grid(row=6, column=1, padx=(5, 20), pady=2)
        self.salary_bottom_label = customtkinter.CTkLabel(self.main_job_frame, text='Salary Bottom-End')
        self.salary_bottom_label.grid(row=6, column=0, padx=(20, 5), pady=2, sticky="e")

        self.salary_type_entry = customtkinter.CTkComboBox(self.main_job_frame,
                                                           values=constant.EARNING_TYPE)
        self.salary_type_entry.grid(row=7, column=1, padx=(5, 20), pady=2)
        self.salary_type_label = customtkinter.CTkLabel(self.main_job_frame, text='Salary Type')
        self.salary_type_label.grid(row=7, column=0, padx=(20, 5), pady=2, sticky="e")

        self.location_type_entry = customtkinter.CTkComboBox(self.main_job_frame,
                                                             values=constant.WORK_TYPE)
        self.location_type_entry.grid(row=8, column=1, padx=(5, 20), pady=2)
        self.location_type_label = customtkinter.CTkLabel(self.main_job_frame,
                                                          text='Work Type')
        self.location_type_label.grid(row=8, column=0, padx=(20, 5), pady=2, sticky="e")

        self.job_type_entry = customtkinter.CTkComboBox(self.main_job_frame,
                                                        values=constant.SALARY_TYPE)
        self.job_type_entry.grid(row=9, column=1, padx=(5, 20), pady=2)
        self.job_type_label = customtkinter.CTkLabel(self.main_job_frame, text='Commitment')
        self.job_type_label.grid(row=9, column=0, padx=(20, 5), pady=2, sticky="e")

        self.job_description_label = customtkinter.CTkLabel(self.main_job_frame, text='Job Description')
        self.job_description_label.grid(row=10, column=0)

        self.job_description_textbox = customtkinter.CTkTextbox(self.main_job_frame)
        self.job_description_textbox.grid(row=11, column=0, columnspan=2, sticky='ew', padx=20, pady=20)

        self.event_info_frame = customtkinter.CTkFrame(self.main_frame)
        self.event_info_frame.grid(row=0, column=1, padx=20, pady=20, stick='nsew')

        self.event_entry = customtkinter.CTkComboBox(self.event_info_frame, values=constant.EVENT_TYPE, width=125)
        self.event_entry.grid(row=0, column=1, padx=(5, 20), pady=(20,10))
        self.event_label = customtkinter.CTkLabel(self.event_info_frame, text='Event')
        self.event_label.grid(row=0, column=0, padx=(20, 5), pady=(20,10), sticky="e")

        self.day_entry = DateEntry(self.event_info_frame, selectmode='day', font=("roboto", "11"),
                                   date_pattern="yyyy-mm-dd")
        self.day_entry.grid(row=1, column=1, padx=(5, 20), pady=10)
        self.day_label = customtkinter.CTkLabel(self.event_info_frame, text='Day')
        self.day_label.grid(row=1, column=0, padx=(20, 5), pady=10, sticky="e")

        self.time_entry = customtkinter.CTkEntry(self.event_info_frame, width=125)
        self.time_entry.grid(row=2, column=1, padx=(5, 20), pady=10)
        self.time_label = customtkinter.CTkLabel(self.event_info_frame, text='Time')
        self.time_label.grid(row=2, column=0, padx=(20, 5), pady=10, sticky="e")

        self.note_entry = customtkinter.CTkTextbox(self.event_info_frame)
        self.note_entry.grid(row=6, column=1, padx=(5, 20), pady=10, columnspan=2)
        self.note_label = customtkinter.CTkLabel(self.event_info_frame, text='Notes')
        self.note_label.grid(row=5, column=0, padx=(20, 5), pady=10, sticky="e")

        self.submit_button = customtkinter.CTkButton(self.main_job_frame, text="Submit",
                                                     fg_color=theme.button_color,
                                                     text_color=theme.button_text_color,
                                                     width=theme.main_button_width
                                                     )
        self.submit_button.grid(row=12, column=1, padx=20, pady=20)
