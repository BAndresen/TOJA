import tkinter

import customtkinter
from CTkListbox.ctk_listbox import CTkListbox


class HomeView(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure Window
        self.frame = "home"
        self.title("Track and Optimize your Job Application Process")
        self.geometry('1200x650')
        self.grid_columnconfigure(1, weight=4)
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
        # self.job_list_box = CTkListbox(self.home_frame)  # -------- CTKListbox
        self.job_list_box = tkinter.Listbox(self.home_frame, bg="light grey", bd=0 )  # --------- tkinter.Listbox

        self.job_list_box.grid(row=0, column=0, rowspan=2, padx=20, pady=20, sticky='nsew')

        # Motivational Stats Board
        self.stat_board_frame = customtkinter.CTkFrame(self.home_frame)
        self.stat_board_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.stat_label = customtkinter.CTkLabel(self.stat_board_frame, text="motivational design stats (coming soon)")
        self.stat_label.grid(row=0, column=0, padx=150, pady=150)

        # Graph - Days vs Events
        self.calendar_frame = customtkinter.CTkFrame(self.home_frame)
        self.calendar_frame.grid(row=2, columnspan=2, column=0, padx=20, pady=20, sticky="nsew")
        self.calendar_label_placeholder = (customtkinter.CTkLabel(
            self.calendar_frame, text="graph - days vs events (coming soon)"))
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

        # Upcoming Events
        self.upcoming_events_frame = customtkinter.CTkFrame(self.event_frame)
        self.upcoming_events_frame.grid_columnconfigure(0, weight=1)

        self.upcoming_events_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.upcoming_events_label = customtkinter.CTkLabel(self.upcoming_events_frame, text="Recent Events")
        self.upcoming_events_label.grid(row=0, column=0)

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

