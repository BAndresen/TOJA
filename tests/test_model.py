import random
import unittest
import sqlite3
from faker import Faker
from random import randint
from unittest.mock import Mock, patch
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
import toja.constants as constant


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


class TestModel(unittest.TestCase):

    def setUp(self):
        # self.user_config = Config()
        config_mock = Mock()
        config_mock.base_dir = Path(__file__).resolve().parent
        config_mock.job_description_parent = os.path.join(config_mock.base_dir,constant.JOB_DESCRIPTION_DIRECTORY)
        config_mock.user_name = 'test_user'
        config_mock.database_path = ':memory:'

        self.model = Model(config_mock)
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
        fake1 = FakeData()
        fake2 = FakeData()

        self.model.add_new_job(fake1.position, fake1.company, fake1.website, fake1.location, fake1.salary_type,
                               fake1.work_type, fake1.salary_top, fake1.salary_bottom, fake1.earning_type,
                               fake1.resume_version, fake1.fake_file_name,
                               1, fake1.current_date, fake1.current_time, fake1.event_note, fake1.event_type, None)

        results_hv = self.model.get_home_view_listbox(1)[0]
        self.assertEqual(results_hv[0], 1)
        self.assertEqual(results_hv[1], fake1.company)
        self.assertEqual(results_hv[2], fake1.position)

        # get job info
        results = self.model.get_job_data(1)
        self.assertEqual(results[0], fake1.company)
        self.assertEqual(results[1], fake1.website)
        self.assertEqual(results[2], fake1.position)
        self.assertEqual(results[3], fake1.location)
        self.assertEqual(results[4], fake1.salary_type)
        self.assertEqual(results[5], fake1.work_type)
        self.assertEqual(results[6], str(fake1.salary_top))
        self.assertEqual(results[7], str(fake1.salary_bottom))
        self.assertEqual(results[8], fake1.earning_type)
        self.assertEqual(results[9], str(fake1.resume_version))
        self.assertEqual(results[10], fake1.fake_file_name)

        # Update Job
        self.model.update_job(1, 'position', fake2.position)
        self.model.update_job(1, 'company', fake2.company)
        self.model.update_job(1, 'website', fake2.website)
        self.model.update_job(1, 'location', fake2.location)
        self.model.update_job(1, 'commitment', fake2.salary_type)
        self.model.update_job(1, 'work_type', fake2.work_type)
        self.model.update_job(1, 'salary_top', fake2.salary_top)
        self.model.update_job(1, 'salary_bottom', fake2.salary_bottom)
        self.model.update_job(1, 'salary_type', fake2.earning_type)
        self.model.update_job(1, 'resume_version', fake2.resume_version)
        self.model.update_job(1, 'job_description_file', fake2.fake_file_name)

        results_updated = self.model.get_job_data(1)
        self.assertEqual(results_updated[0], fake2.company)
        self.assertEqual(results_updated[1], fake2.website)
        self.assertEqual(results_updated[2], fake2.position)
        self.assertEqual(results_updated[3], fake2.location)
        self.assertEqual(results_updated[4], fake2.salary_type)
        self.assertEqual(results_updated[5], fake2.work_type)
        self.assertEqual(results_updated[6], str(fake2.salary_top))
        self.assertEqual(results_updated[7], str(fake2.salary_bottom))
        self.assertEqual(results_updated[8], fake2.earning_type)
        self.assertEqual(results_updated[9], str(fake2.resume_version))
        self.assertEqual(results_updated[10], fake2.fake_file_name)

    def tearDown(self) -> None:
        self.model.conn.close()


if __name__ == '__main__':
    unittest.main()

# coverage run -m unittest tests\test_model.py
