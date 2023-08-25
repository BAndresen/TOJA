import tkinter

import customtkinter
from CTkListbox.ctk_listbox import CTkListbox


class JobProfile:
    def __init__(self, root):
        self.root = root
        self.jp_window = customtkinter.CTkToplevel(root)

        self.jp_window.grab_set()
        self.jp_window.title("Job")

        self.jp_window.grid_columnconfigure(0, weight=1)

        # job_profile
        self.jp_frame = customtkinter.CTkFrame(self.jp_window)
        self.jp_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')
        self.jp_frame.grid_columnconfigure(0, weight=1)
        # company website
        self.company_frame = customtkinter.CTkFrame(self.jp_frame)
        self.company_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        self.company_name = customtkinter.CTkLabel(self.company_frame, text="Company")
        self.company_name.grid(row=0, column=0, padx=20, pady=2)
        self.company_name_user = customtkinter.CTkLabel(self.company_frame, text='')
        self.company_name_user.grid(row=0, column=1, padx=2)
        self.company_web = customtkinter.CTkLabel(self.company_frame, text="Website")
        self.company_web.grid(row=1, column=0, padx=20, pady=2)
        self.company_web_user = customtkinter.CTkLabel(self.company_frame, text='')
        self.company_web_user.grid(row=1, column=1, padx=20, pady=2)

        # job info
        self.job_info_frame = customtkinter.CTkFrame(self.jp_frame)
        self.job_info_frame.grid(row=1, column=0, padx=20, pady=20)
        self.position = customtkinter.CTkLabel(self.job_info_frame, text="Position")
        self.position.grid(row=0, column=0, padx=20, pady=2)
        self.position_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.position_user.grid(row=0, column=1, padx=20, pady=2)

        self.location = customtkinter.CTkLabel(self.job_info_frame, text="Location")
        self.location.grid(row=1, column=0, padx=20, pady=2)
        self.location_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.location_user.grid(row=1, column=1, padx=20, pady=2)

        self.commitment = customtkinter.CTkLabel(self.job_info_frame, text="Commitment")
        self.commitment.grid(row=2, column=0, padx=20, pady=2)
        self.commitment_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.commitment_user.grid(row=2, column=1, padx=20, pady=2)

        self.work_type = customtkinter.CTkLabel(self.job_info_frame, text="Work Type")
        self.work_type.grid(row=3, column=0, padx=20, pady=2)
        self.work_type_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.work_type_user.grid(row=3, column=1, padx=20, pady=2)

        self.salary_top = customtkinter.CTkLabel(self.job_info_frame, text="Salary Top")
        self.salary_top.grid(row=4, column=0, padx=20, pady=2)
        self.salary_top_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.salary_top_user.grid(row=4, column=1, padx=20, pady=2)

        self.salary_bottom = customtkinter.CTkLabel(self.job_info_frame, text="Salary Bottom")
        self.salary_bottom.grid(row=5, column=0, padx=20, pady=2)
        self.salary_bottom_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.salary_bottom_user.grid(row=5, column=1, padx=20, pady=2)

        self.salary_type = customtkinter.CTkLabel(self.job_info_frame, text="Salary Type")
        self.salary_type.grid(row=6, column=0, padx=20, pady=2)
        self.salary_type_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.salary_type_user.grid(row=6, column=1, padx=20, pady=2)

        self.resume = customtkinter.CTkLabel(self.job_info_frame, text="Resume Version")
        self.resume.grid(row=7, column=0, padx=20, pady=2)
        self.resume_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.resume_user.grid(row=7, column=1, padx=20, pady=2)

        # buttons
        self.button_frame = customtkinter.CTkFrame(self.jp_frame)
        self.button_frame.grid(row=1, column=1)
        self.edit_button = customtkinter.CTkButton(self.button_frame, text="Edit")
        self.edit_button.grid(row=1, column=1, pady=5, padx=10)
        self.delete_button = customtkinter.CTkButton(self.button_frame, text="Delete")
        self.delete_button.grid(row=2, column=1, pady=5, padx=10)
        self.new_contact_button = customtkinter.CTkButton(self.button_frame, text="New Contact")
        self.new_contact_button.grid(row=3, column=1, pady=5, padx=10)
        self.new_event_button = customtkinter.CTkButton(self.button_frame, text="New Event")
        self.new_event_button.grid(row=4, column=1, pady=5, padx=10)
        self.edit_job_button = customtkinter.CTkButton(self.button_frame, text="Edit Job Description")
        self.edit_job_button.grid(row=5, column=1, pady=5, padx=10)

        # description
        self.job_tabview = customtkinter.CTkTabview(self.jp_frame, width=500)
        self.job_tabview.grid(row=4, column=0, columnspan=3, padx=20, pady=20)
        self.job_tabview.add("Description")
        self.job_tabview.add("Events")
        self.job_tabview.add('Contacts')
        self.job_tabview.add('Key Words')

        self.job_description_scroll = customtkinter.CTkScrollableFrame(self.job_tabview.tab('Description'), width=701,
                                                                       height=300)
        self.event_scroll = tkinter.Listbox(self.job_tabview.tab('Events'), width=103, height=19,font=('roboto, 10'), bg='grey20', fg='grey90', borderwidth=0)
        self.event_scroll.grid(row=0, column=0,padx=10, pady=10)
        self.job_description_scroll.grid(row=0, column=0, padx=10, pady=10)
        self.job_description_label = customtkinter.CTkLabel(self.job_description_scroll, wraplength=700)
        self.job_description_label.grid(row=0, column=0)

        self.contact_listbox = tkinter.Listbox(self.job_tabview.tab('Contacts'), width=103, height=19,font=('roboto, 10'), bg='grey20', fg='grey90', borderwidth=0)
        self.contact_listbox.grid(row=0, column=0, padx=10, pady=10)
        self.keyword_scroll = customtkinter.CTkScrollableFrame(self.job_tabview.tab('Key Words'), width=702,
                                                                       height=300)
        self.keyword_scroll.grid(row=0, column=0, padx=10, pady=10)

