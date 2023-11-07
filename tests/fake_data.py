from faker import Faker
import random
import string
import datetime

import toja.constants as constant
from toja.utils import date_change


class FakeData:
    def __init__(self):
        fake = Faker()
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.points = random.randint(0, 100)
        self.phone = fake.phone_number()
        self.email = fake.email()
        self.position = fake.job()
        self.event_note = fake.paragraph(nb_sentences=1)
        self.job_note = fake.paragraph(nb_sentences=1)
        self.company = fake.company()
        self.location = fake.city()
        self.salary_top = random.randint(1, 1_000_000)
        self.salary_bottom = random.randint(1, self.salary_top)
        self.salary_type = random.choice(constant.SALARY_TYPE)
        self.event_type = random.choice(constant.EVENT_TYPE)
        self.earning_type = random.choice(constant.EARNING_TYPE)
        self.work_type = random.choice(constant.WORK_TYPE)
        self.website = fake.uri()
        self.resume_version = random.randint(1, 50)
        self.fake_file_name = fake.file_path(depth=2)
        self.today = datetime.datetime.today()
        self.current_date = self.today.date().strftime('%Y-%m-%d')
        self.current_time = self.today.time().strftime('%I:%M%p')
        self.past_day = date_change(random.randint(1, 50), day=True)
        self.past_time = date_change(random.randint(1, 12), hour=True)
        self.future_day = date_change(random.randint(1, 50), day=True, add=True)
        self.future_time = date_change(random.randint(1, 12), hour=True, add=True)
        self.status = random.randint(1, 9)


class ChaosData:
    def __init__(self):
        self.negative_float = -random.uniform(0, 1) + -random.randint(1, 100)
        self.negative_int = -random.randint(1, 100)
        self.escape_char = random.choice(constant.ESCAPE_CHAR)
        self.not_ascii = random.choice(constant.NOT_ASCII)
        self.edge_char = random.choice(constant.EDGE_CHAR)
        self.long_string = ''.join(random.choice(string.ascii_letters) for _ in range(1000))
        self.null = None
        self.chaos_list = [self.negative_int, self.negative_float, self.escape_char, self.not_ascii, self.edge_char,
                           self.long_string, self.null]
        self.chaos_monkey = random.choice(self.chaos_list)

