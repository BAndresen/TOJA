import configparser
from pathlib import Path
import platform
import os
import customtkinter

import toja.constants as constant
from toja.views.theme import Theme


class Config:
    def __init__(self, theme: Theme):
        self.icon_mode = None
        self.appearance_mode = None
        self.system_platform = None
        self.theme = theme
        self.base_dir = Path(__file__).resolve().parent
        self.job_description_parent = os.path.join(self.base_dir, constant.JOB_DESCRIPTION_DIRECTORY)
        self.database_path = os.path.join(self.base_dir, constant.DATABASE_DIRECTORY, constant.DATABASE_NAME)

        self.config_parser = configparser.ConfigParser()
        self.config_file = os.path.join(self.base_dir, constant.CONFIG_FILE)
        self.config_parser.read(self.config_file)
        self.user_name = self.config_parser['user']['name']
        self.set_theme()
        if self.get_appearance_mode() == "Light":
            customtkinter.set_appearance_mode('Light')
        else:
            customtkinter.set_appearance_mode('Dark')

    def set_theme(self):
        self.appearance_mode = self.get_appearance_mode()
        self.set_appearance_mode()
        self.set_font()
        self.set_button_color()
        self.set_accent_color()
        self.set_icon_mode()

    def is_user_new(self) -> bool:
        if self.config_parser['user'].getboolean('new_user'):
            return True

    def initialize_user(self) -> None:
        new_user = False
        self.config_parser.set('user', 'new_user', str(new_user))
        with open(self.config_file, "w") as file:
            self.config_parser.write(file)

    def update_user_name(self, user_name: str):
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

    def update_keywords(self, keyword_num: str, job_description: bool = False, resume: bool = False):
        if job_description:
            self.config_parser['global_settings']['num_keyword_job_description'] = keyword_num
        if resume:
            self.config_parser['global_settings']['num_keyword_resume'] = keyword_num
        with open(self.config_file, "w") as file:
            self.config_parser.write(file)

    def get_appearance_mode(self) -> str:
        return self.config_parser['theme']['appearance_mode']

    def update_appearance_mode(self, mode: str):
        self.config_parser['theme']['appearance_mode'] = mode
        with open(self.config_file, "w") as file:
            self.config_parser.write(file)

    def get_font(self) -> str:
        return self.config_parser['theme']['font']

    def set_font(self):
        self.theme.main_font = self.get_font()

    def get_button_color(self) -> str:
        return self.config_parser['theme']['button_color']

    def set_button_color(self):
        self.theme.button_color = self.get_button_color()

    def update_button_color(self, color: str):
        self.config_parser['theme']['button_color'] = color
        with open(self.config_file, "w") as file:
            self.config_parser.write(file)

    def get_accent_color(self) -> str:
        return self.config_parser['theme']['accent_color']

    def set_accent_color(self):
        self.theme.accent_color = self.get_accent_color()

    def update_accent_color(self, color: str):
        self.config_parser['theme']['accent_color'] = color
        with open(self.config_file, "w") as file:
            self.config_parser.write(file)

    def get_icon_mode(self) -> str:
        return self.config_parser['theme']['icon_mode']

    def update_icon_mode(self, mode):
        self.config_parser['theme']['icon_mode'] = mode
        with open(self.config_file, "w") as file:
            self.config_parser.write(file)

    def set_icon_mode(self):
        self.icon_mode = self.get_icon_mode()
        self.set_button_text_color(self.icon_mode)
        if self.icon_mode == 'Light':
            self.theme.icon_contact = constant.CONTACT_WHITE
            self.theme.icon_delete = constant.DELETE_WHITE
            self.theme.icon_event = constant.EVENT_WHITE
            self.theme.icon_pencil = constant.PENCIL_WHITE
            self.theme.icon_plus = constant.PLUS_WHITE
            self.theme.icon_writing = constant.WRITING_WHITE
            self.theme.icon_questions = constant.QUESTIONS
            self.theme.icon_visible = constant.VISIBLE

        elif self.icon_mode == 'Dark':
            self.theme.icon_contact = constant.CONTACT
            self.theme.icon_delete = constant.DELETE
            self.theme.icon_event = constant.EVENT
            self.theme.icon_pencil = constant.PENCIL
            self.theme.icon_plus = constant.PLUS
            self.theme.icon_writing = constant.WRITING
            self.theme.icon_questions = constant.QUESTIONS_WHITE
            self.theme.icon_visible = constant.VISIBLE_WHITE

    def set_appearance_mode(self):
        if self.appearance_mode == "Dark":
            self.set_dark_mode()
        else:
            self.set_light_mode()

    def set_dark_mode(self):
        self.theme.home_frame_background = 'grey20'
        self.theme.text_color = 'grey86'
        self.theme.listbox_bg = 'grey17'
        self.theme.home_frame_selected = 'grey14'

        self.theme.main_frame = 'grey14'
        self.theme.second_frame = 'grey17'

        self.theme.icon_home = constant.HOME_WHITE
        self.theme.icon_keyword = constant.KEYWORD_WHITE
        self.theme.icon_main_event = constant.EVENT_HOME_WHITE
        self.theme.icon_main_contact = constant.CONTACT_HOME_WHITE

    def set_light_mode(self):
        self.theme.home_frame_background = 'grey86'
        self.theme.text_color = 'grey17'
        self.theme.listbox_bg = 'grey86'
        self.theme.home_frame_selected = 'grey92'

        self.theme.main_frame = 'grey92'
        self.theme.second_frame = 'grey86'

        self.theme.icon_home = constant.HOME
        self.theme.icon_keyword = constant.KEYWORD
        self.theme.icon_main_event = constant.EVENT_HOME
        self.theme.icon_main_contact = constant.CONTACT_HOME

    def set_button_text_color(self, mode: str):
        if mode == 'Light':
            self.theme.button_text_color = 'grey86'
        elif mode == 'Dark':
            self.theme.button_text_color = 'grey17'
