import tkinter
import customtkinter

from .theme import Theme
import toja.constants as constant


class WelcomeUser:
    def __init__(self, root, theme: Theme):
        self.root = root
        self.theme = theme
        self.welcome_window = customtkinter.CTkToplevel(root)
        self.welcome_window.attributes('-topmost', 'true')
        self.welcome_window.title("Welcome")

        self.welcome_frame = customtkinter.CTkFrame(self.welcome_window)
        self.welcome_frame.grid(row=0, column=0, padx=20, pady=20)

        self.welcome_label = customtkinter.CTkLabel(self.welcome_frame, text=constant.WELCOME_MESSAGE)
        self.welcome_label.grid(row=0, column=0, padx=20, pady=20)

        self.radiobutton_frame = customtkinter.CTkFrame(self.welcome_frame)
        self.radiobutton_frame.grid(row=1, column=0, padx=(20, 20), pady=20, sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame,
                                                        text="Would you like to create a new user or try a sample user?")
        self.label_radio_group.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
                                                           value=0, text="Sample User",
                                                           border_width_checked=4,
                                                           fg_color=self.theme.accent_color
                                                           )
        self.radio_button_1.grid(row=1, column=1, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
                                                           value=1, text='New User',
                                                           border_width_checked=4,
                                                           fg_color=self.theme.accent_color
                                                           )
        self.radio_button_2.grid(row=2, column=1, pady=10, padx=20, sticky="n")

        self.radio_button_2.bind('<Button-1>', self.start_new)
        self.radio_button_1.bind('<Button-1>', self.destroy)

        self.start_button = customtkinter.CTkButton(self.welcome_frame, text="Start",
                                                    fg_color=self.theme.button_color,
                                                    text_color=self.theme.button_text_color,
                                                    width=self.theme.main_button_width

                                                    )
        self.start_button.grid(row=3, column=0, padx=20, pady=(65, 19))

    def start_new(self, event):
        self.start_button.grid(pady=(19, 20))
        self.name_entry = customtkinter.CTkEntry(self.welcome_frame)
        self.name_entry.grid(row=2, column=0, padx=10, pady=9)
        self.database_name_label = customtkinter.CTkLabel(self.welcome_frame, text="Username:")
        self.database_name_label.grid(row=2, column=0, padx=(40, 0), pady=9, sticky="w")

    def destroy(self, event):
        self.database_name_label.destroy()
        self.name_entry.destroy()
        self.start_button.grid(pady=(65, 20))
