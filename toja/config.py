import configparser
from pathlib import Path
import platform


class Config:
    def __init__(self):
        self.system_platform = None
        self.base_dir = Path(__file__).resolve().parent
        self.config = configparser.ConfigParser()
        self.config_file = f'{self.base_dir}\\config.ini'
        self.config.read(self.config_file)
        # self.database = self.config['database']['database_dir']
        self.job_description_dir = self.config['database']['job_description_dir']
        self.database_name = self.config['database']['database_name']

    def is_user_new(self) -> bool:
        if self.config['user'].getboolean('new_user'):
            return True

    def initialize_user(self) -> None:
        database_dir = f'{self.base_dir}\\database\\'
        job_description = f'{self.base_dir}\\job_descriptions'
        self.config['database']['job_description_dir'] = job_description
        # self.config['database']['database_dir'] = database_dir
        self.config['user']['base_dir'] = str(self.base_dir)
        self.config['database']['database_name'] = 'sample_database.db'
        new_user = False
        self.config.set('user', 'new_user', str(new_user))
        with open(self.config_file, "w") as file:
            self.config.write(file)
        # self.database = self.config['database']['database_dir']
        self.job_description_dir = self.config['database']['job_description_dir']

    def set_database_name(self, db_name):
        self.config['database']['database_name'] = db_name
        with open(self.config_file, "w") as file:
            self.config.write(file)

    def get_database(self) -> Path:
        self.database_path = Path(*[self.base_dir, 'database', self.database_name])
        return self.database_path

    def get_job_description_dir(self) -> Path:
        return Path(self.job_description_dir)

    def get_users_system(self):
        self.system_platform = platform.system()
        return self.system_platform
