import customtkinter


class UserSelect:
    def __init__(self, root):
        self.root = root

        self.user_window = customtkinter.CTkToplevel(root)
        self.user_window.grab_set()
        self.user_window.title("User")

        self.user_info_frame = customtkinter.CTkFrame(self.user_window)
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=20)

        self.user_entry = customtkinter.CTkComboBox(self.user_info_frame, values=[''], width=140)
        self.user_entry.grid(row=0, column=1, padx=(5, 20), pady=10)
        self.user_label = customtkinter.CTkLabel(self.user_info_frame, text='Select User')
        self.user_label.grid(row=0, column=0, padx=(20, 5), pady=10, sticky="e")

        self.submit_button = customtkinter.CTkButton(self.user_info_frame, text="Submit")
        self.submit_button.grid(row=5, column=1, pady=5)