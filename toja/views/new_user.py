import customtkinter


class CreateUser:
    def __init__(self, root):
        self.root = root
        self.welcome_window = customtkinter.CTkToplevel(root)
        self.welcome_window.grab_set()
        self.welcome_window.title("New User")

        self.welcome_frame = customtkinter.CTkFrame(self.welcome_window)
        self.welcome_frame.grid(row=0, column=0, padx=20, pady=20)
        self.start_button = customtkinter.CTkButton(self.welcome_frame, text="Create")
        self.start_button.grid(row=3, column=1, padx=20, pady=20)
        self.database_name_entry = customtkinter.CTkEntry(self.welcome_frame)
        self.database_name_entry.grid(row=2, column=1, padx=10, pady=9)
        self.database_name_label = customtkinter.CTkLabel(self.welcome_frame, text="Name:")
        self.database_name_label.grid(row=2, column=0, padx=20, pady=9, sticky="w")
