import customtkinter
from .theme import Theme
from customtkinter.windows.widgets.font import ctk_font
from CTkColorPicker import *


class Settings:
    def __init__(self, root, theme: Theme):
        self.root = root
        self.theme = theme
        self.settings_window = customtkinter.CTkToplevel(root)
        self.settings_window.attributes('-topmost', 'true')

        self.settings_window.title("Settings")

        self.main_frame = customtkinter.CTkFrame(self.settings_window, fg_color=self.theme.second_frame)
        self.main_frame.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")

        self.appearance_frame = customtkinter.CTkFrame(self.main_frame, fg_color=self.theme.main_frame)
        self.appearance_frame.grid(row=0, column=0, padx=10, pady=(10,5), sticky="nsew")

        # --- Appearance
        self.appearance_label = customtkinter.CTkLabel(self.appearance_frame, text='Appearance',
                                                       font=self.theme.main_font_bold)
        self.appearance_label.grid(row=0, column=0)

        self.button_color_button = customtkinter.CTkButton(self.appearance_frame, text='',
                                                           width=22,
                                                           height=22,
                                                           corner_radius=10,
                                                           command=self.get_button_color)
        self.button_color_button.grid(row=1, column=1, pady=2, padx=10, stick='w')
        self.button_color_label = customtkinter.CTkLabel(self.appearance_frame, text='Button Color:')
        self.button_color_label.grid(row=1, column=0, padx=(20, 5), pady=2, sticky="e")

        self.accent_color_button = customtkinter.CTkButton(self.appearance_frame, text='',
                                                           width=22,
                                                           height=22,
                                                           corner_radius=10,
                                                           command=self.get_accent_color
                                                           )
        self.accent_color_button.grid(row=2, column=1, padx=10, stick='w', pady=2)
        self.accent_color_label = customtkinter.CTkLabel(self.appearance_frame, text='Accent Color:')
        self.accent_color_label.grid(row=2, column=0, padx=(20, 5), pady=2, sticky="e")

        self.icon_mode_label = customtkinter.CTkLabel(self.appearance_frame, text='Icon Mode:')
        self.icon_mode_label.grid(row=3, column=0, sticky='e')
        self.icon_mode_switch = customtkinter.CTkSwitch(self.appearance_frame, text='Dark',
                                                        button_color=self.theme.button_color,
                                                        progress_color=self.theme.accent_color)
        self.icon_mode_switch.grid(row=3, column=1, pady=2)

        self.appearance_mode_label = customtkinter.CTkLabel(self.appearance_frame, text='Appearance Mode:')
        self.appearance_mode_label.grid(row=4, column=0, sticky='e', padx=(10, 0))
        self.appearance_mode_switch = customtkinter.CTkSwitch(self.appearance_frame, text='Dark',
                                                              button_color=self.theme.button_color,
                                                              progress_color=self.theme.accent_color
                                                              )
        self.appearance_mode_switch.grid(row=4, column=1, pady=2)

        self.num_of_days_dv_graph_entry = customtkinter.CTkEntry(self.appearance_frame, width=45)
        self.num_of_days_dv_graph_entry.grid(row=5, column=1, padx=(5, 20), pady=(2, 10), sticky='w')
        self.num_of_days_dv_graph_label = customtkinter.CTkLabel(self.appearance_frame, text='Num of Days Graph:')
        self.num_of_days_dv_graph_label.grid(row=5, column=0, padx=(20, 5), pady=(2, 10), sticky="e")

        # --- Keyword
        self.keyword_frame = customtkinter.CTkFrame(self.main_frame, fg_color=self.theme.main_frame)
        self.keyword_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        self.keyword_label = customtkinter.CTkLabel(self.keyword_frame, text='Keywords', font=self.theme.main_font_bold)
        self.keyword_label.grid(row=1, column=0)

        self.job_keyword_results_entry = customtkinter.CTkEntry(self.keyword_frame, width=45)
        self.job_keyword_results_entry.grid(row=2, column=1, padx=(5, 20), pady=2, sticky='w')
        self.job_keyword_results_label = customtkinter.CTkLabel(self.keyword_frame, text='Job Results: ')
        self.job_keyword_results_label.grid(row=2, column=0, padx=(20, 5), pady=2, sticky="e")

        self.resume_keyword_entry = customtkinter.CTkEntry(self.keyword_frame, width=45)
        self.resume_keyword_entry.grid(row=3, column=1, padx=(5, 20), pady=(2, 10), sticky='w')
        self.resume_keyword_label = customtkinter.CTkLabel(self.keyword_frame, text='Resume Results:')
        self.resume_keyword_label.grid(row=3, column=0, padx=(20, 5), pady=(2, 10), sticky="e")

        # --- Auto Events
        self.auto_frame = customtkinter.CTkFrame(self.main_frame, fg_color=self.theme.main_frame)
        self.auto_frame.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

        self.auto_label = customtkinter.CTkLabel(self.auto_frame, text='Automation', font=self.theme.main_font_bold)
        self.auto_label.grid(row=1, column=0, padx=25)

        self.job_keyword_results_label = customtkinter.CTkLabel(self.auto_frame, text='Close Job: ')
        self.job_keyword_results_label.grid(row=2, column=0, padx=(20, 5), pady=2, sticky="e")
        self.auto_close_switch = customtkinter.CTkSwitch(self.auto_frame, text='',
                                                         button_color=self.theme.button_color,
                                                         progress_color=self.theme.accent_color
                                                         )
        self.auto_close_switch.grid(row=2, column=1, pady=2)

        self.auto_close_days_entry = customtkinter.CTkEntry(self.auto_frame, width=45)
        self.auto_close_days_entry.grid(row=3, column=1, padx=(5, 20), pady=(2, 10), sticky='w')
        self.auto_close_days_label = customtkinter.CTkLabel(self.auto_frame, text='Inactive Days:')
        self.auto_close_days_label.grid(row=3, column=0, padx=(20, 5), pady=(2, 10), sticky="e")

        # buttons
        self.button_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0)
        self.button_frame.grid(row=3, column=0, sticky='ew')
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.submit_button = customtkinter.CTkButton(self.button_frame, text="OK",
                                                     fg_color=self.theme.button_color,
                                                     text_color=self.theme.button_text_color,
                                                     width=self.theme.main_button_width
                                                     )
        self.submit_button.grid(row=0, column=1, padx=10, pady=10, )

        self.cancel_button = customtkinter.CTkButton(self.button_frame, text="Cancel",
                                                     fg_color=self.theme.button_color,
                                                     text_color=self.theme.button_text_color,
                                                     width=self.theme.main_button_width,
                                                     command=self.cancel
                                                     )
        self.cancel_button.grid(row=0, column=2, padx=10, pady=10, )

        self.apply_button = customtkinter.CTkButton(self.appearance_frame, text="Apply",
                                                    fg_color=self.theme.button_color,
                                                    text_color=self.theme.button_text_color,
                                                    width=self.theme.main_button_width
                                                    )
        self.apply_button.grid(row=6, column=1, padx=20, pady=20, )

    def update_icon_text(self):
        self.submit_button.configure(text_color=self.theme.button_text_color)
        self.apply_button.configure(text_color=self.theme.button_text_color)
        self.cancel_button.configure(text_color=self.theme.button_text_color)

    def update_button_color(self):
        self.submit_button.configure(fg_color=self.theme.button_color)
        self.apply_button.configure(fg_color=self.theme.button_color)
        self.icon_mode_switch.configure(button_color=self.theme.button_color)
        self.appearance_mode_switch.configure(button_color=self.theme.button_color)
        self.cancel_button.configure(fg_color=self.theme.button_color)

    def update_accent_color(self):
        self.icon_mode_switch.configure(progress_color=self.theme.accent_color)
        self.appearance_mode_switch.configure(progress_color=self.theme.accent_color)

    def get_button_color(self):
        pick_color = AskColor()
        pick_color.attributes('-topmost', True)
        color = pick_color.get()
        if color:
            self.button_color_button.configure(fg_color=color)

    def get_accent_color(self):
        pick_color = AskColor()
        pick_color.attributes('-topmost', True)
        color = pick_color.get()
        if color:
            self.accent_color_button.configure(fg_color=color)

    def cancel(self):
        self.settings_window.destroy()
