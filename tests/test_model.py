import unittest
import sqlite3

from toja.database.create_database import create_toja_database


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

        create_toja_database(self.cursor,self.conn)

    def test_status(self):
        self.cursor.execute('''
        SELECT status
        FROM status
        WHERE status_id = 2
        ''')
        results = self.cursor.fetchall()
        self.assertEqual(results[0][0],'applied')



    def tearDown(self) -> None:
        self.conn.close()


if __name__ == '__main__':
    unittest.main()

