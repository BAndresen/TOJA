import tkinter
import customtkinter
import os
from PIL import Image


class JobProfile:
    def __init__(self, root):
        self.root = root
        self.jp_window = customtkinter.CTkToplevel(root)

        self.jp_window.grab_set()
        self.jp_window.title("Job")

        self.jp_window.grid_columnconfigure(0, weight=1)

        icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons")
        pencil_white = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "pencil_white.png")),
                                           size=(17, 17))
        writing_white = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "writing_white.png")),
                                           size=(20, 20))
        add_event_white = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "add_event_white.png")),
                                           size=(20, 20))
        contact_white = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "contact_white.png")),
                                           size=(20, 20))

        # job_profile
        self.jp_frame = customtkinter.CTkFrame(self.jp_window)
        self.jp_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')
        self.jp_frame.grid_columnconfigure(0, weight=1)

        self.jp_all_frame = customtkinter.CTkFrame(self.jp_frame)
        self.jp_all_frame.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        # company website
        self.company_frame = customtkinter.CTkFrame(self.jp_all_frame)
        self.company_frame.grid(row=0, column=0, columnspan=2, padx=(20,5), pady=20, sticky='nsew')
        self.company_name = customtkinter.CTkLabel(self.company_frame, text="Company:")
        self.company_name.grid(row=0, column=0, padx=5, pady=2,sticky='e')
        self.company_name_user = customtkinter.CTkLabel(self.company_frame, text='')
        self.company_name_user.grid(row=0, column=1, padx=5, sticky='w')
        self.company_web = customtkinter.CTkLabel(self.company_frame, text="Website:")
        self.company_web.grid(row=1, column=0, padx=5, pady=2, sticky='e')
        self.company_web_user = customtkinter.CTkLabel(self.company_frame, text='')
        self.company_web_user.grid(row=1, column=1, padx=5, pady=2, sticky='w')

        # job info
        self.job_info_frame = customtkinter.CTkFrame(self.jp_all_frame)
        self.job_info_frame.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')
        self.job_id = customtkinter.CTkLabel(self.job_info_frame, text="job_id:")
        self.job_id.grid(row=0, column=0, padx=5, pady=2, stick='e')
        self.job_id_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.job_id_user.grid(row=0, column=1, padx=5, pady=2, stick='w')
        self.position = customtkinter.CTkLabel(self.job_info_frame, text="Position:")
        self.position.grid(row=1, column=0, padx=5, pady=2, stick='e')
        self.position_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.position_user.grid(row=1, column=1, padx=5, pady=2, stick='w')

        self.location = customtkinter.CTkLabel(self.job_info_frame, text="Location:")
        self.location.grid(row=2, column=0, padx=5, pady=2, stick='e')
        self.location_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.location_user.grid(row=2, column=1, padx=5, pady=2, stick='w')

        self.commitment = customtkinter.CTkLabel(self.job_info_frame, text="Commitment:")
        self.commitment.grid(row=3, column=0, padx=5, pady=2, stick='e')
        self.commitment_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.commitment_user.grid(row=3, column=1, padx=5, pady=2, stick='w')

        self.work_type = customtkinter.CTkLabel(self.job_info_frame, text="Work Type:")
        self.work_type.grid(row=4, column=0, padx=5, pady=2, stick='e')
        self.work_type_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.work_type_user.grid(row=4, column=1, padx=5, pady=2, stick='w')

        self.salary_top = customtkinter.CTkLabel(self.job_info_frame, text="Salary Top:")
        self.salary_top.grid(row=5, column=0, padx=5, pady=2, stick='e')
        self.salary_top_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.salary_top_user.grid(row=5, column=1, padx=5, pady=2, stick='w')

        self.salary_bottom = customtkinter.CTkLabel(self.job_info_frame, text="Salary Bottom:")
        self.salary_bottom.grid(row=6, column=0, padx=5, pady=2, stick='e')
        self.salary_bottom_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.salary_bottom_user.grid(row=6, column=1, padx=5, pady=2, stick='w')

        self.salary_type = customtkinter.CTkLabel(self.job_info_frame, text="Salary Type:")
        self.salary_type.grid(row=7, column=0, padx=5, pady=2, stick='e')
        self.salary_type_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.salary_type_user.grid(row=7, column=1, padx=5, pady=2, stick='w')

        self.resume = customtkinter.CTkLabel(self.job_info_frame, text="Resume Version:")
        self.resume.grid(row=8, column=0, padx=5, pady=2, stick='e')
        self.resume_user = customtkinter.CTkLabel(self.job_info_frame, text='')
        self.resume_user.grid(row=8, column=1, padx=5, pady=2, stick='w')

        # buttons
        self.button_frame = customtkinter.CTkFrame(self.jp_frame)
        self.button_frame.grid(row=2, column=3, sticky="n", pady=38)
        self.edit_button = customtkinter.CTkButton(self.jp_all_frame, text="",image=pencil_white, width=35, height=35,
                                                   fg_color='grey30', hover_color='grey15')
        self.edit_button.grid(row=0, column=2, padx=10, sticky='e')

        self.new_contact_button = customtkinter.CTkButton(self.button_frame, text="", image=contact_white, width=35,
                                                       height=35,
                                                       fg_color='grey30', hover_color='grey15')
        self.new_contact_button.grid(row=2, column=0, pady=5, padx=10)
        self.new_event_button = customtkinter.CTkButton(self.button_frame, text="",  image=add_event_white, width=35,
                                                       height=35,
                                                       fg_color='grey30', hover_color='grey15')
        self.new_event_button.grid(row=1, column=0, pady=5, padx=10)
        self.edit_job_button = customtkinter.CTkButton(self.button_frame, text="", image=writing_white, width=35,
                                                       height=35,
                                                       fg_color='grey30', hover_color='grey15')
        self.edit_job_button.grid(row=0, column=0, pady=5, padx=10)


        # description
        self.job_tabview = customtkinter.CTkTabview(self.jp_frame, width=500)
        self.job_tabview.grid(row=2, column=0, columnspan=3, padx=(20,5), pady=20)
        self.job_tabview.add("Description")
        self.job_tabview.add("Events")
        self.job_tabview.add('Contacts')
        self.job_tabview.add('Key Words')

        self.job_description_scroll = customtkinter.CTkScrollableFrame(self.job_tabview.tab('Description'), width=701,
                                                                       height=300)

        self.event_scroll = tkinter.Listbox(self.job_tabview.tab('Events'), width=103, height=19, font=('roboto, 10'),
                                            bg='grey20', fg='grey90', borderwidth=0)
        self.event_scroll.grid(row=0, column=0, padx=10, pady=10)
        self.job_description_scroll.grid(row=0, column=0, padx=10, pady=10)
        self.job_description_label = customtkinter.CTkLabel(self.job_description_scroll, wraplength=700, justify='left')
        self.job_description_label.grid(row=0, column=0)

        self.contact_listbox = tkinter.Listbox(self.job_tabview.tab('Contacts'), width=103, height=19,
                                               font=('roboto, 10'), bg='grey20', fg='grey90', borderwidth=0)
        self.contact_listbox.grid(row=0, column=0, padx=10, pady=10)
        self.keyword_scroll = customtkinter.CTkScrollableFrame(self.job_tabview.tab('Key Words'), width=701,
                                                               height=300)
        self.keyword_scroll.grid(row=0, column=0, padx=10, pady=10)
