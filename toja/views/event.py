import customtkinter
from tkcalendar import DateEntry


class Event:
    def __init__(self, root):
        self.root = root

        self.event_window = customtkinter.CTkToplevel(root)
        self.event_window.attributes('-topmost','true')
        self.event_window.title("Event")

        self.event_info_frame = customtkinter.CTkFrame(self.event_window)
        self.event_info_frame.grid(row=0, column=0, padx=20, pady=20, stick='nsew')

        self.event_id = customtkinter.CTkLabel(self.event_info_frame, text='')
        self.event_id.grid(row=0, column=1, padx=(5, 20), pady=5, sticky='w')
        self.event_id_label = customtkinter.CTkLabel(self.event_info_frame, text='Event_ID:')
        self.event_id_label.grid(row=0, column=0, padx=(20, 5), pady=5, sticky="e")

        self.event_status = customtkinter.CTkLabel(self.event_info_frame, text='')
        self.event_status.grid(row=1, column=1, padx=(5, 20), pady=5, stick='w')
        self.event_label = customtkinter.CTkLabel(self.event_info_frame, text='Event:')
        self.event_label.grid(row=1, column=0, padx=(20, 5), pady=5, sticky="e")

        self.day_entry = customtkinter.CTkLabel(self.event_info_frame, text='')
        self.day_entry.grid(row=3, column=1, padx=(5, 20), pady=5, stick='w')
        self.day_label = customtkinter.CTkLabel(self.event_info_frame, text='Day:')
        self.day_label.grid(row=3, column=0, padx=(20, 5), pady=5, sticky="e")

        self.time_entry = customtkinter.CTkLabel(self.event_info_frame, text='')
        self.time_entry.grid(row=4, column=1, padx=(5, 20), pady=5, stick='w')
        self.time_label = customtkinter.CTkLabel(self.event_info_frame, text='Time:')
        self.time_label.grid(row=4, column=0, padx=(20, 5), pady=5, sticky="e")

        self.company_entry = customtkinter.CTkLabel(self.event_info_frame, text='')
        self.company_entry.grid(row=5, column=1, padx=(5, 20), pady=5, stick='w')
        self.company_label = customtkinter.CTkLabel(self.event_info_frame, text='Company:')
        self.company_label.grid(row=5, column=0, padx=(20, 5), pady=5, sticky="e")

        self.position_entry = customtkinter.CTkLabel(self.event_info_frame, text='')
        self.position_entry.grid(row=6, column=1, padx=(5, 20), pady=5, stick='w')
        self.position_label = customtkinter.CTkLabel(self.event_info_frame, text='Position:')
        self.position_label.grid(row=6, column=0, padx=(20, 5), pady=5, sticky="e")

        self.contact_entry = customtkinter.CTkLabel(self.event_info_frame, text='')
        self.contact_entry.grid(row=7, column=1, padx=(5, 20), pady=5, stick='w')
        self.contact_label = customtkinter.CTkLabel(self.event_info_frame, text='Contact:')
        self.contact_label.grid(row=7, column=0, padx=(20, 5), pady=5, sticky="e")

        self.note_frame = customtkinter.CTkFrame(self.event_window)
        self.note_frame.grid(row=1, column=0, padx=20, pady=20)
        self.note_entry = customtkinter.CTkLabel(self.note_frame, text='', wraplength=500, justify='left')
        self.note_entry.grid(row=0, column=1, padx=(5, 20), pady=10, stick='w')
        self.note_label = customtkinter.CTkLabel(self.note_frame, text='Notes:')
        self.note_label.grid(row=0, column=0, padx=(20, 5), pady=10, sticky="e")
