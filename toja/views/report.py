import customtkinter
from .theme import Theme
from .visualizations import DayEvent


class Report:
    def __init__(self, root, theme: Theme):
        self.root = root
        self.theme = theme
        self.report_window = customtkinter.CTkToplevel(root)
        self.report_window.attributes('-topmost', 'true')

        self.report_window.title("Report")

        self.main_frame = customtkinter.CTkFrame(self.report_window, fg_color=self.theme.second_frame)
        self.main_frame.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")
        self.report_window.grid_columnconfigure(0,weight=1)
        self.report_window.grid_rowconfigure(0,weight=1)

        self.de_graph = DayEvent()
        self.de_graph.bg_color = self.theme.home_frame_background
        self.de_graph.face_color = self.theme.listbox_bg
        self.de_graph.text_color = self.theme.text_color
        self.de_graph.event_colors = self.theme.event_data

