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

        self.job_list_frame = customtkinter.CTkFrame(self.home_frame)
        self.job_list_frame.grid(row=0, column=0, rowspan=2, padx=20, pady=20, sticky="nsew")
        self.job_list_frame.grid_columnconfigure(0,weight=1)
        self.job_list_frame.grid_rowconfigure(0,weight=1)
        # Job ListBox
        self.job_list_box = tkinter.Listbox(self.job_list_frame, font=('roboto, 10'), bg='grey20', fg='grey90',
                                            borderwidth=0)

        self.job_list_box.grid(row=0, column=0, rowspan=2, padx=(20,5), pady=20, sticky='nsew')

        # Add and Delete Job Button
        self.button_frame = customtkinter.CTkFrame(self.job_list_frame)
        self.button_frame.grid(row=0, column=1, padx=(5,20), pady=20, sticky="ne")
        self.new_job_button = customtkinter.CTkButton(self.button_frame, text="", image=plus_icon, width=35, height=35, fg_color='grey30', hover_color='grey15')
        self.new_job_button.grid(row=0, column=0, padx=10, pady=(10,5), sticky="nsew")
        self.delete_job_button = customtkinter.CTkButton(self.button_frame, text="", image=delete_icon, width=35, height=35,
                                                      fg_color='grey30', hover_color='grey15')
        self.delete_job_button.grid(row=1, column=0, padx=10, pady=(5,10), sticky="nsew")

        # Motivational Stats Board
        self.stat_board_frame = customtkinter.CTkFrame(self.home_frame)
        self.stat_board_frame.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")
        self.stat_label = customtkinter.CTkLabel(self.stat_board_frame, text="motivational design stats (coming soon)")
        self.stat_label.grid(row=0, column=0, padx=150, pady=150)

        # Graph - Days vs Events
        self.calendar_frame = customtkinter.CTkFrame(self.home_frame)
        self.calendar_frame.grid(row=2, columnspan=3, column=0, padx=20, pady=20, sticky="nsew")
        self.calendar_label_placeholder = (customtkinter.CTkLabel(
            self.calendar_frame, text="graph - days vs events (coming soon)"))
        self.calendar_label_placeholder.grid(row=0, column=1, padx=50, pady=50)

        # --------------- Event -------------- #

        self.event_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.event_frame.grid_columnconfigure(0, weight=1)

        self.event_button_frame = customtkinter.CTkFrame(self.event_frame)
        self.event_button_frame.grid(row=0, column=1, padx=(5,20), pady=20, sticky="ne")
        self.event_new_button = customtkinter.CTkButton(self.event_button_frame, text="", image=plus_icon, width=35, height=35, fg_color='grey30', hover_color='grey15')
        self.event_new_button.grid(row=0, column=0, padx=10, pady=(10,5), sticky="nsew")
        self.event_delete_button = customtkinter.CTkButton(self.event_button_frame, text="", image=delete_icon, width=35, height=35,
                                                      fg_color='grey30', hover_color='grey15')
        self.event_delete_button.grid(row=1, column=0, padx=10, pady=(5,10), sticky="nsew")

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

        # --------------- Network -------------- #

        self.network_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.network_frame.grid_columnconfigure(0, weight=1)

        self.network_button_frame = customtkinter.CTkFrame(self.network_frame)
        self.network_button_frame.grid(row=0, column=1, padx=(5,20), pady=20, sticky="ne")
        self.network_new_contact_button = customtkinter.CTkButton(self.network_button_frame, text="", image=plus_icon, width=35, height=35, fg_color='grey30', hover_color='grey15')
        self.network_new_contact_button.grid(row=0, column=0, padx=10, pady=(10,5), sticky="nsew")
        self.network_delete_job_button = customtkinter.CTkButton(self.network_button_frame, text="", image=delete_icon, width=35, height=35,
                                                      fg_color='grey30', hover_color='grey15')
        self.network_delete_job_button.grid(row=1, column=0, padx=10, pady=(5,10), sticky="nsew")

        self.contacts_frame = customtkinter.CTkFrame(self.network_frame)
        self.contacts_frame.grid_columnconfigure(0,weight=1)
        self.contacts_frame.grid(row=0, column=0, padx= 20, pady= 20, sticky='nsew')

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
