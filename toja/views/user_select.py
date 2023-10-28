import customtkinter
from .theme import Theme


class UserSelect:
    def __init__(self, root, theme: Theme):
        self.root = root
        self.theme = theme

        self.user_window = customtkinter.CTkToplevel(root)
        self.user_window.attributes('-topmost', 'true')
        self.user_window.title("User")

        self.user_info_frame = customtkinter.CTkFrame(self.user_window)
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=20)

        self.user_entry = customtkinter.CTkComboBox(self.user_info_frame, values=[''], width=140)
        self.user_entry.grid(row=0, column=1, padx=(5, 20), pady=10)
        self.user_label = customtkinter.CTkLabel(self.user_info_frame, text='Select User')
        self.user_label.grid(row=0, column=0, padx=(20, 5), pady=10, sticky="e")

        self.button_frame = customtkinter.CTkFrame(self.user_info_frame, corner_radius=0)
        self.button_frame.grid(row=1, column=0, columnspan=2, sticky='ew')
        self.button_frame.grid_columnconfigure(0, weight=1)

        self.submit_button = customtkinter.CTkButton(self.button_frame, text="OK",
                                                     fg_color=self.theme.button_color,
                                                     text_color=self.theme.button_text_color,
                                                     width=self.theme.main_button_width
                                                     )
        self.submit_button.grid(row=0, column=1, pady=10, padx=5)

        self.cancel_button = customtkinter.CTkButton(self.button_frame, text="Cancel",
                                                     fg_color=self.theme.button_color,
                                                     text_color=self.theme.button_text_color,
                                                     width=self.theme.main_button_width,
                                                     command= self.cancel
                                                     )
        self.cancel_button.grid(row=0, column=2, pady=10, padx=5)

    def cancel(self):
        self.user_window.destroy()
