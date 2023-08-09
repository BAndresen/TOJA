import tkinter


class JobInputs:
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


class JobDescriptionUI(tkinter.Tk):
    def __init__(self, job_file_path:str, job_file_name:str):
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
