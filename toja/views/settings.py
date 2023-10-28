import customtkinter
from .theme import Theme
from customtkinter.windows.widgets.font import ctk_font


class Settings:
    def __init__(self, root, theme: Theme):
        self.root = root
        self.theme = theme
        self.settings_window = customtkinter.CTkToplevel(root)
        self.settings_window.attributes('-topmost', 'true')
        # bold_font = ctk_font.CTkFont(family="Helvetica", size=12, weight="bold")

        self.settings_window.title("Settings")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        self.main_frame = customtkinter.CTkFrame(self.settings_window)
        self.main_frame.grid(row=0, column=0, padx=50, pady=(50, 10), sticky="nsew")

        self.appearance_frame = customtkinter.CTkFrame(self.main_frame)
        self.appearance_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # --- Appearance
        self.appearance_label = customtkinter.CTkLabel(self.appearance_frame, text='Appearance')
        self.appearance_label.grid(row=0, column=0)

        self.button_color_entry = customtkinter.CTkEntry(self.appearance_frame)
        self.button_color_entry.grid(row=1, column=1, padx=(5, 20), pady=2)
        self.button_color_label = customtkinter.CTkLabel(self.appearance_frame, text='Button Color:')
        self.button_color_label.grid(row=1, column=0, padx=(20, 5), pady=2, sticky="e")

        self.accent_color_entry = customtkinter.CTkEntry(self.appearance_frame)
        self.accent_color_entry.grid(row=2, column=1, padx=(5, 20), pady=2)
        self.accent_color_label = customtkinter.CTkLabel(self.appearance_frame, text='Accent Color:')
        self.accent_color_label.grid(row=2, column=0, padx=(20, 5), pady=2, sticky="e")

        self.icon_mode_label = customtkinter.CTkLabel(self.appearance_frame, text='Icon Mode:')
        self.icon_mode_label.grid(row=3, column=0, sticky='e')
        self.icon_mode_switch = customtkinter.CTkSwitch(self.appearance_frame, text='Dark',
                                                        button_color=self.theme.button_color,
                                                        progress_color=self.theme.accent_color)
        self.icon_mode_switch.grid(row=3, column=1)

        self.appearance_mode_label = customtkinter.CTkLabel(self.appearance_frame, text='Appearance Mode:')
        self.appearance_mode_label.grid(row=4, column=0, sticky='e')
        self.appearance_mode_switch = customtkinter.CTkSwitch(self.appearance_frame, text='Dark',
                                                              button_color=self.theme.button_color,
                                                              progress_color=self.theme.accent_color
                                                              )
        self.appearance_mode_switch.grid(row=4, column=1)

        # --- Keyword
        self.keyword_frame = customtkinter.CTkFrame(self.main_frame)
        self.keyword_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.keyword_label = customtkinter.CTkLabel(self.keyword_frame, text='Keywords')
        self.keyword_label.grid(row=1, column=0)

        self.job_keyword_results_entry = customtkinter.CTkEntry(self.keyword_frame, width=45)
        self.job_keyword_results_entry.grid(row=2, column=1, padx=(5, 20), pady=2, sticky='w')
        self.job_keyword_results_label = customtkinter.CTkLabel(self.keyword_frame, text='Job Results: ')
        self.job_keyword_results_label.grid(row=2, column=0, padx=(20, 5), pady=2, sticky="e")

        self.resume_keyword_entry = customtkinter.CTkEntry(self.keyword_frame, width=45)
        self.resume_keyword_entry.grid(row=3, column=1, padx=(5, 20), pady=(2,10), sticky='w')
        self.resume_keyword_label = customtkinter.CTkLabel(self.keyword_frame, text='Resume Results:')
        self.resume_keyword_label.grid(row=3, column=0, padx=(20, 5), pady=(2,10), sticky="e")

        # buttons
        self.button_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0)
        self.button_frame.grid(row=2, column=0, sticky='ew')
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.submit_button = customtkinter.CTkButton(self.button_frame, text="OK",
                                                     fg_color=self.theme.button_color,
                                                     text_color=self.theme.button_text_color,
                                                     width=self.theme.main_button_width
                                                     )
        self.submit_button.grid(row=0, column=1, padx=10, pady=10,)

        self.cancel_button = customtkinter.CTkButton(self.button_frame, text="Cancel",
                                                     fg_color=self.theme.button_color,
                                                     text_color=self.theme.button_text_color,
                                                     width=self.theme.main_button_width
                                                     )
        self.cancel_button.grid(row=0, column=2, padx=10, pady=10,)

        self.apply_button = customtkinter.CTkButton(self.appearance_frame, text="Apply",
                                                    fg_color=self.theme.button_color,
                                                    text_color=self.theme.button_text_color,
                                                    width=self.theme.main_button_width
                                                    )
        self.apply_button.grid(row=5, column=1, padx=20, pady=20, )

    def update_icon_text(self):
        self.submit_button.configure(text_color=self.theme.button_text_color)
        self.apply_button.configure(text_color=self.theme.button_text_color)

    def update_button_color(self):
        self.submit_button.configure(fg_color=self.theme.button_color)
        self.apply_button.configure(fg_color=self.theme.button_color)
        self.icon_mode_switch.configure(button_color=self.theme.button_color)
        self.appearance_mode_switch.configure(button_color=self.theme.button_color)

    def update_accent_color(self):
        self.icon_mode_switch.configure(progress_color=self.theme.accent_color)
        self.appearance_mode_switch.configure(progress_color=self.theme.accent_color)
