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

EARNING_TYPE = ['Annual', 'Monthly', 'Hourly', 'Contract', 'None']
WORK_TYPE = ['Remote', 'Hybrid', 'Onsite', 'None']
SALARY_TYPE = ['Full-Time', 'Part-Time', 'Contract', 'Freelance']
EVENT_TYPE = ['applied', 'prospect', 'follow_up', 'meeting', 'workshop', 'interview', 'offer', 'offer_accepted',
              'rejected']


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

        # generate fake info
        fake = Faker()
        self.name_1_first = fake.first_name()
        self.name_1_last = fake.last_name()
        self.points_1 = random.randint(0, 100)
        self.phone_1 = fake.phone_number()
        self.email_1 = fake.email()
        self.position_1 = fake.job()
        self.event_note1 = fake.paragraph(nb_sentences=1)
        self.job_note1 = fake.paragraph(nb_sentences=1)
        self.company1 = fake.company()
        self.location1 = fake.city()
        self.salary_top1 = random.randint(1, 1_000_000)
        self.salary_bottom1 = random.randint(1, self.salary_top1)
        self.salary_type1 = random.choice(SALARY_TYPE)
        self.event_type1 = random.choice(EVENT_TYPE)
        self.earning_type1 = random.choice(EARNING_TYPE)
        self.work_type1 = random.choice(WORK_TYPE)

        self.name_2_first = fake.first_name()
        self.name_2_last = fake.last_name()
        self.points_2 = random.randint(0, 100)
        self.phone_2 = fake.phone_number()
        self.email_2 = fake.email()
        self.position_2 = fake.job()
        self.event_note2 = fake.paragraph(nb_sentences=1)
        self.job_note2 = fake.paragraph(nb_sentences=1)
        self.company2 = fake.company()
        self.location2 = fake.city()
        self.salary_top2 = random.randint(1, 1_000_000)
        self.salary_bottom2 = random.randint(1, self.salary_top2)
        self.salary_type2 = random.choice(SALARY_TYPE)
        self.event_type2 = random.choice(EVENT_TYPE)
        self.earning_type2 = random.choice(EARNING_TYPE)
        self.work_type2 = random.choice(WORK_TYPE)

        self.today = datetime.datetime.today()

    def test_user(self):
        # insert users & points
        self.model.insert_user_db(self.name_1_first, self.points_1)
        self.model.insert_user_db(self.name_2_first, self.points_2)

        # get user id
        user1_id = self.model.get_user_id(self.name_1_first)
        self.assertEqual(user1_id, 1)

        # get all users
        all_users = self.model.get_all_users()
        self.assertEqual(all_users[0][0], self.name_1_first)
        self.assertEqual(all_users[1][0], self.name_2_first)

        # test points
        user_1_points = self.model.get_total_points(1)
        self.assertEqual(user_1_points, self.points_1)

        # test points update
        self.model.update_points(1, 4)  # status_id = 'applied' for 3 points
        user_1_updated_points = self.model.get_total_points(1)
        self.assertEqual(user_1_updated_points, (user_1_points + 3))

    def test_status(self):
        results = self.model.get_status_id("applied")[0][0]
        self.assertEqual(results, 4)

    def test_event(self):
        self.model.add_contact(self.name_1_first, self.name_1_last, self.email_1, self.phone_1, self.position_1, 1, 1)

        date = self.today.date().strftime('%Y-%m-%d')
        time = self.today.time().strftime('%I:%M%p')
        rand_status1 = random.randint(1, 9)
        rand_status2 = random.randint(1, 9)
        # past event
        self.model.add_event(date, time, self.event_note1, rand_status1, None, 1, 1)
        self.model.add_event(date, time, self.event_note2, rand_status2, 1, 2, 1)

        # test get_all_event
        past_events1 = self.model.get_all_event(user=1)[0]
        self.assertEqual(past_events1[0], 1)
        self.assertEqual(past_events1[1], date)
        self.assertEqual(past_events1[2], time)
        self.assertEqual(past_events1[3], self.event_note1)
        past_events2 = self.model.get_all_event(user=1)[1]
        self.assertEqual(past_events2[0], 2)
        self.assertEqual(past_events2[1], date)
        self.assertEqual(past_events2[2], time)
        self.assertEqual(past_events2[3], self.event_note2)

        # test get_event
        past_event3 = self.model.get_event(1, job=True)[0]
        self.assertEqual(past_event3[0], 1)
        self.assertEqual(past_event3[1], date)
        self.assertEqual(past_event3[2], time)
        self.assertEqual(past_event3[3], self.event_note1)

    def test_contact(self):
        # add contact
        self.model.add_contact(self.name_1_first, self.name_1_last, self.email_1, self.phone_1, self.position_1, 1, 1)
        self.model.add_contact(self.name_2_first, self.name_2_last, self.email_2, self.phone_2, self.position_2, 2, 1)

        # get contact
        results = self.model.get_contacts(1)[0]
        self.assertEqual(results[0], 1)
        self.assertEqual(results[1], self.name_1_first)
        self.assertEqual(results[2], self.name_1_last)
        self.assertEqual(results[3], self.email_1)
        self.assertEqual(results[4], self.phone_1)
        self.assertEqual(results[5], self.position_1)

        # get all contacts
        results_all = self.model.get_all_contacts(1)[1]
        self.assertEqual(results_all[0], 2)
        self.assertEqual(results_all[1], self.name_2_first)
        self.assertEqual(results_all[2], self.name_2_last)
        self.assertEqual(results_all[3], self.email_2)
        self.assertEqual(results_all[4], self.phone_2)
        self.assertEqual(results_all[5], self.position_2)

    def test_delete(self):
        # test delete contact
        self.model.add_contact(self.name_1_first, self.name_1_last, self.email_1, self.phone_1, self.position_1, 1, 1)
        self.model.delete_entry('contact', 'contact_id', '1')
        results_all = self.model.get_all_contacts(1)
        self.assertEqual(results_all, [])

    def tearDown(self) -> None:
        self.model.conn.close()


if __name__ == '__main__':
    unittest.main()

# coverage run -m unittest test_model.py
