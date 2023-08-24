import configparser
from pathlib import Path


class Config:
    def __init__(self):
        self.base_dir = Path(__file__).resolve().parent
        # self.grandparent_dir = Path(self.base_dir).resolve().parent
        self.config = configparser.ConfigParser()
        self.config_file = f'{self.base_dir}\\config.ini'
        self.config.read(self.config_file)
        self.database = self.config['database']['database_path']
        self.job_description_dir = self.config['database']['job_description_dir']

    def is_user_new(self) -> bool:
        if self.config['user'].getboolean('new_user'):
            return True

    def initialize_user(self) -> None:
        database = f'{self.base_dir}\\database\\toja_database.db'
        job_description = f'{self.base_dir}\\job_descriptions'
        self.config['database']['job_description_dir'] = job_description
        self.config['database']['database_path'] = database
        self.config['user']['base_dir'] = str(self.base_dir)
        # self.config['user']['grandparent_dir'] = str(self.grandparent_dir)
        new_user = False
        self.config.set('user', 'new_user', str(new_user))
        with open(self.config_file, "w") as file:
            self.config.write(file)
        self.database = self.config['database']['database_path']
        self.job_description_dir = self.config['database']['job_description_dir']

    def get_database(self) -> Path:
        return Path(self.database)

    def get_job_description_dir(self) -> Path:
        return Path(self.job_description_dir)
