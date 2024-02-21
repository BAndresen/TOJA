import tkinter as tk
from tkinter import ttk

import customtkinter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DayEvent:
    def __init__(self):
        self.dates = []
        self.data = []
        self.bg_color = ''
        self.face_color = ''

    def day_event_graph(self, frame: customtkinter.CTkFrame, data: dict, events: set):

        fig, ax = plt.subplots(figsize=(4, 4), facecolor=self.bg_color)
        ax.set_facecolor(self.face_color)

        dates = list(data.keys())
        event_counts = {event: [0] * len(dates) for event in events}

        for i, date in enumerate(dates):
            for event, count in data[date]:
                event_counts[event][i] += count

        bottom = None

        for event in events:
            if bottom is None:
                ax.bar(dates, event_counts[event], label=event, width=.5)
                bottom = event_counts[event]
            else:
                ax.bar(dates, event_counts[event], bottom=bottom, label=event, width=.5)
                bottom = [bottom[i] + event_counts[event][i] for i in range(len(dates))]

        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        # Set font size for x-axis label

        # Set font size for tick labels on x-axis
        plt.tick_params(axis='x', labelsize=8)

        # Set font size for tick labels on y-axis
        plt.tick_params(axis='y', labelsize=8)
        # plt.set_facecolor(self.face_color)  # Light gray background color

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
