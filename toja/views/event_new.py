import customtkinter
from tkcalendar import DateEntry
import tkinter


class NewEvent:
    def __init__(self, root):
        self.root = root

        self.event_window = customtkinter.CTkToplevel(root)
        self.event_window.grab_set()
        self.event_window.title("Event")

        self.event_info_frame = customtkinter.CTkFrame(self.event_window)
        self.event_info_frame.grid(row=0, column=0, padx=20, pady=20)

        self.job_id_entry = customtkinter.CTkEntry(self.event_info_frame)
        self.job_id_label = customtkinter.CTkLabel(self.event_info_frame, text='Job_id')

        self.event_entry = customtkinter.CTkComboBox(self.event_info_frame, values=['follow_up',
                                                                                    'prospect',
                                                                                    'applied',
                                                                                    'meeting',
                                                                                    'networking',
                                                                                    'interview',
                                                                                    'offer',
                                                                                    'offer_accepted',
                                                                                    'rejected', ], width=140)
        self.event_entry.grid(row=1, column=1, padx=(5, 20), pady=10)
        self.event_label = customtkinter.CTkLabel(self.event_info_frame, text='Event')
        self.event_label.grid(row=1, column=0, padx=(20, 5), pady=10, sticky="e")

        self.day_entry = DateEntry(self.event_info_frame, selectmode='day', font=("roboto", "12"),
                                   date_pattern="yyyy-mm-dd")
        self.day_entry.grid(row=2, column=1, padx=(5, 20), pady=10)

        self.day_label = customtkinter.CTkLabel(self.event_info_frame, text='Day')
        self.day_label.grid(row=2, column=0, padx=(20, 5), pady=10, sticky="e")

        self.time_entry = customtkinter.CTkEntry(self.event_info_frame)
        self.time_entry.grid(row=3, column=1, padx=(5, 20), pady=10)
        self.time_label = customtkinter.CTkLabel(self.event_info_frame, text='Time')
        self.time_label.grid(row=3, column=0, padx=(20, 5), pady=10, sticky="e")

        self.contact_entry = customtkinter.CTkComboBox(self.event_info_frame, values=[' '], width=150)
        self.contact_entry.grid(row=4, column=1, padx=(5, 20), pady=10)
        self.contact_label = customtkinter.CTkLabel(self.event_info_frame, text='Contact')
        self.contact_label.grid(row=4, column=0, padx=(20, 5), pady=10, sticky="e")

        self.note_entry = customtkinter.CTkTextbox(self.event_info_frame)
        self.note_entry.grid(row=5, column=1, padx=(5, 20), pady=10)
        self.note_label = customtkinter.CTkLabel(self.event_info_frame, text='Notes')
        self.note_label.grid(row=5, column=0, padx=(20, 5), pady=10, sticky="e")

        self.submit_event_button = customtkinter.CTkButton(self.event_info_frame, text="Submit")
        self.submit_event_button.grid(row=6, column=1, pady=5)
