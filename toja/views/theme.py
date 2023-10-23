import toja.constants as constant


class Theme:
    def __init__(self):
        self.listbox_bg = ''
        self.text_color = ''
        self.frame1_color = ''
        self.main_font = ''
        self.button_text_color = ''

        # icons
        self.icon_contact = ''
        self.icon_delete = ''
        self.icon_event = ''
        self.icon_pencil = ''
        self.icon_plus = ''
        self.icon_writing = ''

        # button color
        self.button_color = ''

        # accent_color
        self.accent_color = ''

        # icons
        self.icon_contact = ''
        self.icon_delete = ''
        self.icon_event = ''
        self.icon_pencil = ''
        self.icon_plus = ''
        self.icon_writing = ''

    def set_dark_mode(self):
        self.frame1_color = 'grey20'
        self.text_color = 'grey86'
        self.listbox_bg = 'grey17'

    def set_light_mode(self):
        self.frame1_color = 'grey80'
        self.text_color = 'grey17'
        self.listbox_bg = 'grey86'

    def set_button_text_color(self, mode: str):
        if mode == 'Light':
            self.button_text_color = 'grey86'
        elif mode == 'Dark':
            self.button_text_color = 'grey17'
