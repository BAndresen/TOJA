import customtkinter
from .theme import Theme


class CreateUser:
    def __init__(self, root, theme: Theme):
        self.root = root
        self.theme = theme
        self.window = customtkinter.CTkToplevel(root)
        self.window.grab_set()
        self.window.title("New User")
        self.welcome_frame = customtkinter.CTkFrame(self.window)
        self.welcome_frame.grid(row=0, column=0, padx=20, pady=20)

        self.user_name_entry = customtkinter.CTkEntry(self.welcome_frame)
        self.user_name_entry.grid(row=0, column=1, padx=10, pady=9)
        self.user_name_label = customtkinter.CTkLabel(self.welcome_frame, text="Name:")
        self.user_name_label.grid(row=0, column=0, padx=20, pady=9, sticky="w")

        self.button_frame = customtkinter.CTkFrame(self.welcome_frame, corner_radius=0)
        self.button_frame.grid(row=1, column=0, columnspan=2, sticky='ew')
        self.button_frame.grid_columnconfigure(0, weight=1)

        self.create_button = customtkinter.CTkButton(self.button_frame, text="Create",
                                                     fg_color=self.theme.button_color,
                                                     text_color=self.theme.button_text_color,
                                                     width=self.theme.main_button_width
                                                     )

        self.create_button.grid(row=0, column=1, padx=5, pady=10)
        self.cancel_button = customtkinter.CTkButton(self.button_frame, text="Cancel",
                                                     fg_color=self.theme.button_color,
                                                     text_color=self.theme.button_text_color,
                                                     width=self.theme.main_button_width,
                                                     command=self.cancel
                                                     )
        self.cancel_button.grid(row=0, column=2, padx=10, pady=10)

    def cancel(self):
        self.window.destroy()
