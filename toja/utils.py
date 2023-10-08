from typing import Union
from pathlib import Path
import datetime
import os


def date_change(unit: int, day=False, hour=False, add=False) -> str:
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
            previous_time = (current_time + day_change).strftime('%Y-%m-%d')
        else:
            previous_time = (current_time - day_change).strftime('%Y-%m-%d')
    if hour:
        day_change = datetime.timedelta(hours=unit)
        if add:
            previous_time = (current_time + day_change).strftime('%I:%M%p')
        else:
            previous_time = (current_time - day_change).strftime('%I:%M%p')
    return previous_time


def load_job_file(file_list: list, parent_directory: Union[Path, str]) -> str:
    text = ''
    for files in file_list:
        try:
            file_path = os.path.join(parent_directory, files[0])
            with open(file_path, 'r') as file:
                job = file.read()
            text += job

        except UnicodeDecodeError:
            print(f'Unicode Error {files[0]}')
    return text.lower()
