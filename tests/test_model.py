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

        # generate fake user info
        fake = Faker()
        self.user_1 = fake.name()
        self.points_1 = random.randint(0, 100)
        self.user_2 = fake.name()
        self.points_2 = random.randint(0, 100)

    def test_user(self):
        # insert users & points
        self.model.insert_user_db(self.user_1, self.points_1)
        self.model.insert_user_db(self.user_2, self.points_2)

        # get user id
        user1_id = self.model.get_user_id(self.user_1)
        self.assertEqual(user1_id, 1)

        # get all users
        all_users = self.model.get_all_users()
        self.assertEqual(all_users[0][0], self.user_1)
        self.assertEqual(all_users[1][0], self.user_2)

        # test points
        user_1_points = self.model.get_total_points(1)
        self.assertEqual(user_1_points, self.points_1)

        # test points update
        self.model.update_points(1, 4)  # status_id = 'applied' for 3 points
        user_1_updated_points = self.model.get_total_points(1)
        self.assertEqual(user_1_updated_points, (user_1_points + 3))

    def test_update_points(self):
        # self.model.insert_user_db(self.user_1, self.points_1)
        pass

    def tearDown(self) -> None:
        self.model.conn.close()


if __name__ == '__main__':
    unittest.main()

# coverage run -m unittest test_model.py
