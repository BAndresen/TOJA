import customtkinter


class Contact:
    def __init__(self, root):
        self.root = root

        self.contact_window = customtkinter.CTkToplevel(root)
        self.contact_window.grab_set()
        self.contact_window.title("Contact")

        self.contact_info_frame = customtkinter.CTkFrame(self.contact_window)
        self.contact_info_frame.grid(row=0, column=0, padx=20, pady=20, stick='nsew')

        self.contact_id = customtkinter.CTkLabel(self.contact_info_frame, text='')
        self.contact_id.grid(row=0, column=1, padx=(5, 20), pady=5, sticky='w')
        self.contact_id_label = customtkinter.CTkLabel(self.contact_info_frame, text='Contact_ID:')
        self.contact_id_label.grid(row=0, column=0, padx=(20, 5), pady=5, sticky="e")

        self.first_name = customtkinter.CTkLabel(self.contact_info_frame, text='')
        self.first_name.grid(row=1, column=1, padx=(5, 20), pady=5, stick='w')
        self.first_name_label = customtkinter.CTkLabel(self.contact_info_frame, text='First Name:')
        self.first_name_label.grid(row=1, column=0, padx=(20, 5), pady=5, sticky="e")

        self.last_name = customtkinter.CTkLabel(self.contact_info_frame, text='')
        self.last_name.grid(row=3, column=1, padx=(5, 20), pady=5, stick='w')
        self.last_name_label = customtkinter.CTkLabel(self.contact_info_frame, text='Last Name:')
        self.last_name_label.grid(row=3, column=0, padx=(20, 5), pady=5, sticky="e")

        self.email = customtkinter.CTkLabel(self.contact_info_frame, text='')
        self.email.grid(row=4, column=1, padx=(5, 20), pady=5, stick='w')
        self.email_label = customtkinter.CTkLabel(self.contact_info_frame, text='Contact:')
        self.email_label.grid(row=4, column=0, padx=(20, 5), pady=5, sticky="e")

        self.phone = customtkinter.CTkLabel(self.contact_info_frame, text='')
        self.phone.grid(row=5, column=1, padx=(5, 20), pady=5, stick='w')
        self.phone_label = customtkinter.CTkLabel(self.contact_info_frame, text='Phone:')
        self.phone_label.grid(row=5, column=0, padx=(20, 5), pady=5, sticky="e")

        self.position = customtkinter.CTkLabel(self.contact_info_frame, text='')
        self.position.grid(row=6, column=1, padx=(5, 20), pady=5, stick='w')
        self.position_label = customtkinter.CTkLabel(self.contact_info_frame, text='Position:')
        self.position_label.grid(row=6, column=0, padx=(20, 5), pady=5, sticky="e")

        self.job_id = customtkinter.CTkLabel(self.contact_info_frame, text='')
        self.job_id.grid(row=7, column=1, padx=(5, 20), pady=5, stick='w')
        self.job_id_label = customtkinter.CTkLabel(self.contact_info_frame, text='Job_ID:')
        self.job_id_label.grid(row=7, column=0, padx=(20, 5), pady=5, sticky="e")

