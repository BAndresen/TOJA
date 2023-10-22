
import toja.constants as constant


class Theme:
    def __init__(self):
        self.listbox_bg = ''
        self.text_color = ''
        self.frame1_color = ''
        self.main_font = ''

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

    def set_dark_mode(self):
        self.frame1_color = 'gray20'
        self.text_color = 'grey86'
        self.listbox_bg = 'grey17'
        self.icon_contact = constant.CONTACT_WHITE
        self.icon_delete = constant.DELETE_WHITE
        self.icon_event = constant.EVENT_WHITE
        self.icon_pencil = constant.PENCIL_WHITE
        self.icon_plus = constant.PLUS_WHITE
        self.icon_writing = constant.WRITING_WHITE

    def set_light_mode(self):
        self.frame1_color = 'gray80'
        self.text_color = 'gray17'
        self.listbox_bg = 'gray86'
        self.icon_contact = constant.CONTACT
        self.icon_delete = constant.DELETE
        self.icon_event = constant.EVENT
        self.icon_pencil = constant.PENCIL
        self.icon_plus = constant.PLUS
        self.icon_writing = constant.WRITING













