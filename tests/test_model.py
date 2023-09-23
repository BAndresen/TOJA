import random
import unittest
import sqlite3
from faker import Faker
from random import randint
from unittest.mock import Mock
from pathlib import Path
import sys
import os
import datetime

current_dir = os.getcwd()
sys.path.append(current_dir)

from toja.database.create_database import create_toja_database
from toja.model import Model
from toja.model import Config
from toja.utils import date_change

EARNING_TYPE = ['Annual', 'Monthly', 'Hourly', 'Contract', 'None']
WORK_TYPE = ['Remote', 'Hybrid', 'Onsite', 'None']
SALARY_TYPE = ['Full-Time', 'Part-Time', 'Contract', 'Freelance']
EVENT_TYPE = ['applied', 'prospect', 'follow_up', 'meeting', 'workshop', 'interview', 'offer', 'offer_accepted',
              'rejected']


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
        self.salary_type = random.choice(SALARY_TYPE)
        self.event_type = random.choice(EVENT_TYPE)
        self.earning_type = random.choice(EARNING_TYPE)
        self.work_type = random.choice(WORK_TYPE)
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


class TestModel(unittest.TestCase):

    def setUp(self):
        self.user_config = Mock()
        self.user_config.get_database.return_value = ":memory:"
        self.base_dir = Path(__file__).resolve().parent
        job_description = f'{self.base_dir}\\job_descriptions'
        self.user_config.get_job_description_dir.return_value = job_description
        self.model = Model(self.user_config)
        self.model.conn = sqlite3.connect(':memory:')
        self.model.cursor = self.model.conn.cursor()
        create_toja_database(self.model.cursor, self.model.conn)

    def test_user(self):
        user_1 = FakeData()
        user_2 = FakeData()
        # insert users & points
        self.model.insert_user_db(user_1.first_name, user_1.points)
        self.model.insert_user_db(user_2.first_name, user_2.points)

        # get user id
        user1_id = self.model.get_user_id(user_1.first_name)
        self.assertEqual(user1_id, 1)

        # get all users
        all_users = self.model.get_all_users()
        self.assertEqual(all_users[0][0], user_1.first_name)
        self.assertEqual(all_users[1][0], user_2.first_name)

        # test points
        user_1_points = self.model.get_total_points(1)
        self.assertEqual(user_1_points, user_1.points)

        # test points update
        self.model.update_points(1, 4)  # status_id = 'applied' for 3 points
        user_1_updated_points = self.model.get_total_points(1)
        self.assertEqual(user_1_updated_points, (user_1_points + 3))

    def test_status(self):
        results = self.model.get_status_id("applied")[0][0]
        self.assertEqual(results, 4)

    def test_event(self):
        fake1 = FakeData()
        fake2 = FakeData()
        self.model.add_contact(fake1.first_name, fake1.last_name, fake1.email, fake1.phone, fake1.position, 1, 1)

        # past event
        self.model.add_event(fake1.current_date, fake1.current_time, fake1.event_note, fake1.status, None, 1, 1)
        self.model.add_event(fake2.current_date, fake2.current_time, fake2.event_note, fake2.status, 1, 2, 1)

        # test get_all_event
        past_events1 = self.model.get_all_event(user=1)[0]
        self.assertEqual(past_events1[0], 1)
        self.assertEqual(past_events1[1], fake1.current_date)
        self.assertEqual(past_events1[2], fake1.current_time)
        self.assertEqual(past_events1[3], fake1.event_note)
        past_events2 = self.model.get_all_event(user=1)[1]
        self.assertEqual(past_events2[0], 2)
        self.assertEqual(past_events2[1], fake2.current_date)
        self.assertEqual(past_events2[2], fake2.current_time)
        self.assertEqual(past_events2[3], fake2.event_note)

        # test get_event
        past_event3 = self.model.get_event(1, job=True)[0]
        self.assertEqual(past_event3[0], 1)
        self.assertEqual(past_event3[1], fake1.current_date)
        self.assertEqual(past_event3[2], fake1.current_time)
        self.assertEqual(past_event3[3], fake1.event_note)

    def test_contact(self):
        fake1 = FakeData()
        fake2 = FakeData()
        # add contact
        self.model.add_contact(fake1.first_name, fake1.last_name, fake1.email, fake1.phone, fake1.position, 1, 1)
        self.model.add_contact(fake2.first_name, fake2.last_name, fake2.email, fake2.phone, fake2.position, 1, 1)

        # get contact
        results = self.model.get_contacts(1)[0]
        self.assertEqual(results[0], 1)
        self.assertEqual(results[1], fake1.first_name)
        self.assertEqual(results[2], fake1.last_name)
        self.assertEqual(results[3], fake1.email)
        self.assertEqual(results[4], fake1.phone)
        self.assertEqual(results[5], fake1.position)

        # get all contacts
        results_all = self.model.get_all_contacts(1)[1]
        self.assertEqual(results_all[0], 2)
        self.assertEqual(results_all[1], fake2.first_name)
        self.assertEqual(results_all[2], fake2.last_name)
        self.assertEqual(results_all[3], fake2.email)
        self.assertEqual(results_all[4], fake2.phone)
        self.assertEqual(results_all[5], fake2.position)

    def test_delete(self):
        fake1 = FakeData()
        # test delete contact
        self.model.add_contact(fake1.first_name, fake1.last_name, fake1.email, fake1.phone, fake1.position, 1, 1)
        self.model.delete_entry('contact', 'contact_id', '1')
        results_all = self.model.get_all_contacts(1)
        self.assertEqual(results_all, [])

    def test_job(self):
        pass

        # self.model.add_new_job(self.position_1,self.company1,self.website1,self.location1,self.salary_type1,
        #                        self.work_type1,self.salary_top1,self.salary_bottom1, self.earning_type1,self.resume_version1,self.fake_file_name,
        #                        1,)

    def tearDown(self) -> None:
        self.model.conn.close()


if __name__ == '__main__':
    unittest.main()

# coverage run -m unittest test_model.py
