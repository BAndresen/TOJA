from typing import Union
from pathlib import Path


def get_file_from_path(file_path: Union[str, Path], file_extension=False, forward_slash=False) -> str:
    """
    :param file_path: (Union[str, Path]): The path to the file from which the name needs to be extracted.
    :param file_extension: (bool, optional): If True, returns the full file name with extension.
                                     If False (default), returns the clean file name without extension.
    :param forward_slash: (bool, optional): set to True for path forward slash
    :return: str: The clean file name extracted from the provided file path.
    """
    if not forward_slash:
        file = str(file_path).split('\\')
    else:
        file = str(file_path.split('/'))
    clean_file = file[-1]
    if not file_extension:
        without_file_extension = clean_file.split('.')[0]
        clean_file = without_file_extension
    return clean_file

