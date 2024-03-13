import customtkinter
from .theme import Theme
from tkcalendar import DateEntry


# from customtkinter.windows.widgets.font import ctk_font


class GenerateReport:
    def __init__(self, root, theme: Theme):
        self.root = root
        self.theme = theme
        self.generate_report_window = customtkinter.CTkToplevel(root)
        self.generate_report_window.attributes('-topmost', 'true')

        self.generate_report_window.title("Generate Report")

        self.main_frame = customtkinter.CTkFrame(self.generate_report_window, fg_color=self.theme.second_frame)
        self.main_frame.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")

        self.date_range_frame = customtkinter.CTkFrame(self.main_frame, fg_color=self.theme.main_frame)
        self.date_range_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.start_date_label = customtkinter.CTkLabel(self.date_range_frame, text="Start:")
        self.start_date_label.grid(row=0, column=0, padx=10, pady=10)

        self.start_date = DateEntry(self.date_range_frame, selectmode='day', font=("roboto", "12"),
                                    date_pattern="yyyy-mm-dd")
        self.start_date.grid(row=0, column=1)

        self.end_date_label = customtkinter.CTkLabel(self.date_range_frame, text="End:")
        self.end_date_label.grid(row=0, column=2, padx=10, pady=10)

        self.end_date = DateEntry(self.date_range_frame, selectmode='day', font=("roboto", "12"),
                                  date_pattern="yyyy-mm-dd")
        self.end_date.grid(row=0, column=3, padx=(0, 10), pady=10)

        # buttons
        self.button_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0)
        self.button_frame.grid(row=1, column=0, sticky='ew')
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.generate_button = customtkinter.CTkButton(self.button_frame, text="Generate",
                                                       fg_color=self.theme.button_color,
                                                       text_color=self.theme.button_text_color,
                                                       width=self.theme.main_button_width
                                                       )
        self.generate_button.grid(row=0, column=1, padx=10, pady=10, )

        self.cancel_button = customtkinter.CTkButton(self.button_frame, text="Cancel",
                                                     fg_color=self.theme.button_color,
                                                     text_color=self.theme.button_text_color,
                                                     width=self.theme.main_button_width,
                                                     command=self.cancel
                                                     )
        self.cancel_button.grid(row=0, column=2, padx=10, pady=10, )

    def cancel(self):
        self.generate_report_window.destroy()
