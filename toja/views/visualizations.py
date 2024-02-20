import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class DayEvent:
    def __init__(self):
        self.categories = []
        self.events1 = []  # Values for the first category
        self.events2 = []  # Values for the second category
        self.bg_color = ''
        self.face_color = ''

    def day_event_graph(self, frame):
        fig, ax = plt.subplots(figsize=(6, 4),facecolor=self.bg_color)

        # Data for the stacked bar chart

        # Create stacked bar chart
        bar_width = 0.35
        ind = np.arange(len(self.categories))
        ax.bar(ind, self.events1, bar_width, label='Group 1')
        ax.bar(ind, self.events2, bar_width, bottom=self.events1, label='Group 2')

        # ax.set_xlabel('Categories')
        # ax.set_ylabel('Values')
        # ax.set_title('Stacked Bar Chart')
        ax.set_xticks(ind)
        ax.set_xticklabels(self.categories)
        ax.legend()

        # Set background color of the graph
        ax.set_facecolor(self.face_color)  # Light gray background color

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
