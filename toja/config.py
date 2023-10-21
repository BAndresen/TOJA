import configparser
from pathlib import Path
import platform
import os
import customtkinter

import toja.constants as constant
from toja.views.theme import Theme


class Config:
    def __init__(self, theme: Theme):
        self.system_platform = None
        self.theme = theme
        self.base_dir = Path(__file__).resolve().parent
        self.job_description_parent = os.path.join(self.base_dir, constant.JOB_DESCRIPTION_DIRECTORY)
        self.database_path = os.path.join(self.base_dir, constant.DATABASE_DIRECTORY, constant.DATABASE_NAME)

        self.config_parser = configparser.ConfigParser()
        self.config_file = os.path.join(self.base_dir, constant.CONFIG_FILE)
        self.config_parser.read(self.config_file)
        self.user_name = self.config_parser['user']['name']
        self.appearance_mode = self.get_appearance_mode()
        self.set_appearance_mode()

    def is_user_new(self) -> bool:
        if self.config_parser['user'].getboolean('new_user'):
            return True

    def initialize_user(self) -> None:
        new_user = False
        self.config_parser.set('user', 'new_user', str(new_user))
        with open(self.config_file, "w") as file:
            self.config_parser.write(file)

    def set_user_name(self, user_name: str):
        self.config_parser['user']['name'] = user_name
        with open(self.config_file, "w") as file:
            self.config_parser.write(file)
        self.user_name = user_name

    def get_users_system(self) -> str:
        self.system_platform = platform.system()
        return self.system_platform

    def get_num_keywords(self, job_description: bool = False, resume: bool = False) -> int:
        if job_description:
            return int(self.config_parser['global_settings']['num_keyword_job_description'])
        if resume:
            return int(self.config_parser['global_settings']['num_keyword_resume'])

    def get_appearance_mode(self) -> str:
        return self.config_parser['theme']['appearance_mode']

    def set_appearance_mode(self):
        customtkinter.set_appearance_mode(self.appearance_mode)
        if self.appearance_mode == "Dark":
            self.theme.set_dark_mode()
        else:
            self.theme.set_light_mode()
