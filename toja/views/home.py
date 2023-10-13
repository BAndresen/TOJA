import tkinter
import customtkinter
from tkinter import Menu
import os
from PIL import Image


class HomeView(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # image icons
        icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons")
        plus_icon = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "plus_thin_white.png")),
                                           size=(20, 20))
        delete_icon = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "delete_white.png")),
                                             size=(22, 22))

        # Configure Window
        self.frame = "home"
        self.title("Track and Optimize your Job Application Process")
        self.geometry('1200x750')
        self.grid_columnconfigure(1, weight=4)
        self.grid_rowconfigure(0, weight=1)

        # Right Side Navigation Frame
        self.navigation_frame = customtkinter.CTkFrame(self, fg_color='gray10')
        self.navigation_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   anchor="w")
        self.home_button.grid(row=0, column=0, pady=(50, 0))

        self.analytics_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                        border_spacing=10,
                                                        text="Keywords",
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

        self.network_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10,
                                                      text="Network",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w")
        self.network_button.grid(row=3, column=0)

        # Home Frame
        self.home_frame = customtkinter.CTkFrame(self)
        self.home_frame.grid(row=0, column=1, sticky="nsew")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(0, weight=1)

        self.job_list_frame = customtkinter.CTkFrame(self.home_frame)
        self.job_list_frame.grid(row=0, column=0, rowspan=2, padx=20, pady=20, sticky="nsew")
        self.job_list_frame.grid_columnconfigure(0, weight=1)
        self.job_list_frame.grid_rowconfigure(0, weight=1)
        # Job ListBox
        self.job_list_box = tkinter.Listbox(self.job_list_frame, font=('roboto, 10'), bg='grey20', fg='grey90',
                                            borderwidth=0, height=20)

        self.job_list_box.grid(row=0, column=0, rowspan=2, padx=(20, 5), pady=20, sticky='nsew')

        # Add and Delete Job Button
        self.button_frame = customtkinter.CTkFrame(self.job_list_frame)
        self.button_frame.grid(row=0, column=1, padx=(5, 20), pady=20, sticky="ne")
        self.new_job_button = customtkinter.CTkButton(self.button_frame, text="", image=plus_icon, width=35, height=35,
                                                      fg_color='grey30', hover_color='grey15')
        self.new_job_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="nsew")
        self.delete_job_button = customtkinter.CTkButton(self.button_frame, text="", image=delete_icon, width=35,
                                                         height=35,
                                                         fg_color='grey30', hover_color='grey15')
        self.delete_job_button.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="nsew")

        # Motivational Stats Board
        self.stat_board_frame = customtkinter.CTkFrame(self.home_frame)
        self.stat_board_frame.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")

        self.total_points_label = customtkinter.CTkLabel(self.stat_board_frame, text="Total Points:")
        self.total_points_label.grid(row=0, column=0, padx=(20, 5), pady=(20, 5), sticky="e")
        self.total_points = customtkinter.CTkLabel(self.stat_board_frame, text="")
        self.total_points.grid(row=0, column=1, padx=(5, 20), pady=(20, 5), sticky="w")

        self.next_level = customtkinter.CTkLabel(self.stat_board_frame, text="Next Level")
        self.next_level.grid(row=1, column=0, padx=(20, 5), pady=5, sticky="e")
        self.progress_bar = customtkinter.CTkProgressBar(self.stat_board_frame)
        self.progress_bar.grid(row=1, column=1, padx=(5, 20), pady=5, sticky="ew")

        self.current_level_label = customtkinter.CTkLabel(self.stat_board_frame, text="Job Hunter Level:")
        self.current_level_label.grid(row=2, column=0, padx=(20, 5), pady=5, sticky="e")
        self.current_level = customtkinter.CTkLabel(self.stat_board_frame, text="")
        self.current_level.grid(row=2, column=1, padx=(5, 20), pady=5, sticky="w")

        # Graph - Days vs Events
        self.calendar_frame = customtkinter.CTkFrame(self.home_frame)
        self.calendar_frame.grid(row=2, columnspan=3, column=0, padx=20, pady=20, sticky="nsew")
        # self.calendar_label_placeholder = (customtkinter.CTkLabel(
        #     self.calendar_frame, text="graph - days vs events (coming soon)"))
        # self.calendar_label_placeholder.grid(row=0, column=1, padx=50, pady=50)

        # --------------- Event -------------- #

        self.event_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.event_frame.grid_columnconfigure(0, weight=1)

        self.event_button_frame = customtkinter.CTkFrame(self.event_frame)
        self.event_button_frame.grid(row=0, column=1, padx=(5, 20), pady=20, sticky="ne")
        self.event_new_button = customtkinter.CTkButton(self.event_button_frame, text="", image=plus_icon, width=35,
                                                        height=35, fg_color='grey30', hover_color='grey15')
        self.event_new_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="nsew")
        self.event_delete_button = customtkinter.CTkButton(self.event_button_frame, text="", image=delete_icon,
                                                           width=35, height=35,
                                                           fg_color='grey30', hover_color='grey15')
        self.event_delete_button.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="nsew")

        # Recent Events
        self.past_events_frame = customtkinter.CTkFrame(self.event_frame)
        self.past_events_frame.grid_columnconfigure(0, weight=1)
        self.past_events_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.past_events_label = customtkinter.CTkLabel(self.past_events_frame, text="Past Events")
        self.past_events_label.grid(row=0, column=0)
        self.past_events_listbox = tkinter.Listbox(self.past_events_frame, font=('roboto, 10'), bg='grey20',
                                                   fg='grey90', borderwidth=0)
        self.past_events_listbox.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)

        # Upcoming Events
        self.upcoming_events_frame = customtkinter.CTkFrame(self.event_frame)
        self.upcoming_events_frame.grid_columnconfigure(0, weight=1)

        self.upcoming_events_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.upcoming_events_label = customtkinter.CTkLabel(self.upcoming_events_frame, text="Upcoming Events")
        self.upcoming_events_label.grid(row=0, column=0)
        self.upcoming_events_listbox = tkinter.Listbox(self.upcoming_events_frame, font=('roboto, 10'), bg='grey20',
                                                       fg='grey90', borderwidth=0)
        self.upcoming_events_listbox.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)

        # --------------- Keywords -------------- #

        self.analytics_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.analytics_frame.grid_columnconfigure(0, weight=1)
        self.analytics_frame.grid_rowconfigure(0, weight=1)

        # Keywords Frames
        self.keywords_frame = customtkinter.CTkFrame(self.analytics_frame)
        self.keywords_frame.grid_columnconfigure(0, weight=1)
        self.keywords_frame.grid_columnconfigure(1, weight=1)
        self.keywords_frame.grid_rowconfigure(1, weight=1)
        self.keywords_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Keyword Title labels
        self.jd_title = customtkinter.CTkLabel(self.keywords_frame, text="Job Description Search")
        self.jd_title.grid(row=0, column=0)
        self.resume_title = customtkinter.CTkLabel(self.keywords_frame, text="Resume Search")
        self.resume_title.grid(row=0, column=1)

        # Job Description search
        self.jd_frame = customtkinter.CTkFrame(self.keywords_frame)
        self.jd_frame.grid(row=1, column=0, padx=50, pady=(5,20), sticky='nsew')
        self.jd_frame.grid_columnconfigure(0, weight=1)
        self.jd_frame.grid_rowconfigure(1, weight=1)

        self.jd_search_button = customtkinter.CTkButton(self.jd_frame, text='Search')
        self.jd_search_button.grid(row=2,column=0, pady=(0,20))

        self.search_jd_frame = customtkinter.CTkFrame(self.jd_frame)
        self.search_jd_frame.grid(row=0, column=0, padx=50, pady=50, sticky='nsew')

        self.search_by_label = customtkinter.CTkLabel(self.search_jd_frame, text="Search By:")
        self.search_by_label.grid(row=0,column=0)
        self.radio_var = tkinter.IntVar(value=0)
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.search_jd_frame, variable=self.radio_var, value=0, text="All")
        self.radio_button_1.grid(row=1, column=0, pady=5, padx=20)
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.search_jd_frame, variable=self.radio_var, value=1, text='Job ID')
        self.radio_button_2.grid(row=2, column=0, pady=5, padx=20)
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.search_jd_frame, variable=self.radio_var, value=2, text='Position')
        self.radio_button_3.grid(row=3, column=0, pady=5, padx=20)

        self.radio_button_1.bind('<Button-1>', self.destroy_entry)
        self.radio_button_2.bind('<Button-1>', self.display_job_id)
        self.radio_button_3.bind('<Button-1>', self.display_position)

        self.job_id_entry = customtkinter.CTkEntry(self.search_jd_frame)
        self.position_entry = customtkinter.CTkEntry(self.search_jd_frame)

        # list box job
        self.jd_search_listbox = tkinter.Listbox(self.jd_frame,
                                                 font=('roboto, 10'),
                                                 bg='grey20',
                                                 fg='grey90',
                                                 borderwidth=0,
                                                 # height=15
                                                 )
        self.jd_search_listbox.grid(row=1, column=0, padx=50, pady=(5, 50), sticky='nsew')

        # Resume search
        self.resume_frame = customtkinter.CTkFrame(self.keywords_frame)
        self.resume_frame.grid(row=1, column=1, padx=50, pady=(5,20), sticky='nsew')
        self.resume_frame.grid_columnconfigure(0, weight=1)
        self.resume_frame.grid_rowconfigure(1, weight=1)

        self.resume_search_button = customtkinter.CTkButton(self.resume_frame, text='Search')
        self.resume_search_button.grid(row=2,column=0, pady=(0,20))

        self.search_resume_frame = customtkinter.CTkFrame(self.resume_frame)
        self.search_resume_frame.grid(row=0, column=0, padx=50, pady=50, sticky='nsew')

        self.upload_resume = customtkinter.CTkLabel(self.search_resume_frame, text='Upload Resume')
        self.upload_resume.grid(row=0, column=0, padx=10, pady=(10,0))
        self.resume_browse_button = customtkinter.CTkButton(self.search_resume_frame, text='Browse')
        self.resume_browse_button.grid(row=1, column=0, padx=10, pady=(0,10))

        self.resume_score_label = customtkinter.CTkLabel(self.search_resume_frame, text='Resume Score:')
        self.resume_score_label.grid(row=2, column=0)
        self.resume_score = customtkinter.CTkLabel(self.search_resume_frame, text='')
        self.resume_score.grid(row=2, column=1)


        # list box resume
        self.resume_search_listbox = tkinter.Listbox(self.resume_frame,
                                                 font=('roboto, 10'),
                                                 bg='grey20',
                                                 fg='grey90',
                                                 borderwidth=0,
                                                 # height=15
                                                 )
        self.resume_search_listbox.grid(row=1, column=0, padx=50, pady=(5, 50), sticky='nsew')

        # --------------- Network -------------- #

        self.network_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.network_frame.grid_columnconfigure(0, weight=1)

        self.network_button_frame = customtkinter.CTkFrame(self.network_frame)
        self.network_button_frame.grid(row=0, column=1, padx=(5, 20), pady=20, sticky="ne")
        self.network_new_contact_button = customtkinter.CTkButton(self.network_button_frame, text="", image=plus_icon,
                                                                  width=35, height=35, fg_color='grey30',
                                                                  hover_color='grey15')
        self.network_new_contact_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="nsew")
        self.network_delete_job_button = customtkinter.CTkButton(self.network_button_frame, text="", image=delete_icon,
                                                                 width=35, height=35,
                                                                 fg_color='grey30', hover_color='grey15')
        self.network_delete_job_button.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="nsew")

        self.contacts_frame = customtkinter.CTkFrame(self.network_frame)
        self.contacts_frame.grid_columnconfigure(0, weight=1)
        self.contacts_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

        self.contact_label = customtkinter.CTkLabel(self.contacts_frame, text="Contacts")
        self.contact_label.grid(row=0, column=0)
        self.contact_listbox = tkinter.Listbox(self.contacts_frame, font=('roboto, 10'), bg='grey20',
                                               fg='grey90', borderwidth=0, height=15)
        self.contact_listbox.grid(row=1, column=0, sticky='nsew', padx=20, pady=10)

        # -------------- File Menu -------------- #
        self.menubar = Menu(self)
        # --- Adding File Menu and commands
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.file)

        self.help_ = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Help', menu=self.help_)

        # --- Display Menu
        self.config(menu=self.menubar)

    def display_job_id(self, event):
        self.job_id_entry.grid(row=4, column=0, padx=10,pady=10)

    def display_position(self, event):
        self.position_entry.grid(row=4, column=0, padx=10,pady=10)

    def destroy_entry(self, event):
        self.job_id_entry.grid_forget()
        self.position_entry.grid_forget()




