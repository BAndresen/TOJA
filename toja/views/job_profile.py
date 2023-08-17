import customtkinter
from CTkListbox.ctk_listbox import CTkListbox


class JobProfile:
    def __init__(self, root):
        self.root = root
        self.jp_window = customtkinter.CTkToplevel(root)

        self.jp_window.grab_set()
        self.jp_window.title("Job")

        # job_profile
        self.jp_frame = customtkinter.CTkFrame(self.jp_window)
        self.jp_frame.grid(row=0, column=0, padx=20, pady=20)
        # company website
        self.company_frame = customtkinter.CTkFrame(self.jp_frame)
        self.company_frame.grid(row=0, column=0, padx=20, pady=20)
        self.company_name = customtkinter.CTkLabel(self.company_frame, text="Company")
        self.company_name.grid(row=0, column=0, padx=20, pady=10)
        self.company_name_user = customtkinter.CTkLabel(self.company_frame, text='')
        self.company_name_user.grid(row=0, column=1, padx=10)
        self.company_web = customtkinter.CTkLabel(self.company_frame, text="Website")
        self.company_web.grid(row=1, column=0, padx=20, pady=10)
        self.company_web_user = customtkinter.CTkLabel(self.company_frame, text='')
        self.company_web_user.grid(row=1, column=1, padx=20, pady=10)

        # job info
        self.job_info_frame = customtkinter.CTkFrame(self.jp_frame)
        self.job_info_frame.grid(row=1, column=0, padx=20, pady=20)
        self.position = customtkinter.CTkLabel(self.job_info_frame, text="Position")
        self.position.grid(row=0, column=0, padx=20, pady=10)
        self.position_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.position_user.grid(row=0, column=1, padx=20, pady=10)

        self.location = customtkinter.CTkLabel(self.job_info_frame, text="Location")
        self.location.grid(row=1, column=0, padx=20, pady=10)
        self.location_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.location_user.grid(row=1, column=1, padx=20, pady=10)

        self.commitment = customtkinter.CTkLabel(self.job_info_frame, text="Commitment")
        self.commitment.grid(row=2, column=0, padx=20, pady=10)
        self.commitment_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.commitment_user.grid(row=2, column=1, padx=20, pady=10)

        self.work_type = customtkinter.CTkLabel(self.job_info_frame, text="Work Type")
        self.work_type.grid(row=3, column=0, padx=20, pady=10)
        self.work_type_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.work_type_user.grid(row=3, column=1, padx=20, pady=10)

        self.salary_top = customtkinter.CTkLabel(self.job_info_frame, text="Salary Top")
        self.salary_top.grid(row=4, column=0, padx=20, pady=10)
        self.salary_top_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.salary_top_user.grid(row=4, column=1, padx=20, pady=10)

        self.salary_bottom = customtkinter.CTkLabel(self.job_info_frame, text="Salary Bottom")
        self.salary_bottom.grid(row=5, column=0, padx=20, pady=10)
        self.salary_bottom_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.salary_bottom_user.grid(row=5, column=1, padx=20, pady=10)

        self.salary_type = customtkinter.CTkLabel(self.job_info_frame, text="Salary Type")
        self.salary_type.grid(row=6, column=0, padx=20, pady=10)
        self.salary_type_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.salary_type_user.grid(row=6, column=1, padx=20, pady=10)

        # contact
        self.contact_frame = customtkinter.CTkFrame(self.jp_frame)
        self.contact_frame.grid(row=1, column=2)
        self.contact_label = customtkinter.CTkLabel(self.contact_frame, text="Contacts")
        self.contact_label.grid(row=0, column=0, padx=20, pady=20)

        # keywords
        self.keyword_frame = customtkinter.CTkFrame(self.jp_frame)
        self.keyword_frame.grid(row=0, column=2, rowspan=2, padx=20, pady=20)
        self.keyword_label = customtkinter.CTkLabel(self.keyword_frame, text="Keywords")
        self.keyword_label.grid(row=0, column=0, padx=20, pady=20)

        # description
        self.job_tabview = customtkinter.CTkTabview(self.jp_frame, width=400)
        self.job_tabview.grid(row=4, column=0, columnspan=3, padx=20, pady=20)
        self.job_tabview.add("Description")
        self.job_tabview.add("Event")
        self.job_description_label = customtkinter.CTkLabel(self.job_tabview.tab("Description"), text="Description")
        self.job_description_label.grid(row=0, column=0)

        self.event_label = CTkListbox(self.job_tabview.tab("Event"))
        self.event_label.grid(row=0, column=0)

        # buttons
        self.update_button = customtkinter.CTkButton(self.jp_frame, text="Update")
        self.update_button.grid(row=2, column=2, pady=5)
        self.delete_button = customtkinter.CTkButton(self.jp_frame, text="Delete")
        self.delete_button.grid(row=3, column=2, pady=5)