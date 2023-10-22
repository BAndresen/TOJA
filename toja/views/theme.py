
class Theme:
    def __init__(self):
        self.listbox_bg = ''
        self.text_color = ''
        self.frame1_color = ''
        self.main_font = ''

    def set_dark_mode(self):
        self.frame1_color = 'gray20'
        self.text_color = 'grey20'
        self.listbox_bg = 'grey90'

    def set_light_mode(self):
        self.frame1_color = 'gray80'
        self.text_color = 'grey90'
        self.listbox_bg = 'grey20'


