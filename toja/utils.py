import tkinter
from typing import Union
from pathlib import Path
from datetime import datetime, timedelta
import os
import string
from tkinter import messagebox, Toplevel
from loguru import logger

logger.add('log.txt')


def get_past_dates(today: datetime, num_of_days: int) -> list:
    past_week_dates = [today - timedelta(days=i) for i in range(int(num_of_days), -1, -1)]
    past_week_dates.append(today - timedelta(days=1))
    past_week_dates.append(today)
    clean_format = [date.strftime('%Y-%m-%d') for date in past_week_dates]

    logger.debug(f'returned past dates {clean_format}')
    return clean_format


def get_dates_between(start_date: datetime, end_date: datetime) -> list:
    dates_between = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
    clean_format = [date.strftime('%Y-%m-%d') for date in dates_between]
    return clean_format


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
    current_time = datetime.now()
    if day:
        day_change = timedelta(days=unit)
        if add:
            previous_time = (current_time + day_change).strftime(date_format)
        else:
            previous_time = (current_time - day_change).strftime(date_format)
    if hour:
        day_change = timedelta(hours=unit)
        if add:
            previous_time = (current_time + day_change).strftime(time_format)
        else:
            previous_time = (current_time - day_change).strftime(time_format)
    return previous_time


def load_job_file(file_list: list, parent_directory: Union[Path, str]) -> str:
    text = ''
    for files in file_list:
        try:
            if len(files[0]) == 1:
                f = files
            else:
                f = files[0]
        except TypeError as e:
            logger.error(e)

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
            logger.info(f'Opened with Unicode utf-8 {f} {e}')

        except UnboundLocalError as e:
            logger.error(f'Error Null File {e}')

    return text.lower()
