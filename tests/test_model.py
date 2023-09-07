import unittest
import sqlite3
# import coverage
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
        self.model.insert_user_db("User1", 25)
        self.model.insert_user_db("User2", 65)
        self.model.insert_user_db("User3", 110)
        user1_id = self.model.get_user_id("User1")
        user2_id = self.model.get_user_id("User2")
        user3_id = self.model.get_user_id("User3")
        self.assertEqual(user1_id, 1)
        self.assertEqual(user2_id, 2)
        self.assertEqual(user3_id, 3)
        all_users = self.model.get_all_users()
        self.assertEqual(all_users[0][0],'User1')
        self.assertEqual(all_users[1][0],'User2')
        self.assertEqual(all_users[2][0],'User3')

    def tearDown(self) -> None:
        self.model.conn.close()


if __name__ == '__main__':
    unittest.main()


# coverage run -m unittest test_model.py
