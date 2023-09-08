import random
import unittest
import sqlite3
# import coverage
from faker import Faker
from random import randint
from unittest.mock import Mock
from pathlib import Path

from toja.database.create_database import create_toja_database
from toja.model import Model
from toja.model import Config


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
        # generate fake user info
        fake = Faker()
        self.user_1_first = fake.first_name()
        self.user_1_last = fake.last_name()
        self.points_1 = random.randint(0, 100)
        self.user_2_first = fake.first_name()
        self.user_2_last = fake.last_name()
        self.points_2 = random.randint(0, 100)

        # insert users & points
        self.model.insert_user_db(self.user_1_first, self.points_1)
        self.model.insert_user_db(self.user_2_first, self.points_2)

        # get user id
        user1_id = self.model.get_user_id(self.user_1_first)
        self.assertEqual(user1_id, 1)

        # get all users
        all_users = self.model.get_all_users()
        self.assertEqual(all_users[0][0], self.user_1_first)
        self.assertEqual(all_users[1][0], self.user_2_first)

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

    def test_contact(self):
        fake = Faker()
        # generate contact info
        self.user_1_first = fake.first_name()
        self.user_1_last = fake.last_name()
        self.user_2_first = fake.first_name()
        self.user_2_last = fake.last_name()
        self.phone_1 = fake.phone_number()
        self.phone_2 = fake.phone_number()
        self.email_1 = fake.email()
        self.email_2 = fake.email()
        self.job_1 = fake.job()
        self.job_2 = fake.job()

        # add contact
        self.model.add_contact(self.user_1_first, self.user_1_last, self.email_1, self.phone_1, self.job_1, 1, 1)
        self.model.add_contact(self.user_2_first, self.user_2_last, self.email_2, self.phone_2, self.job_2, 2, 1)

        # get contact
        results = self.model.get_contacts(1)[0]
        self.assertEqual(results[0], 1)
        self.assertEqual(results[1], self.user_1_first)
        self.assertEqual(results[2], self.user_1_last)
        self.assertEqual(results[3], self.email_1)
        self.assertEqual(results[4], self.phone_1)
        self.assertEqual(results[5], self.job_1)

        # get all contacts
        results_all = self.model.get_all_contacts(1)[1]
        self.assertEqual(results_all[0], 2)
        self.assertEqual(results_all[1], self.user_2_first)
        self.assertEqual(results_all[2], self.user_2_last)
        self.assertEqual(results_all[3], self.email_2)
        self.assertEqual(results_all[4], self.phone_2)
        self.assertEqual(results_all[5], self.job_2)

    def tearDown(self) -> None:
        self.model.conn.close()


if __name__ == '__main__':
    unittest.main()

# coverage run -m unittest test_model.py
