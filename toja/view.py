import customtkinter
from CTkListbox.ctk_listbox import CTkListbox


class HomeView(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure Window
        self.frame = "home"
        self.title("Track and Optimize your Job Application Process")
        self.geometry('1200x650')
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Right Side Navigation Frame
        self.navigation_frame = customtkinter.CTkFrame(self, fg_color="black")
        self.navigation_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   anchor="w")
        self.home_button.grid(row=0, column=0)

        self.analytics_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                        border_spacing=10,
                                                        text="Analytics",
                                                        fg_color="transparent", text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),
                                                        anchor="w")
        self.analytics_button.grid(row=1, column=0)

        self.events_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                     border_spacing=10,
                                                     text="Events",
                                                     fg_color="transparent", text_color=("gray10", "gray90"),
                                                     hover_color=("gray70", "gray30"),
                                                     anchor="w")
        self.events_button.grid(row=2, column=0)

        # Home Frame
        self.home_frame = customtkinter.CTkFrame(self)
        self.home_frame.grid(row=0, column=1, sticky="nsew")
        self.home_frame.grid_columnconfigure(0, weight=1)

        # Job ListBox
        self.job_list_box = CTkListbox(self.home_frame)
        self.job_list_box.grid(row=0, column=0, rowspan=2, padx=20, pady=20, sticky='nsew')

        # Motivational Stats Board
        self.stat_board_frame = customtkinter.CTkFrame(self.home_frame)
        self.stat_board_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.stat_label = customtkinter.CTkLabel(self.stat_board_frame, text="motivational design stats")
        self.stat_label.grid(row=0, column=0, padx=150, pady=150)

        # Graph - Days vs Events
        self.calendar_frame = customtkinter.CTkFrame(self.home_frame)
        self.calendar_frame.grid(row=2, columnspan=2, column=0, padx=20, pady=20, sticky="nsew")
        self.calendar_label_placeholder = (customtkinter.CTkLabel(
            self.calendar_frame, text="graph - days vs events"))
        self.calendar_label_placeholder.grid(row=0, column=1, padx=50, pady=50)

        # Add New Job Button
        self.button_frame = customtkinter.CTkFrame(self.home_frame)
        self.button_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        self.new_job_button = customtkinter.CTkButton(self.button_frame, text="Add")
        self.new_job_button.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        # --------------- Event -------------- #

        self.event_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.event_frame.grid_columnconfigure(0, weight=1)

        # Recent Events
        self.recent_events_frame = customtkinter.CTkFrame(self.event_frame)
        self.recent_events_frame.grid_columnconfigure(0, weight=1)
        self.recent_events_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.recent_events_label = customtkinter.CTkLabel(self.recent_events_frame, text="Recent Events")
        self.recent_events_label.grid(row=0, column=0)
        self.recent_events_listbox = CTkListbox(self.recent_events_frame)
        self.recent_events_listbox.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        # Upcoming Events
        self.upcoming_events_frame = customtkinter.CTkFrame(self.event_frame)
        self.upcoming_events_frame.grid_columnconfigure(0, weight=1)

        self.upcoming_events_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.upcoming_events_label = customtkinter.CTkLabel(self.upcoming_events_frame, text="Recent Events")
        self.upcoming_events_label.grid(row=0, column=0)
        self.upcoming_events_listbox = CTkListbox(self.upcoming_events_frame)
        self.upcoming_events_listbox.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        # --------------- Analytics -------------- #

        self.analytics_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.analytics_frame.grid_columnconfigure(0, weight=1)

        # Keywords
        self.keywords_frame = customtkinter.CTkFrame(self.analytics_frame)
        self.keywords_frame.grid_columnconfigure(0, weight=1)
        self.keywords_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.keywords_label = customtkinter.CTkLabel(self.keywords_frame, text="Keywords")
        self.keywords_label.grid(row=0, column=0)

        # Resume
        self.resume_frame = customtkinter.CTkFrame(self.analytics_frame)
        self.resume_frame.grid_columnconfigure(0, weight=1)
        self.resume_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.resume_label = customtkinter.CTkLabel(self.resume_frame, text="Resume")
        self.resume_label.grid(row=0, column=0)


class NewJob:
    def __init__(self, root):
        self.root = root
        self.aj_window = customtkinter.CTkToplevel(root)
        self.aj_window.grab_set()
        # self.title("Add Job")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        self.main_frame = customtkinter.CTkFrame(self.aj_window)
        self.main_frame.grid(row=0, column=1, padx=50, pady=50, sticky="nsew")

        self.position_title_entry = customtkinter.CTkEntry(self.main_frame)
        self.position_title_entry.grid(row=0, column=1, padx=(5, 20), pady=10)
        self.position_title_label = customtkinter.CTkLabel(self.main_frame, text='Position Title')
        self.position_title_label.grid(row=0, column=0, padx=(20, 5), pady=10, sticky="e")

        self.company_name_entry = customtkinter.CTkEntry(self.main_frame)
        self.company_name_entry.grid(row=1, column=1, padx=(5, 20), pady=10)
        self.company_name_label = customtkinter.CTkLabel(self.main_frame, text='Company Name')
        self.company_name_label.grid(row=1, column=0, padx=(20, 5), pady=10, sticky="e")

        self.job_location_entry = customtkinter.CTkEntry(self.main_frame)
        self.job_location_entry.grid(row=2, column=1, padx=(5, 20), pady=10)
        self.job_location_label = customtkinter.CTkLabel(self.main_frame, text='Job Location')
        self.job_location_label.grid(row=2, column=0, padx=(20, 5), pady=10, sticky="e")

        self.resume_version_entry = customtkinter.CTkEntry(self.main_frame)
        self.resume_version_entry.grid(row=3, column=1, padx=(5, 20), pady=10)
        self.resume_version_label = customtkinter.CTkLabel(self.main_frame, text='Resume Version')
        self.resume_version_label.grid(row=3, column=0, padx=(20, 5), pady=10, sticky="e")

        self.salary_top_entry = customtkinter.CTkEntry(self.main_frame)
        self.salary_top_entry.grid(row=4, column=1, padx=(5, 20), pady=10)
        self.salary_top_label = customtkinter.CTkLabel(self.main_frame, text='Salary Top-End Range')
        self.salary_top_label.grid(row=4, column=0, padx=(20, 5), pady=10, sticky="e")

        self.salary_bottom_entry = customtkinter.CTkEntry(self.main_frame)
        self.salary_bottom_entry.grid(row=5, column=1, padx=(5, 20), pady=10)
        self.salary_bottom_label = customtkinter.CTkLabel(self.main_frame, text='Salary Bottom-End Range')
        self.salary_bottom_label.grid(row=5, column=0, padx=(20, 5), pady=10, sticky="e")

        self.app_platform_entry = customtkinter.CTkEntry(self.main_frame)
        self.app_platform_entry.grid(row=6, column=1, padx=(5, 20), pady=10)
        self.app_platform_label = customtkinter.CTkLabel(self.main_frame, text='Application Platform')
        self.app_platform_label.grid(row=6, column=0, padx=(20, 5), pady=10, sticky="e")

        self.location_type_entry = customtkinter.CTkEntry(self.main_frame)
        self.location_type_entry.grid(row=7, column=1, padx=(5, 20), pady=10)
        self.location_type_label = customtkinter.CTkLabel(self.main_frame,
                                                          text='Location Type (remote,hybrid,onsite)')
        self.location_type_label.grid(row=7, column=0, padx=(20, 5), pady=10, sticky="e")

        self.job_type_entry = customtkinter.CTkEntry(self.main_frame)
        self.job_type_entry.grid(row=9, column=1, padx=(5, 20), pady=10)
        self.job_type_label = customtkinter.CTkLabel(self.main_frame,
                                                     text='Job Type (full-time, part-time, contract, freelance)')
        self.job_type_label.grid(row=9, column=0, padx=(20, 5), pady=10, sticky="e")

        self.job_description_label = customtkinter.CTkLabel(self.main_frame, text='Job Description')
        self.job_description_label.grid(row=10, column=0)

        self.job_description = customtkinter.CTkTextbox(self.main_frame)
        self.job_description.grid(row=11, column=0, columnspan=2, sticky='ew')

        self.submit_button = customtkinter.CTkButton(self.main_frame, text="Submit")
        self.submit_button.grid(row=12, column=1, padx=20, pady=20)


class JobProfile:
    def __init__(self, root, job_id):
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
        self.company_name = customtkinter.CTkLabel(self.company_frame, text="Company Name")
        self.company_name.grid(row=0, column=0,padx=20, pady=10)
        self.company_web = customtkinter.CTkLabel(self.company_frame, text="Website")
        self.company_web.grid(row=1, column=0,padx=20, pady=10)

        # job info
        self.job_info_frame = customtkinter.CTkFrame(self.jp_frame)
        self.job_info_frame.grid(row=1, column=0, padx=20, pady=20)
        self.position = customtkinter.CTkLabel(self.job_info_frame, text="Position")
        self.position.grid(row=0, column=0,padx=20, pady=10)
        self.work_type = customtkinter.CTkLabel(self.job_info_frame, text="Work Type")
        self.work_type.grid(row=1, column=0,padx=20, pady=10)
        self.location = customtkinter.CTkLabel(self.job_info_frame, text="Location")
        self.location.grid(row=2, column=0,padx=20, pady=10)
        self.salary_top = customtkinter.CTkLabel(self.job_info_frame, text="Salary Top")
        self.salary_top.grid(row=3, column=0,padx=20, pady=10)
        self.salary_bottom = customtkinter.CTkLabel(self.job_info_frame, text="Salary Bottom")
        self.salary_bottom.grid(row=4, column=0,padx=20, pady=10)
        self.salary_type = customtkinter.CTkLabel(self.job_info_frame, text="Salary Type")
        self.salary_type.grid(row=5, column=0,padx=20, pady=10)

        # contact
        self.contact_frame = customtkinter.CTkFrame(self.jp_frame)
        self.contact_frame.grid(row=1, column=2)
        self.contact_label = customtkinter.CTkLabel(self.contact_frame, text="Contacts")
        self.contact_label.grid(row=0, column=0, padx=20, pady=20)

        # keywords
        self.keyword_frame = customtkinter.CTkFrame(self.jp_frame)
        self.keyword_frame.grid(row=0, column=2,rowspan=2, padx=20, pady=20)
        self.keyword_label = customtkinter.CTkLabel(self.keyword_frame, text="Keywords")
        self.keyword_label.grid(row=0, column=0, padx=20, pady=20)

        # description
        self.job_tabview = customtkinter.CTkTabview(self.jp_frame, width=400)
        self.job_tabview.grid(row=4, column=0, columnspan=3, padx=20, pady=20)
        self.job_tabview.add("Description")
        self.job_tabview.add("Event")
        self.job_description_label = customtkinter.CTkLabel(self.job_tabview.tab("Description"), text="Description")
        self.job_description_label.grid(row=0, column=0)

        self.event_label = customtkinter.CTkLabel(self.job_tabview.tab("Event"), text="Events")
        self.event_label.grid(row=0, column=0)

        # buttons
        self.update_button = customtkinter.CTkButton(self.jp_frame, text="Update")
        self.update_button.grid(row=2,column=2, pady=5)
        self.delete_button = customtkinter.CTkButton(self.jp_frame, text="Delete")
        self.delete_button.grid(row=3, column=2, pady=5)

        # self.jp_window.mainloop()


