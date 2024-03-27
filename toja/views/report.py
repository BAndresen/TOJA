import customtkinter
from .theme import Theme
from .visualizations import DayEvent, PieEvent, KeywordBar, ProgressEvent


class Report:
    def __init__(self, root, theme: Theme):
        self.root = root
        self.theme = theme
        self.report_window = customtkinter.CTkToplevel(root)
        self.report_window.attributes('-topmost', 'true')

        self.report_window.title("Report")
        self.report_window.grid_columnconfigure(0, weight=1)
        self.report_window.grid_rowconfigure(1, weight=1)

        self.main_frame = customtkinter.CTkFrame(self.report_window, fg_color=self.theme.second_frame)
        self.main_frame.grid(row=1, column=0, padx=40, pady=(0, 40), sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        self.days_vs_event_frame = customtkinter.CTkFrame(self.main_frame, fg_color=self.theme.main_frame)
        self.days_vs_event_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.de_graph = DayEvent()
        self.de_graph.bg_color = self.theme.home_frame_background
        self.de_graph.face_color = self.theme.listbox_bg
        self.de_graph.text_color = self.theme.text_color
        self.de_graph.event_colors = self.theme.event_data

        self.event_pie_frame = customtkinter.CTkFrame(self.main_frame, fg_color=self.theme.main_frame)
        self.event_pie_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.pie_graph = PieEvent()
        self.pie_graph.bg_color = self.theme.home_frame_background
        self.pie_graph.face_color = self.theme.listbox_bg
        self.pie_graph.text_color = self.theme.text_color
        self.pie_graph.event_colors = self.theme.event_data

        self.keyword_graph_frame = customtkinter.CTkFrame(self.main_frame, fg_color=self.theme.main_frame)
        self.keyword_graph_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        self.keyword_graph = KeywordBar()
        self.keyword_graph.bg_color = self.theme.home_frame_background
        self.keyword_graph.face_color = self.theme.listbox_bg
        self.keyword_graph.text_color = self.theme.text_color

        self.left_combo_frame = customtkinter.CTkFrame(self.main_frame, fg_color=self.theme.main_frame)
        self.left_combo_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.left_combo_frame.grid_columnconfigure(0, weight=1)
        self.left_combo_frame.grid_rowconfigure(1, weight=1)

        self.info_frame = customtkinter.CTkFrame(self.left_combo_frame, fg_color=self.theme.main_frame)
        self.info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.user_name_label = customtkinter.CTkLabel(self.info_frame, text='User:',
                                                      font=self.theme.header_two_font
                                                      )
        self.user_name_label.grid(row=1, column=0, sticky='e', padx=5)
        self.user_name = customtkinter.CTkLabel(self.info_frame, text='',
                                                font=self.theme.header_two_font
                                                )
        self.user_name.grid(row=1, column=1)

        self.user_level_label = customtkinter.CTkLabel(self.info_frame, text='Job Hunter:',
                                                       font=self.theme.header_two_font
                                                       )
        self.user_level_label.grid(row=2, column=0, sticky='e', padx=5)
        self.user_level = customtkinter.CTkLabel(self.info_frame, text='',
                                                 font=self.theme.header_two_font
                                                 )
        self.user_level.grid(row=2, column=1)

        self.report_range = customtkinter.CTkLabel(self.report_window, text='',
                                                   font=self.theme.header_font
                                                   )
        self.report_range.grid(row=0, column=0, padx=10, pady=10)

        self.user_point_gain_label = customtkinter.CTkLabel(self.info_frame, text='Points Gained:',
                                                            font=self.theme.header_two_font
                                                            )
        self.user_point_gain_label.grid(row=5, column=0, sticky='e', padx=5)
        self.user_point_gain = customtkinter.CTkLabel(self.info_frame, text='',
                                                      font=self.theme.header_two_font
                                                      )
        self.user_point_gain.grid(row=5, column=1)

        self.progress_bar_frame = customtkinter.CTkFrame(self.left_combo_frame, fg_color=self.theme.main_frame)
        self.progress_bar_frame.grid(row=1, column=0, sticky="nsew")

        self.progress_graph = ProgressEvent()
        self.progress_graph.bg_color = self.theme.home_frame_background
        self.progress_graph.face_color = self.theme.listbox_bg
        self.progress_graph.text_color = self.theme.text_color
        self.progress_graph.event_colors = self.theme.event_data
