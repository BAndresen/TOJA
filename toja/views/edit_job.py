import customtkinter


class EditJob:
    def __init__(self, root):
        self.root = root
        self.aj_window = customtkinter.CTkToplevel(root)
        self.aj_window.grab_set()
        self.aj_window.title("Edit Job")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        self.main_frame = customtkinter.CTkFrame(self.aj_window)
        self.main_frame.grid(row=0, column=0, padx=50, pady=50, sticky="nsew")

        self.position_title_entry = customtkinter.CTkEntry(self.main_frame)
        self.position_title_entry.grid(row=0, column=1, padx=(5, 20), pady=2)
        self.position_title_label = customtkinter.CTkLabel(self.main_frame, text='Position')
        self.position_title_label.grid(row=0, column=0, padx=(20, 5), pady=2, sticky="e")

        self.company_name_entry = customtkinter.CTkEntry(self.main_frame)
        self.company_name_entry.grid(row=1, column=1, padx=(5, 20), pady=2)
        self.company_name_label = customtkinter.CTkLabel(self.main_frame, text='Company')
        self.company_name_label.grid(row=1, column=0, padx=(20, 5), pady=2, sticky="e")

        self.company_website_entry = customtkinter.CTkEntry(self.main_frame)
        self.company_website_entry.grid(row=2, column=1, padx=(5, 20), pady=2)
        self.company_website_label = customtkinter.CTkLabel(self.main_frame, text='Website')
        self.company_website_label.grid(row=2, column=0, padx=(20, 5), pady=2, sticky="e")

        self.job_location_entry = customtkinter.CTkEntry(self.main_frame)
        self.job_location_entry.grid(row=3, column=1, padx=(5, 20), pady=2)
        self.job_location_label = customtkinter.CTkLabel(self.main_frame, text='Location')
        self.job_location_label.grid(row=3, column=0, padx=(20, 5), pady=2, sticky="e")

        self.resume_version_entry = customtkinter.CTkEntry(self.main_frame)
        self.resume_version_entry.grid(row=4, column=1, padx=(5, 20), pady=2)
        self.resume_version_label = customtkinter.CTkLabel(self.main_frame, text='Resume Version')
        self.resume_version_label.grid(row=4, column=0, padx=(20, 5), pady=2, sticky="e")

        self.salary_top_entry = customtkinter.CTkEntry(self.main_frame)
        self.salary_top_entry.grid(row=5, column=1, padx=(5, 20), pady=2)
        self.salary_top_label = customtkinter.CTkLabel(self.main_frame, text='Salary Top-End')
        self.salary_top_label.grid(row=5, column=0, padx=(20, 5), pady=2, sticky="e")

        self.salary_bottom_entry = customtkinter.CTkEntry(self.main_frame)
        self.salary_bottom_entry.grid(row=6, column=1, padx=(5, 20), pady=2)
        self.salary_bottom_label = customtkinter.CTkLabel(self.main_frame, text='Salary Bottom-End')
        self.salary_bottom_label.grid(row=6, column=0, padx=(20, 5), pady=2, sticky="e")

        self.salary_type_entry = customtkinter.CTkComboBox(self.main_frame,
                                                           values=['Annual', 'Monthly', 'Hourly', 'Contract', 'None'])
        self.salary_type_entry.grid(row=7, column=1, padx=(5, 20), pady=2)
        self.salary_type_label = customtkinter.CTkLabel(self.main_frame, text='Salary Type')
        self.salary_type_label.grid(row=7, column=0, padx=(20, 5), pady=2, sticky="e")

        self.location_type_entry = customtkinter.CTkComboBox(self.main_frame,
                                                             values=['Remote', 'Hybrid', 'Onsite', 'None'])
        self.location_type_entry.grid(row=8, column=1, padx=(5, 20), pady=2)
        self.location_type_label = customtkinter.CTkLabel(self.main_frame,
                                                          text='Work Type')
        self.location_type_label.grid(row=8, column=0, padx=(20, 5), pady=2, sticky="e")

        self.job_type_entry = customtkinter.CTkComboBox(self.main_frame,
                                                        values=['Full-Time', 'Part-Time', 'Contract', 'Freelance',
                                                                'None'])
        self.job_type_entry.grid(row=9, column=1, padx=(5, 20), pady=2)
        self.job_type_label = customtkinter.CTkLabel(self.main_frame,
                                                     text='Commitment')
        self.job_type_label.grid(row=9, column=0, padx=(20, 5), pady=2, sticky="e")



        # self.job_description_textbox = customtkinter.CTkTextbox(self.main_frame)
        # self.job_description_textbox.grid(row=11, column=0, columnspan=2, sticky='ew')
        self.job_frame = customtkinter.CTkFrame(self.aj_window)
        self.job_frame.grid(row=1,column=0)
        self.job_description_label = customtkinter.CTkLabel(self.job_frame, text='Job Description')
        self.job_description_label.grid(row=0, column=0)

        self.job_description_scroll = customtkinter.CTkScrollableFrame(self.job_frame, width=702,
                                                                       height=300)
        self.job_description_scroll.grid(row=1, column=0, padx=10, pady=10)
        self.job_description_label_edit = customtkinter.CTkLabel(self.job_description_scroll, wraplength=700)
        self.job_description_label_edit.grid(row=0, column=0)


