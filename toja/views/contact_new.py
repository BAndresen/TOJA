import customtkinter
from .theme import Theme


class NewContact:
    def __init__(self, root, theme: Theme):
        self.root = root
        self.theme = theme

        self.contact_window = customtkinter.CTkToplevel(root)
        self.contact_window.attributes('-topmost', 'true')
        self.contact_window.title("New Contact")
        self.contact_info_frame = customtkinter.CTkFrame(self.contact_window)
        self.contact_info_frame.grid(row=0, column=0, padx=20, pady=20)

        self.job_id_entry = customtkinter.CTkEntry(self.contact_info_frame)
        self.job_id_label = customtkinter.CTkLabel(self.contact_info_frame, text='Job_ID')

        self.first_name_entry = customtkinter.CTkEntry(self.contact_info_frame)
        self.first_name_entry.grid(row=2, column=1, padx=(5, 20), pady=10)
        self.first_name_label = customtkinter.CTkLabel(self.contact_info_frame, text='First Name')
        self.first_name_label.grid(row=2, column=0, padx=(20, 5), pady=10, sticky="e")

        self.last_name_entry = customtkinter.CTkEntry(self.contact_info_frame)
        self.last_name_entry.grid(row=3, column=1, padx=(5, 20), pady=10)
        self.last_name_label = customtkinter.CTkLabel(self.contact_info_frame, text='Last Name')
        self.last_name_label.grid(row=3, column=0, padx=(20, 5), pady=10, sticky="e")

        self.email_entry = customtkinter.CTkEntry(self.contact_info_frame)
        self.email_entry.grid(row=4, column=1, padx=(5, 20), pady=10)
        self.email_label = customtkinter.CTkLabel(self.contact_info_frame, text='Email')
        self.email_label.grid(row=4, column=0, padx=(20, 5), pady=10, sticky="e")

        self.phone_entry = customtkinter.CTkEntry(self.contact_info_frame)
        self.phone_entry.grid(row=5, column=1, padx=(5, 20), pady=10)
        self.phone_label = customtkinter.CTkLabel(self.contact_info_frame, text='Phone')
        self.phone_label.grid(row=5, column=0, padx=(20, 5), pady=10, sticky="e")

        self.position_entry = customtkinter.CTkEntry(self.contact_info_frame)
        self.position_entry.grid(row=6, column=1, padx=(5, 20), pady=10)
        self.position_label = customtkinter.CTkLabel(self.contact_info_frame, text='Position')
        self.position_label.grid(row=6, column=0, padx=(20, 5), pady=10, sticky="e")

        self.submit_contact_button = customtkinter.CTkButton(self.contact_window, text="Submit",
                                                             fg_color=self.theme.button_color,
                                                             text_color=self.theme.button_text_color,
                                                             width=self.theme.main_button_width)
        self.submit_contact_button.grid(row=1, column=0, pady=20, padx=20, sticky="e")
