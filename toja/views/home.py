import tkinter
import customtkinter
from tkinter import Menu
import os
from PIL import Image
from CTkToolTip import *

import constants as constant
from .theme import Theme
from .visualizations import DayEvent


class HomeView(customtkinter.CTk):
    def __init__(self, theme: Theme):
        super().__init__()
        self.theme = theme

        # image icons
        self.icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), constant.ICON_FILE_DIRECTORY)
        self.plus_icon = customtkinter.CTkImage(Image.open(os.path.join(self.icon_path, self.theme.icon_plus)),
                                                size=(20, 20))
        self.delete_icon = customtkinter.CTkImage(Image.open(os.path.join(self.icon_path, self.theme.icon_delete)),
                                                  size=(22, 22))
        self.home_icon = customtkinter.CTkImage(Image.open(os.path.join(self.icon_path, self.theme.icon_home)),
                                                size=(22, 22))
        self.keyword_icon = customtkinter.CTkImage(Image.open(os.path.join(self.icon_path, self.theme.icon_keyword)),
                                                   size=(22, 22))
        self.event_icon = customtkinter.CTkImage(Image.open(os.path.join(self.icon_path, self.theme.icon_main_event)),
                                                 size=(22, 22))
        self.network_icon = customtkinter.CTkImage(
            Image.open(os.path.join(self.icon_path, self.theme.icon_main_contact)),
            size=(22, 22))
        self.view_icon = customtkinter.CTkImage(Image.open(os.path.join(self.icon_path, self.theme.icon_visible)),
                                                size=(22, 22))

        # Configure Window
        self.frame = "home"
        self.title("Track and Optimize your Job Applications")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_position = 0  # Start from the left edge
        y_position = 0  # Start from the top edge
        self.geometry(f'{screen_width - 50}x{screen_height - 100}+{x_position}+{y_position}')
        self.grid_columnconfigure(1, weight=4)
        self.grid_rowconfigure(0, weight=1)

        # Right Side Navigation Frame
        self.navigation_frame = customtkinter.CTkFrame(self, fg_color=self.theme.home_frame_background, )
        self.navigation_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        self.home_button = customtkinter.CTkButton(self.navigation_frame, image=self.home_icon, corner_radius=0,
                                                   height=40,
                                                   border_spacing=10,
                                                   text="Home",
                                                   fg_color=self.theme.home_frame_selected,
                                                   text_color=self.theme.text_color,
                                                   hover_color=("gray70", "gray30"),
                                                   anchor="w")
        self.home_button.grid(row=0, column=0, pady=(50, 0))

        self.keyword_button = customtkinter.CTkButton(self.navigation_frame, image=self.keyword_icon, corner_radius=0,
                                                      height=40,
                                                      border_spacing=10,
                                                      text="Keywords",
                                                      fg_color="transparent",
                                                      text_color=self.theme.text_color,
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w")
        self.keyword_button.grid(row=1, column=0)

        self.events_button = customtkinter.CTkButton(self.navigation_frame, image=self.event_icon, corner_radius=0,
                                                     height=40,
                                                     border_spacing=10,
                                                     text="Events",
                                                     fg_color="transparent",
                                                     text_color=self.theme.text_color,
                                                     hover_color=("gray70", "gray30"),
                                                     anchor="w")
        self.events_button.grid(row=2, column=0)

        self.network_button = customtkinter.CTkButton(self.navigation_frame, image=self.network_icon, corner_radius=0,
                                                      height=40,
                                                      border_spacing=10,
                                                      text="Network",
                                                      fg_color="transparent",
                                                      text_color=self.theme.text_color,
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w")
        self.network_button.grid(row=3, column=0)

        # Home Frame
        self.home_frame = customtkinter.CTkFrame(self, fg_color=self.theme.main_frame)
        self.home_frame.grid(row=0, column=1, sticky="nsew")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(0, weight=1)

        self.job_list_frame = customtkinter.CTkFrame(self.home_frame, fg_color=self.theme.second_frame)
        self.job_list_frame.grid(row=0, column=0, rowspan=2, padx=(20, 5), pady=(20, 5), sticky="nsew")
        self.job_list_frame.grid_columnconfigure(0, weight=1)
        self.job_list_frame.grid_rowconfigure(1, weight=1)

        # Job ListBox
        self.job_list_box = tkinter.Listbox(self.job_list_frame,
                                            font=self.theme.main_font,
                                            fg=self.theme.text_color,
                                            bg=self.theme.listbox_bg,
                                            selectbackground=self.theme.accent_color,
                                            selectforeground=self.theme.text_color,
                                            activestyle='none',
                                            borderwidth=0, height=20)

        self.job_list_box.grid(row=1, column=0, rowspan=2, padx=(20, 5), pady=(0, 20), sticky='nsew')

        # Job listbox title legend
        self.job_title_legend_frame = customtkinter.CTkFrame(self.job_list_frame, fg_color=self.theme.listbox_bg,
                                                             corner_radius=0)
        self.job_title_legend_frame.grid(column=0, row=0, sticky='nsew', pady=(20, 0), padx=(20, 5))

        self.job_id_title = customtkinter.CTkLabel(self.job_title_legend_frame, text="Job ID")
        self.job_id_title.grid(column=0, row=0, padx=(2, 10))
        self.company_title = customtkinter.CTkLabel(self.job_title_legend_frame, text="|  Company  |")
        self.company_title.grid(column=1, row=0, padx=10)
        self.position_title = customtkinter.CTkLabel(self.job_title_legend_frame, text="Position")
        self.position_title.grid(column=2, row=0, padx=10)

        # Add and Delete Job Button
        self.button_frame = customtkinter.CTkFrame(self.job_list_frame, fg_color=self.theme.main_frame)
        self.button_frame.grid(row=0, rowspan=2, column=1, padx=10, pady=20, sticky="new")
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.new_job_button = customtkinter.CTkButton(self.button_frame, text="",
                                                      image=self.plus_icon,
                                                      width=35, height=35,
                                                      fg_color=self.theme.button_color,
                                                      hover_color='grey15')
        self.new_job_button.grid(row=0, column=0, padx=10, pady=(10, 5), )
        self.delete_job_button = customtkinter.CTkButton(self.button_frame, text="", image=self.delete_icon, width=35,
                                                         height=35,
                                                         fg_color=self.theme.button_color, hover_color='grey15')
        self.delete_job_button.grid(row=1, column=0, padx=10, pady=(5, 10), )

        # Display Open switch Frame
        self.switch_frame = customtkinter.CTkFrame(self.job_list_frame, fg_color=self.theme.main_frame)
        self.switch_frame.grid(row=1, rowspan=2, column=1, padx=10, pady=80, sticky='n')
        self.display_open_label = customtkinter.CTkLabel(self.switch_frame, text='Only Active',
                                                         text_color=self.theme.text_color)
        self.display_open_label.grid(row=0, column=0, padx=10)
        self.open_jobs_switch = customtkinter.CTkSwitch(self.switch_frame, text='', width=0,
                                                        button_color=self.theme.button_color,
                                                        progress_color=self.theme.accent_color)
        self.open_jobs_switch.grid(row=1, column=0, pady=(0, 10))

        # Motivational Stats Board
        self.stat_board_frame = customtkinter.CTkFrame(self.home_frame, fg_color=self.theme.second_frame)
        self.stat_board_frame.grid(row=0, column=2, padx=(5, 20), pady=(20, 5), sticky="nsew")
        self.stat_board_frame.grid_columnconfigure(0, weight=1)
        self.stat_board_frame.grid_columnconfigure(1, weight=1)

        # Users stats
        self.user_stats_frame = customtkinter.CTkFrame(self.stat_board_frame, fg_color=self.theme.main_frame)
        self.user_stats_frame.grid(column=0, row=0, padx=10, pady=20)

        self.next_level = customtkinter.CTkLabel(self.user_stats_frame, text="Next Level",
                                                 text_color=self.theme.text_color)
        self.next_level.grid(row=2, column=0, padx=(20, 5), pady=5, sticky="e")

        self.user_name_label = customtkinter.CTkLabel(self.user_stats_frame, text="", font=self.theme.header_font,
                                                      text_color=self.theme.text_color)
        self.user_name_label.grid(row=0, column=0, padx=(20, 5), pady=(20,10))

        self.progress_bar = customtkinter.CTkProgressBar(self.user_stats_frame, progress_color=self.theme.accent_color)
        self.progress_bar.grid(row=2, column=1, padx=(5, 20), pady=5, sticky="ew")

        self.current_level_label = customtkinter.CTkLabel(self.user_stats_frame, text="Job Hunter:",
                                                          text_color=self.theme.text_color,
                                                          font=self.theme.header_two_font)
        self.current_level_label.grid(row=1, column=0, padx=(20, 5), pady=5, sticky="e")
        self.current_level = customtkinter.CTkLabel(self.user_stats_frame, text="", font=self.theme.header_two_font,
                                                    text_color=self.theme.text_color)
        self.current_level.grid(row=1, column=1, padx=(5, 20), pady=5, sticky="w")
        self.total_points_label = customtkinter.CTkLabel(self.user_stats_frame, text="Total Points:",
                                                         text_color=self.theme.text_color)
        self.total_points_label.grid(row=3, column=0, padx=(20, 5), pady=(5,20), sticky="e")
        self.total_points = customtkinter.CTkLabel(self.user_stats_frame, text="", font=self.theme.main_font_bold,
                                                   text_color=self.theme.text_color)
        self.total_points.grid(row=3, column=1, padx=(5, 20), pady=(5,20), sticky="w")

        # Graph - Days vs Events
        self.de_graph = DayEvent()
        self.de_graph.bg_color = self.theme.home_frame_background
        self.de_graph.face_color = self.theme.listbox_bg
        self.de_graph.text_color = self.theme.text_color
        self.de_graph.event_colors = self.theme.event_data

        self.calendar_frame = customtkinter.CTkFrame(self.home_frame, fg_color=self.theme.second_frame)
        self.calendar_frame.grid(row=2, columnspan=3, column=0, padx=20, pady=(5, 20), sticky="nsew")

        # --------------- Event -------------- #

        self.event_frame = customtkinter.CTkFrame(self, fg_color=self.theme.main_frame)
        self.event_frame.grid_columnconfigure(0, weight=1)
        self.event_frame.grid_rowconfigure(0, weight=2)
        self.event_frame.grid_rowconfigure(1, weight=1)

        self.event_button_frame = customtkinter.CTkFrame(self.event_frame, fg_color=self.theme.second_frame)
        self.event_button_frame.grid(row=0, column=1, padx=(5, 20), pady=20, sticky="ne")
        self.event_new_button = customtkinter.CTkButton(self.event_button_frame,
                                                        text="",
                                                        image=self.plus_icon,
                                                        width=35,
                                                        height=35,
                                                        fg_color=self.theme.button_color,
                                                        hover_color='grey15')
        self.event_new_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="nsew")
        self.event_delete_button = customtkinter.CTkButton(self.event_button_frame,
                                                           text="",
                                                           image=self.delete_icon,
                                                           width=35,
                                                           height=35,
                                                           fg_color=self.theme.button_color,
                                                           hover_color='grey15')
        self.event_delete_button.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="nsew")

        # Recent Events
        self.past_events_frame = customtkinter.CTkFrame(self.event_frame, fg_color=self.theme.second_frame)
        self.past_events_frame.grid_columnconfigure(0, weight=1)

        self.past_events_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.past_events_label = customtkinter.CTkLabel(self.past_events_frame, text="Past Events",
                                                        font=self.theme.header_two_font)
        self.past_events_label.grid(row=0, column=0, pady=(10, 0))
        self.past_events_listbox = tkinter.Listbox(self.past_events_frame,
                                                   font=self.theme.main_font,
                                                   fg=self.theme.text_color,
                                                   bg=self.theme.listbox_bg,
                                                   selectbackground=self.theme.accent_color,
                                                   selectforeground=self.theme.text_color,
                                                   activestyle='none',
                                                   borderwidth=0,
                                                   height=25)
        self.past_events_listbox.grid(row=1, column=0, sticky='nsew', padx=20, pady=(5, 20))

        # Upcoming Events
        self.upcoming_events_frame = customtkinter.CTkFrame(self.event_frame, fg_color=self.theme.second_frame)
        self.upcoming_events_frame.grid_columnconfigure(0, weight=1)

        self.upcoming_events_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.upcoming_events_label = customtkinter.CTkLabel(self.upcoming_events_frame, text="Upcoming Events",
                                                            font=self.theme.header_two_font)
        self.upcoming_events_label.grid(row=0, column=0, pady=(10, 0))
        self.upcoming_events_listbox = tkinter.Listbox(self.upcoming_events_frame,
                                                       font=self.theme.main_font,
                                                       fg=self.theme.text_color,
                                                       bg=self.theme.listbox_bg,
                                                       selectbackground=self.theme.accent_color,
                                                       selectforeground=self.theme.text_color,
                                                       activestyle='none',
                                                       borderwidth=0)
        self.upcoming_events_listbox.grid(row=1, column=0, sticky='nsew', padx=20, pady=(5, 20))

        # --------------- Keywords -------------- #

        self.analytics_frame = customtkinter.CTkFrame(self, fg_color=self.theme.main_frame)
        self.analytics_frame.grid_columnconfigure(0, weight=1)
        self.analytics_frame.grid_rowconfigure(0, weight=1)

        # Keywords Frames
        self.keywords_frame = customtkinter.CTkFrame(self.analytics_frame, fg_color=self.theme.second_frame)
        self.keywords_frame.grid_columnconfigure(0, weight=1)
        self.keywords_frame.grid_columnconfigure(1, weight=1)
        self.keywords_frame.grid_rowconfigure(1, weight=1)
        self.keywords_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Keyword Title labels
        self.jd_title = customtkinter.CTkLabel(self.keywords_frame, text="Job Description Search",
                                               text_color=self.theme.text_color,
                                               font=self.theme.header_two_font)
        self.jd_title.grid(row=0, column=0, pady=(10, 0))
        self.resume_title = customtkinter.CTkLabel(self.keywords_frame, text="Resume Search",
                                                   text_color=self.theme.text_color,
                                                   font=self.theme.header_two_font)
        self.resume_title.grid(row=0, column=1, pady=(10, 0))

        # Job Description search
        self.jd_frame = customtkinter.CTkFrame(self.keywords_frame, fg_color=self.theme.main_frame)
        self.jd_frame.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky='nsew')
        self.jd_frame.grid_columnconfigure(0, weight=1)
        self.jd_frame.grid_rowconfigure(1, weight=1)

        self.jd_search_button = customtkinter.CTkButton(self.jd_frame, text='Search',
                                                        fg_color=self.theme.button_color,
                                                        text_color=self.theme.button_text_color,
                                                        width=self.theme.main_button_width)
        self.jd_search_button.grid(row=2, column=0, pady=(0, 20))

        self.search_jd_frame = customtkinter.CTkFrame(self.jd_frame, fg_color=self.theme.second_frame)
        self.search_jd_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')
        # self.search_jd_frame.grid_columnconfigure(3, weight=1)

        self.search_by_label = customtkinter.CTkLabel(self.search_jd_frame, text="Search By:",
                                                      text_color=self.theme.text_color)
        self.search_by_label.grid(row=0, column=0)
        self.radio_var = tkinter.IntVar(value=0)
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.search_jd_frame, variable=self.radio_var,
                                                           value=0, text="All", border_width_checked=4,
                                                           fg_color=self.theme.accent_color,
                                                           text_color=self.theme.text_color)
        self.radio_button_1.grid(row=1, column=0, pady=5, padx=(20, 0))
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.search_jd_frame, variable=self.radio_var,
                                                           value=1, text='Job ID', border_width_checked=4,
                                                           fg_color=self.theme.accent_color,
                                                           text_color=self.theme.text_color)
        self.radio_button_2.grid(row=2, column=0, pady=5, padx=(20, 0))
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.search_jd_frame, variable=self.radio_var,
                                                           value=2, text='Position',
                                                           border_width_checked=4,
                                                           fg_color=self.theme.accent_color,
                                                           text_color=self.theme.text_color)
        self.radio_button_3.grid(row=3, column=0, pady=(5, 43), padx=(20, 0))

        self.radio_button_1.bind('<Button-1>', self.destroy_entry)
        self.radio_button_2.bind('<Button-1>', self.display_job_id)
        self.radio_button_3.bind('<Button-1>', self.display_position)

        self.job_id_entry = customtkinter.CTkEntry(self.search_jd_frame)
        self.position_entry = customtkinter.CTkEntry(self.search_jd_frame)
        self.view_position = customtkinter.CTkButton(self.search_jd_frame, text='', image=self.view_icon,
                                                     fg_color=self.theme.second_frame,
                                                     width=35)

        self.position_tooltip = CTkToolTip(self.view_position, delay=0.01, message='', bg_color=self.theme.listbox_bg)

        self.slider_1 = customtkinter.CTkSlider(self.search_jd_frame, from_=0, to=100, command=self.show_value,
                                                button_color=self.theme.accent_color)
        self.slider_1.set(80)

        start_val = customtkinter.Variable(self, 80)
        self.threshold_entry = customtkinter.CTkEntry(self.search_jd_frame, width=40, )
        self.threshold_label = customtkinter.CTkLabel(self.search_jd_frame, text="Threshold:",
                                                      text_color=self.theme.text_color)
        self.threshold_entry.configure(textvariable=start_val)

        # list box job
        self.jd_search_listbox = tkinter.Listbox(self.jd_frame,
                                                 font=self.theme.main_font,
                                                 fg=self.theme.text_color,
                                                 bg=self.theme.listbox_bg,
                                                 selectbackground=self.theme.accent_color,
                                                 selectforeground=self.theme.text_color,
                                                 activestyle='none',
                                                 borderwidth=0,
                                                 )
        self.jd_search_listbox.grid(row=1, column=0, padx=20, pady=(5, 20), sticky='nsew')

        # Resume search
        self.resume_frame = customtkinter.CTkFrame(self.keywords_frame, fg_color=self.theme.main_frame)
        self.resume_frame.grid(row=1, column=1, padx=(10, 20), pady=(10, 20), sticky='nsew')
        self.resume_frame.grid_columnconfigure(0, weight=1)
        self.resume_frame.grid_rowconfigure(1, weight=1)

        self.resume_search_button = customtkinter.CTkButton(self.resume_frame, text='Search',
                                                            fg_color=self.theme.button_color,
                                                            text_color=self.theme.button_text_color,
                                                            width=self.theme.main_button_width)
        self.resume_search_button.grid(row=2, column=0, pady=(0, 20))

        self.search_resume_frame = customtkinter.CTkFrame(self.resume_frame, fg_color=self.theme.second_frame)
        self.search_resume_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

        self.upload_resume = customtkinter.CTkLabel(self.search_resume_frame, text='Upload Resume',
                                                    text_color=self.theme.text_color)
        self.upload_resume.grid(row=0, column=0, padx=10, pady=(10, 0))
        self.resume_browse_button = customtkinter.CTkButton(self.search_resume_frame, text='Browse',
                                                            fg_color=self.theme.button_color,
                                                            text_color=self.theme.button_text_color,
                                                            width=self.theme.main_button_width)
        self.resume_browse_button.grid(row=1, column=0, padx=10, pady=(0, 10))

        self.resume_score_label = customtkinter.CTkLabel(self.search_resume_frame, text='Resume Score:',
                                                         text_color=self.theme.text_color)
        self.resume_score_label.grid(row=2, column=0)
        self.resume_score = customtkinter.CTkLabel(self.search_resume_frame, text='',
                                                   text_color=self.theme.text_color)
        self.resume_score.grid(row=2, column=1)

        # list box resume
        self.resume_search_listbox = tkinter.Listbox(self.resume_frame,
                                                     font=self.theme.main_font,
                                                     fg=self.theme.text_color,
                                                     bg=self.theme.listbox_bg,
                                                     selectbackground=self.theme.accent_color,
                                                     selectforeground=self.theme.text_color,
                                                     activestyle='none',
                                                     borderwidth=0,
                                                     )
        self.resume_search_listbox.grid(row=1, column=0, padx=20, pady=(5, 20), sticky='nsew')

        # --------------- Network -------------- #

        self.network_frame = customtkinter.CTkFrame(self, fg_color=self.theme.main_frame)
        self.network_frame.grid_columnconfigure(0, weight=1)

        self.network_button_frame = customtkinter.CTkFrame(self.network_frame, fg_color=self.theme.second_frame)
        self.network_button_frame.grid(row=0, column=1, padx=(5, 20), pady=20, sticky="ne")
        self.network_new_contact_button = customtkinter.CTkButton(self.network_button_frame, text="",
                                                                  image=self.plus_icon,
                                                                  width=35, height=35, fg_color=self.theme.button_color,
                                                                  hover_color='grey15')
        self.network_new_contact_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="nsew")
        self.network_delete_job_button = customtkinter.CTkButton(self.network_button_frame, text="",
                                                                 image=self.delete_icon,
                                                                 width=35, height=35,
                                                                 fg_color=self.theme.button_color, hover_color='grey15')
        self.network_delete_job_button.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="nsew")

        self.contacts_frame = customtkinter.CTkFrame(self.network_frame, fg_color=self.theme.second_frame)
        self.contacts_frame.grid_columnconfigure(0, weight=1)
        self.contacts_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

        self.contact_label = customtkinter.CTkLabel(self.contacts_frame, text="Contacts",
                                                    font=self.theme.header_two_font)
        self.contact_label.grid(row=0, column=0, pady=(10, 0))
        self.contact_listbox = tkinter.Listbox(self.contacts_frame,
                                               font=self.theme.main_font,
                                               fg=self.theme.text_color,
                                               bg=self.theme.listbox_bg,
                                               selectbackground=self.theme.accent_color,
                                               selectforeground=self.theme.text_color,
                                               activestyle='none',
                                               borderwidth=0, height=15)
        self.contact_listbox.grid(row=1, column=0, sticky='nsew', padx=20, pady=(5, 20))

        # -------------- File Menu -------------- #
        self.menubar = Menu(self)
        # --- Adding File Menu and commands
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.file)

        self.help_ = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Help', menu=self.help_)

        # --- Display Menu
        self.config(menu=self.menubar)

        self.home_list_box_list = [
            self.job_list_box,
            self.past_events_listbox,
            self.upcoming_events_listbox,
            self.jd_search_listbox,
            self.resume_search_listbox,
            self.contact_listbox,
        ]

        # Bind the on_closing function to the window's close event
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        # Clean up tasks or stop the process here
        self.destroy()
        self.quit()

    def event_frame_button(self):
        self.home_frame.grid_remove()
        self.analytics_frame.grid_remove()
        self.network_frame.grid_remove()
        self.event_frame.grid(row=0, column=1, sticky="nsew")
        self.events_button.configure(fg_color=self.theme.home_frame_selected)
        self.home_button.configure(fg_color='transparent')
        self.network_button.configure(fg_color='transparent')
        self.keyword_button.configure(fg_color='transparent')

    def home_frame_button(self):
        self.event_frame.grid_remove()
        self.analytics_frame.grid_remove()
        self.network_frame.grid_remove()
        self.home_frame.grid(row=0, column=1, sticky="nsew")
        self.home_button.configure(fg_color=self.theme.home_frame_selected)
        self.events_button.configure(fg_color='transparent')
        self.network_button.configure(fg_color='transparent')
        self.keyword_button.configure(fg_color='transparent')

    def keyword_frame_button(self):
        self.home_frame.grid_remove()
        self.event_frame.grid_remove()
        self.network_frame.grid_remove()
        self.analytics_frame.grid(row=0, column=1, sticky="nsew")
        self.keyword_button.configure(fg_color=self.theme.home_frame_selected)
        self.events_button.configure(fg_color='transparent')
        self.home_button.configure(fg_color='transparent')
        self.network_button.configure(fg_color='transparent')

    def network_frame_button(self):
        self.home_frame.grid_remove()
        self.event_frame.grid_remove()
        self.analytics_frame.grid_remove()
        self.view_position.grid_remove()
        self.network_frame.grid(row=0, column=1, sticky="nsew")
        self.network_button.configure(fg_color=self.theme.home_frame_selected)
        self.events_button.configure(fg_color='transparent')
        self.home_button.configure(fg_color='transparent')
        self.keyword_button.configure(fg_color='transparent')

    def display_job_id(self, event):
        self.position_entry.grid_remove()
        self.threshold_entry.grid_remove()
        self.threshold_label.grid_remove()
        self.view_position.grid_remove()
        self.slider_1.grid_remove()
        self.job_id_entry.grid(row=2, column=1, padx=0, sticky='w')
        self.job_id_entry.configure(placeholder_text='Enter Job ID')
        self.radio_button_3.grid(pady=(5, 43))

    def display_position(self, event):
        self.job_id_entry.grid_remove()
        self.position_entry.grid(row=3, column=1, padx=0, sticky='ew')
        self.position_entry.configure(placeholder_text='Enter Position')
        self.threshold_entry.grid(row=4, column=2, padx=0, pady=5, )
        self.threshold_label.grid(row=4, column=0, sticky="e", padx=3)
        self.slider_1.grid(row=4, column=1, sticky="w")
        self.radio_button_3.grid(pady=5)
        self.view_position.grid(row=3, column=2, )

    def destroy_entry(self, event):
        self.job_id_entry.grid_remove()
        self.position_entry.grid_remove()
        self.threshold_entry.grid_remove()
        self.threshold_label.grid_remove()
        self.view_position.grid_remove()
        self.slider_1.grid_remove()
        self.radio_button_3.grid(pady=(5, 43))

    def show_value(self, value):
        v = customtkinter.Variable(self, int(value))
        self.threshold_entry.configure(textvariable=v)

    def update_icon_paths(self):
        self.plus_icon = customtkinter.CTkImage(Image.open(os.path.join(self.icon_path, self.theme.icon_plus)),
                                                size=(20, 20))
        self.delete_icon = customtkinter.CTkImage(
            Image.open(os.path.join(self.icon_path, self.theme.icon_delete)),
            size=(22, 22))
        self.home_icon = customtkinter.CTkImage(Image.open(os.path.join(self.icon_path, self.theme.icon_home)),
                                                size=(22, 22))
        self.keyword_icon = customtkinter.CTkImage(
            Image.open(os.path.join(self.icon_path, self.theme.icon_keyword)),
            size=(22, 22))
        self.event_icon = customtkinter.CTkImage(
            Image.open(os.path.join(self.icon_path, self.theme.icon_main_event)),
            size=(22, 22))
        self.network_icon = customtkinter.CTkImage(
            Image.open(os.path.join(self.icon_path, self.theme.icon_main_contact)),
            size=(22, 22))
        self.view_icon = customtkinter.CTkImage(Image.open(os.path.join(self.icon_path, self.theme.icon_visible)),
                                                size=(22, 22))

    def update_home_theme(self):
        home_frame_button_list = [
            self.home_button,
            self.keyword_button,
            self.events_button,
            self.network_button,
        ]

        self.navigation_frame.configure(fg_color=self.theme.home_frame_background)
        self.home_button.configure(image=self.home_icon)
        self.keyword_button.configure(image=self.keyword_icon)
        self.events_button.configure(image=self.event_icon)
        self.network_button.configure(image=self.network_icon)
        self.home_frame.configure(fg_color=self.theme.main_frame)
        self.view_position.configure(fg_color=self.theme.second_frame, image=self.view_icon)
        self.position_tooltip.configure(bg_color=self.theme.listbox_bg)

        for buttons in home_frame_button_list:
            buttons.configure(text_color=self.theme.text_color)
            if not buttons.cget('fg_color') == 'transparent':
                buttons.configure(fg_color=self.theme.home_frame_selected)

        for listbox in self.home_list_box_list:
            listbox.configure(font=self.theme.main_font,
                              fg=self.theme.text_color,
                              bg=self.theme.listbox_bg,
                              selectbackground=self.theme.accent_color,
                              selectforeground=self.theme.text_color, )
        self.job_title_legend_frame.configure(fg_color=self.theme.listbox_bg)

        second_frame_list = [
            self.job_list_frame,
            self.stat_board_frame,
            self.calendar_frame,
            self.event_button_frame,
            self.past_events_frame,
            self.upcoming_events_frame,
            self.search_resume_frame,
            self.network_button_frame,
            self.search_jd_frame,
            self.keywords_frame,
            self.contacts_frame,

        ]
        for frame in second_frame_list:
            frame.configure(fg_color=self.theme.second_frame)

        main_frame_list = [
            self.analytics_frame,
            self.event_frame,
            self.network_frame,
            self.jd_frame,
            self.resume_frame,
            self.button_frame,
            self.user_stats_frame,
            self.switch_frame,

        ]
        for frame in main_frame_list:
            frame.configure(fg_color=self.theme.main_frame)

        label_list = [
            self.jd_title,
            self.resume_title,
            self.search_by_label,
            self.radio_button_1,
            self.radio_button_2,
            self.radio_button_3,
            self.threshold_label,
            self.upload_resume,
            self.resume_score_label,
            self.resume_score,
            self.total_points_label,
            self.next_level,
            self.current_level_label,
            self.current_level,
            self.total_points,
            self.user_name_label,
            self.display_open_label,
        ]

        for label in label_list:
            label.configure(text_color=self.theme.text_color)

    def update_day_event_graph_color_scheme(self):
        self.de_graph.bg_color = self.theme.home_frame_background
        self.de_graph.face_color = self.theme.listbox_bg
        self.de_graph.text_color = self.theme.text_color
        self.calendar_frame.destroy()
        self.calendar_frame = customtkinter.CTkFrame(self.home_frame, fg_color=self.theme.second_frame)
        self.calendar_frame.grid(row=2, columnspan=3, column=0, padx=20, pady=(5, 20), sticky="nsew")
        self.de_graph.toggle_color_scheme(self.calendar_frame)

    def update_icon_mode(self):
        self.update_icon_paths()
        self.new_job_button.configure(image=self.plus_icon)
        self.delete_job_button.configure(image=self.delete_icon)
        self.event_new_button.configure(image=self.plus_icon)
        self.event_delete_button.configure(image=self.delete_icon)
        self.network_new_contact_button.configure(image=self.plus_icon)
        self.network_delete_job_button.configure(image=self.delete_icon)
        self.jd_search_button.configure(text_color=self.theme.button_text_color)
        self.resume_browse_button.configure(text_color=self.theme.button_text_color)
        self.resume_search_button.configure(text_color=self.theme.button_text_color)

    def update_button_color(self):
        self.new_job_button.configure(fg_color=self.theme.button_color)
        self.delete_job_button.configure(fg_color=self.theme.button_color)
        self.event_new_button.configure(fg_color=self.theme.button_color)
        self.event_delete_button.configure(fg_color=self.theme.button_color)
        self.network_new_contact_button.configure(fg_color=self.theme.button_color)
        self.network_delete_job_button.configure(fg_color=self.theme.button_color)
        self.jd_search_button.configure(fg_color=self.theme.button_color)
        self.resume_browse_button.configure(fg_color=self.theme.button_color)
        self.resume_search_button.configure(fg_color=self.theme.button_color)
        self.open_jobs_switch.configure(button_color=self.theme.button_color)

    def update_accent_color(self):
        self.progress_bar.configure(progress_color=self.theme.accent_color)
        self.radio_button_1.configure(fg_color=self.theme.accent_color)
        self.radio_button_2.configure(fg_color=self.theme.accent_color)
        self.radio_button_3.configure(fg_color=self.theme.accent_color)
        self.slider_1.configure(button_color=self.theme.accent_color)
        for listbox in self.home_list_box_list:
            listbox.configure(selectbackground=self.theme.accent_color)
        self.open_jobs_switch.configure(progress_color=self.theme.accent_color)
