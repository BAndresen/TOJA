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
        plt.xticks(rotation=30)
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

        # Define a function to format the label with total count and percentage
        def label_format(count, pct):
            return f'{int(count)}\n({pct:.1f}%)'

        ax.pie(values, labels=labels, labeldistance=1.1, autopct=lambda pct: label_format(sum(values) * pct / 100, pct), colors=colors, explode=explode,
               startangle=90,
               textprops={'color': self.text_color, 'fontsize': 10},
               wedgeprops={'edgecolor': self.text_color, 'linewidth': .8})

        plt.subplots_adjust(left=0.1, right=0.9)

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


class KeywordBar:
    def __init__(self):
        self.bg_color = ''
        self.face_color = ''
        self.text_color = ''

    def show_keyword_chart(self, frame: customtkinter.CTkFrame, data: list):
        fig, ax = plt.subplots(figsize=(4, 3), facecolor=self.bg_color)
        ax.set_facecolor(self.face_color)

        labels = [item[0] for item in data]
        values = [item[1] for item in data]

        # Create horizontal bar chart
        ax.barh(labels, values, color='skyblue')

        # Set axis labels and title
        ax.set_title('Top Keywords')

        # Invert y-axis to display categories from top to bottom
        ax.invert_yaxis()
        ax.tick_params(axis='both', which='major', labelsize=10)

        # Adjust layout
        plt.subplots_adjust(left=0.15, right=0.9)

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

    def show_bar_chart(self, frame: tk.Frame, data: dict):
        fig, ax = plt.subplots(figsize=(6, 4), facecolor=self.bg_color)
        ax.set_facecolor(self.face_color)

        events = list(data.keys())
        percent_changes = list(data.values())

        colors = [self.event_colors.get(event, 'gray') for event in events]

        bars = ax.barh(events, percent_changes, color=colors)

        # Add zero line
        ax.axvline(0, color='black', linewidth=0.5)

        # Add labels
        for bar in bars:
            width = bar.get_width()
            ax.text(width, bar.get_y() + bar.get_height()/2, f'{width}%', ha='left' if width > 0 else 'right', va='center',
                    color=self.text_color)

        ax.set_xlabel('Percent Change')
        ax.set_title('Percent Change of Events')
        ax.grid(axis='x', linestyle='--', alpha=0.7)

        plt.subplots_adjust(left=0.1, right=0.9)

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)