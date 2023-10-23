import customtkinter
from .theme import Theme


class CreateUser:
    def __init__(self, root, theme:Theme):
        self.root = root
        self.window = customtkinter.CTkToplevel(root)
        self.window.grab_set()
        self.window.title("New User")

        self.welcome_frame = customtkinter.CTkFrame(self.window)
        self.welcome_frame.grid(row=0, column=0, padx=20, pady=20)
        self.create_button = customtkinter.CTkButton(self.welcome_frame, text="Create",
                                                     fg_color=theme.button_color,
                                                     text_color=theme.button_text_color
                                                     )
        self.create_button.grid(row=3, column=1, padx=20, pady=20)
        self.database_name_entry = customtkinter.CTkEntry(self.welcome_frame)
        self.database_name_entry.grid(row=2, column=1, padx=10, pady=9)
        self.database_name_label = customtkinter.CTkLabel(self.welcome_frame, text="Name:")
        self.database_name_label.grid(row=2, column=0, padx=20, pady=9, sticky="w")
