import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class DayEvent:

    def day_event_graph(self, frame):
        fig, ax = plt.subplots(figsize=(6, 4))

        # Data for the stacked bar chart
        categories = ['Category 1', 'Category 2', 'Category 3']
        values1 = [15, 30, 45]  # Values for the first category
        values2 = [10, 20, 30]  # Values for the second category

        # Create stacked bar chart
        bar_width = 0.35
        ind = np.arange(len(categories))
        ax.bar(ind, values1, bar_width, label='Group 1')
        ax.bar(ind, values2, bar_width, bottom=values1, label='Group 2')

        ax.set_xlabel('Categories')
        ax.set_ylabel('Values')
        ax.set_title('Stacked Bar Chart')
        ax.set_xticks(ind)
        ax.set_xticklabels(categories)
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
