import customtkinter


class JobDescription:
    def __init__(self, root):
        self.root = root
        self.jd_window = customtkinter.CTkToplevel(root)

        self.jd_window.grab_set()
        self.jd_window.title("Job Description")

        # job_profile
        self.jd_frame = customtkinter.CTkFrame(self.jd_window)
        self.jd_frame.grid(row=0, column=0, padx=20, pady=20)
        self.job_description_label = customtkinter.CTkLabel(self.jd_frame, text='Job Description')
        self.job_description_label.grid(row=0, column=0)

        self.job_description_textbox_only = customtkinter.CTkTextbox(self.jd_frame)
        self.job_description_textbox_only.grid(row=1, column=0, columnspan=2, sticky='ew')

        self.submit_job_description = customtkinter.CTkButton(self.jd_window, text="Submit")
        self.submit_job_description.grid(row=1, column=0, pady=5, padx=10)