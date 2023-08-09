import tkinter
import customtkinter


class HomeWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # self.minsize(width=1000, height=700)
        self.title("Track and Optimize your Job Application Process")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.stat_board_frame = customtkinter.CTkFrame(self)
        self.stat_board_frame.grid(row=0, rowspan=2, column=1, padx=20, pady=20, sticky="nsew")

        self.stat_label = customtkinter.CTkLabel(self.stat_board_frame, text="stat board placeholder")
        self.stat_label.grid(row=0, column=0, padx=150, pady=150)

        self.calendar_frame = customtkinter.CTkFrame(self)
        self.calendar_frame.grid(row=2, columnspan=2, column=0, padx=20, pady=20, sticky="nsew")
        self.calendar_label_placeholder = (customtkinter.CTkLabel(
            self.calendar_frame, text="calendar placeholder"))
        self.calendar_label_placeholder.grid(row=0, column=0, padx=50, pady=50)

        self.button_frame = customtkinter.CTkFrame(self)
        self.button_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        self.new_job_button = customtkinter.CTkButton(self.button_frame, text="Add")
        self.new_job_button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.new_job_button = customtkinter.CTkButton(self.button_frame, text="Update")
        self.new_job_button.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        self.new_job_button = customtkinter.CTkButton(self.button_frame, text="Analyze")
        self.new_job_button.grid(row=1, column=2, padx=20, pady=20, sticky="nsew")

        self.mainloop()


class NewJobInputs:
    def __init__(self):
        print('\nEnter Application Details Below or Leave Blank\n')
        self.position_title = input('Enter the Position Title: ').lower()
        self.company = input('Enter the Company Name: ').lower()
        self.job_location = input('Enter the Job Location: ').lower()
        try:
            self.resume_version = float(input('Enter the Resume Version: '))
        except ValueError:
            self.resume_version = None
        try:
            self.salary_top = int(input('Enter the Salary Top-End Range: '))
        except ValueError:
            self.salary_top = None
        try:
            self.salary_bottom = int(input('Enter the Salary Bottom-End Range: '))
        except ValueError:
            self.salary_bottom = None
        self.application_platform = input('Enter the Application Platform: ').lower()
        self.work_type = input('Location Type (remote,hybrid,onsite): ').lower()
        self.job_type = input('Job Type (full-time, part-time, contract, freelance): ').lower()

        self._check_null()

    def _check_null(self):
        """Convert empty strings to NULL"""
        if self.position_title == "":
            self.position_title = None
        if self.company == "":
            self.company = None
        if self.job_location == "":
            self.job_location = None
        if self.application_platform == "":
            self.application_platform = None
        if self.work_type == "":
            self.work_type = None
        if self.job_type == "":
            self.job_type = None


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
