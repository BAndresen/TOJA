import tkinter
from typing import Union
from pathlib import Path
import datetime
import os
import string
from tkinter import messagebox, Toplevel


def validate_file_name(file_name: str) -> bool:
    """
    Checks string for non-valid file name characters
    :param file_name:
    :return:
    """
    valid_char = set(string.ascii_letters + string.digits + ' -_.')
    for char in file_name:
        if char not in valid_char:
            return False
    return True


def showerror(window: tkinter.Toplevel, error_message: str):
    window.attributes('-alpha', 0.5)
    messagebox.showerror(message=error_message)
    window.attributes('-alpha', 1)


def date_change(unit: int, day=False, hour=False, add=False, date_format='%Y-%m-%d', time_format='%I:%M%p') -> str:
    """
    Change day or hour by unit.

    Parameters:
        unit (int): The number of units (days or hours) to change by.
        day (bool, optional): If True, the function operates on days.
        hour (bool, optional): If True, the function operates on hours.
        add (bool, optional): If True, the unit time will be added instead of subtracted.

    Returns:
        str: A formatted string representing the previous time based on the unit change.

    Notes:
        The returned string is in '%Y-%m-%d' format if 'day' is True and in '%I:%M%p' format if 'hour' is True.
    """
    previous_time = None
    current_time = datetime.datetime.now()
    if day:
        day_change = datetime.timedelta(days=unit)
        if add:
            previous_time = (current_time + day_change).strftime(date_format)
        else:
            previous_time = (current_time - day_change).strftime(date_format)
    if hour:
        day_change = datetime.timedelta(hours=unit)
        if add:
            previous_time = (current_time + day_change).strftime(time_format)
        else:
            previous_time = (current_time - day_change).strftime(time_format)
    return previous_time


def load_job_file(file_list: list, parent_directory: Union[Path, str]) -> str:
    text = ''
    for files in file_list:
        if len(files[0]) == 1:
            f = files
        else:
            f = files[0]
        try:
            file_path = os.path.join(parent_directory, f)
            with open(file_path, 'r') as file:
                job = file.read()
            text += job

        except UnicodeDecodeError as e:
            file_path = os.path.join(parent_directory, f)
            with open(file_path, 'r', encoding='utf-8') as file:
                job = file.read()
            text += job
            print(f'Opened with Unicode utf-8 {f} {e}')

    return text.lower()



