import tkinter as tk
from tkinter import ttk
from loguru import logger

import customtkinter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class DayEvent:
    def __init__(self):
        self.dates = []
        self.data = {}
        self.events = set()
        self.bg_color = ''
        self.face_color = ''
        self.text_color = ''
        self.fig = None
        self.ax = None
        self.event_colors = {}

    def day_event_graph(self, frame: customtkinter.CTkFrame, data: dict, events: set):
        self.data = data
        self.events = events

        logger.debug(f'data:{data}')
        logger.debug(f'events:{events}')

        self.fig, self.ax = plt.subplots(figsize=(4, 3), facecolor=self.bg_color, layout='tight')
        self.ax.set_facecolor(self.face_color)

        self._plot_graph(data, events)

        # plt.xticks(rotation=25)
        plt.legend(fontsize=9)

        self._configure_spines()

        plt.subplots_adjust(left=0.1, right=0.9)

        self._draw_canvas(frame)

    def update_graph(self, data: dict, events: set):
        self.data = data
        self.events = events
        self.ax.clear()
        self._plot_graph(data, events)

        self._configure_spines()

        plt.subplots_adjust(left=0.1, right=0.9)
        # plt.xticks(rotation=30)
        plt.legend(fontsize=9)

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def _plot_graph(self, data: dict, events: set):
        dates = list(data.keys())
        event_counts = {event: [0] * len(dates) for event in events}

        if len(dates) > 90:
            plt.tick_params(axis='x', labelsize=6)
        else:
            plt.tick_params(axis='x', labelsize=8)

        plt.yticks(color=self.text_color)
        plt.xticks(color=self.text_color)
        # plt.xticks(rotation=30)
        self.ax.tick_params(axis='x', colors=self.text_color)
        self.ax.tick_params(axis='y', colors=self.text_color)

        plt.tick_params(axis='y', labelsize=8)

        for i, date in enumerate(dates):
            for event, count in data[date]:
                event_counts[event][i] += count

        bottom = None

        for event in events:
            color = self.event_colors.get(event, None)
            if color is None:
                color = 'gray'  # Default color for events not in event_colors
            if bottom is None:
                self.ax.bar(dates, event_counts[event], label=event, width=.5, color=color)
                bottom = event_counts[event]
            else:
                self.ax.bar(dates, event_counts[event], bottom=bottom, label=event, width=.5, color=color)
                bottom = [bottom[i] + event_counts[event][i] for i in range(len(dates))]

    def _configure_spines(self):
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)
        self.ax.spines['left'].set_visible(False)
        plt.xticks(rotation=40)
        plt.legend(fontsize=9, facecolor=self.bg_color, edgecolor=self.face_color, labelcolor=self.text_color)

    def _draw_canvas(self, frame):
        canvas = FigureCanvasTkAgg(self.fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def toggle_color_scheme(self, frame):
        self.day_event_graph(frame, self.data, self.events)


class PieEvent:
    def __init__(self):
        self.bg_color = ''
        self.face_color = ''
        self.text_color = ''
        self.event_colors = {}

    def show_pie_chart(self, frame: customtkinter.CTkFrame, data: dict):
        fig, ax = plt.subplots(figsize=(6, 4), facecolor=self.bg_color)
        ax.set_facecolor(self.face_color)

        labels = list(data.keys())
        values = list(data.values())

        colors = [self.event_colors.get(label, 'gray') for label in labels]
        explode = [0.1 for i in range(len(labels))]

        ax.pie(values, labels=labels, labeldistance=1.1,
               autopct='%1.1f%%',
               colors=colors, explode=explode,
               startangle=90,
               textprops={'color': self.text_color, 'fontsize': 9},
               wedgeprops={'edgecolor': self.text_color, 'linewidth': .8})

        plt.subplots_adjust(left=0.2, right=0.8)

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


class KeywordBar:
    def __init__(self):
        self.bg_color = ''
        self.face_color = ''
        self.text_color = ''

    def show_keyword_chart(self, frame: customtkinter.CTkFrame, data: list):
        fig, ax = plt.subplots(figsize=(4, 3), facecolor=self.bg_color,)
        ax.set_facecolor(self.face_color)

        labels = [item[0] for item in data]
        values = [item[1] for item in data]

        # Create horizontal bar chart
        ax.barh(labels, values, color='skyblue',)

        # Set axis labels and title
        ax.set_title('Top Keywords', color=self.text_color)

        # Invert y-axis to display categories from top to bottom
        ax.invert_yaxis()
        ax.tick_params(axis='both', which='major', labelsize=9, colors=self.text_color)

        # Adjust layout
        plt.subplots_adjust(left=0.35, right=0.9)

        # Draw canvas on tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


class ProgressEvent:
    def __init__(self):
        self.bg_color = ''
        self.face_color = ''
        self.text_color = ''
        self.event_colors = {}
        self.ax = None

    def show_bar_chart(self, frame: tk.Frame, data: dict):
        fig, ax = plt.subplots(figsize=(4, 4), facecolor=self.bg_color)
        ax.set_facecolor(self.face_color)
        self.ax= ax

        events = list(data.keys())
        changes = list(data.values())

        colors = [self.event_colors.get(event, 'gray') for event in events]

        bars = ax.barh(events,
                       changes,
                       color=colors)

        # Calculate the maximum absolute change to set the limits of the x-axis symmetrically around 0
        max_change = max(abs(change) for change in changes)
        ax.set_xlim(-max_change, max_change)

        # Add zero line
        ax.axvline(0, color='black', linewidth=0.1)

        ax.set_xlabel('Change')
        # ax.set_title('Change of Events')
        ax.tick_params(axis='both', labelsize=9, colors=self.text_color)
        ax.grid(axis='x', linestyle='--', alpha=0.7)

        plt.subplots_adjust(left=0.35,
                            right=0.9
                            )

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def update_title(self, title: str):
        if self.ax:
            self.ax.set_title(title, fontsize=10, color=self.text_color)
