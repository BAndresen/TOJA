# testing
ESCAPE_CHAR = ['\n', '\r', '\t', '\\', '\'', '\"', '\a', '\b', '\f', '\v', '\0', '\ooo', ]
NOT_ASCII = ['À', 'ñ', 'Ç', 'β', 'Ω', 'Д', 'ж', 'Я', '你', '世', 'こんにちは', 'テスト', '😁', '🌍', '∑', '∫', '€', '¥',
             '₽', '→', '⇨', '◆', '△', '✂', '✈', '♪', '♫']
EDGE_CHAR = ['0', '', ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']',
             '|', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '~', '`']

# Config
CONFIG_FILE = 'config.ini'
DATABASE_DIRECTORY = 'database'
DATABASE_NAME = 'toja_database.db'
APPLICATION_DIRECTORY = 'toja'
JOB_DESCRIPTION_DIRECTORY = 'job_descriptions'
SAMPLE_USER_NAME = 'Sample'
SAMPLE_JOB = 'sample_job.sql'
SAMPLE_CONTACT = 'sample_contact.sql'
EXPORT_JOB_CSV = 'exported_job_data.csv'
EXPORT_EVENT_CSV = 'exported_event_data.csv'
EXPORT_CONTACT_CSV = 'exported_contact_data.csv'

# Job Entry Variables
EARNING_TYPE = ['Annual', 'Monthly', 'Hourly', 'Contract', 'None']
WORK_TYPE = ['Remote', 'Hybrid', 'Onsite', 'None']
SALARY_TYPE = ['Full-Time', 'Part-Time', 'Contract', 'Freelance']
EVENT_TYPE = ['applied', 'prospect', 'follow up', 'workshop', 'meeting', 'networking', 'interview', 'offer',
              'portfolio_project',
              'rejected']


# Listbox and Textbox ranges
START_RANGE_LISTBOX = '0'
END_RANGE_LISTBOX = 'end'
START_RANGE_TEXTBOX = '1.0'
END_RANGE_TEXTBOX = 'end-1c'

# Docs
TOJA_GITHUB_URL = 'https://github.com/BAndresen/TOJA'

# Keywords
SPACY_NLP_MODEL = "en_core_web_sm"  # https://spacy.io/models
PART_OF_SPEECH = ["NOUN", "PROPN"]  # https://spacy.io/usage/spacy-101#section-features

CURRENT_TIME_FORMAT = '%I:%M%p'
CURRENT_DATE_FORMAT = '%Y-%m-%d'

# icons
ICON_FILE_DIRECTORY = 'icons'
CONTACT = 'contact.png'
CONTACT_WHITE = 'contact_white.png'
DELETE = 'delete.png'
DELETE_WHITE = 'delete_white.png'
EVENT = 'event.png'
EVENT_WHITE = 'event_white.png'
PENCIL = 'pencil.png'
PENCIL_WHITE = 'pencil_white.png'
PLUS = 'plus_thin.png'
PLUS_WHITE = 'plus_thin_white.png'
WRITING = 'writing.png'
WRITING_WHITE = 'writing_white.png'
HOME = 'home.png'
HOME_WHITE = 'home_white.png'
KEYWORD = 'keyword.png'
KEYWORD_WHITE = 'keyword_white.png'
QUESTIONS = 'question.png'
QUESTIONS_WHITE = 'question_white.png'
VISIBLE = 'visible.png'
VISIBLE_WHITE = 'visible_white.png'
EVENT_HOME = 'event_home.png'
EVENT_HOME_WHITE = 'event_home_white.png'
CONTACT_HOME = 'contact_home.png'
CONTACT_HOME_WHITE = 'contact_home_white.png'

WELCOME_MESSAGE = "Welcome To TOJA! \n\n Let's Track and Optimize your Job Application Process"

# theme
DARK_MODE = 'Dark'
LIGHT_MODE = 'Light'

HOME_FRAME_BG_DARK = '#2b2b2b'  # 'grey17'
TEXT_DARK = '#dbdbdb'  # 'grey86'
LISTBOX_BG_DARK = '#333333'  # 'grey20'
MAIN_FRAME_DARK = '#242424'  # 'grey14'
SECOND_FRAME_DARK = '#2b2b2b'  # 'grey17'
BUTTON_TEXT_DARK = '#2b2b2b'  # 'grey86'

HOME_FRAME_BG = '#d9d9d9'  # grey85
TEXT = '#2b2b2b'
LISTBOX_BG = '#e5e5e5'  # 'grey90'
MAIN_FRAME = '#ebebeb'  # 'grey92'
SECOND_FRAME = '#d9d9d9'  # 'grey85'
BUTTON_TEXT = '#dbdbdb'  # 'grey17'
