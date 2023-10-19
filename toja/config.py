import configparser
from pathlib import Path
import platform
import os

import toja.constants as constant


class Config:
    def __init__(self):
        self.system_platform = None
        self.base_dir = Path(__file__).resolve().parent
        self.job_description_parent = os.path.join(self.base_dir, constant.JOB_DESCRIPTION_DIRECTORY)
        self.database_path = os.path.join(self.base_dir, constant.DATABASE_DIRECTORY, constant.DATABASE_NAME)

        self.config = configparser.ConfigParser()
        self.config_file = f'{self.base_dir}\\{constant.CONFIG_FILE}'
        self.config.read(self.config_file)
        self.user_name = self.config['user']['name']

    def is_user_new(self) -> bool:
        if self.config['user'].getboolean('new_user'):
            return True

    def initialize_user(self) -> None:
        new_user = False
        self.config.set('user', 'new_user', str(new_user))
        with open(self.config_file, "w") as file:
            self.config.write(file)

    def set_user_name(self, user_name: str):
        self.config['user']['name'] = user_name
        with open(self.config_file, "w") as file:
            self.config.write(file)
        self.user_name = user_name

    def get_users_system(self) -> str:
        self.system_platform = platform.system()
        return self.system_platform
