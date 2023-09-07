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
        # generate fake username and points
        fake = Faker()
        user_1 = fake.name()
        points_1 = random.randint(0, 100)
        user_2 = fake.name()
        points_2 = random.randint(0, 100)

        # insert users
        self.model.insert_user_db(user_1, points_1)
        self.model.insert_user_db(user_2, points_2)

        # get user id
        user1_id = self.model.get_user_id(user_1)
        self.assertEqual(user1_id, 1)

        # get all users
        all_users = self.model.get_all_users()
        self.assertEqual(all_users[0][0], user_1)
        self.assertEqual(all_users[1][0], user_2)

    def tearDown(self) -> None:
        self.model.conn.close()


if __name__ == '__main__':
    unittest.main()

# coverage run -m unittest test_model.py
