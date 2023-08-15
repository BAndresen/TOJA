from __future__ import annotations
from typing import TYPE_CHECKING

import datetime
import os
import sqlite3

from sql_query import create_toja_database, add_sample_data, home_view_listbox

if TYPE_CHECKING:
    from pathlib import Path


class Model:
    def __init__(self, db_file_path: Path, sample_data=False):
        self.db_file_path = db_file_path

        # Check if database exists, if not create
        if not os.path.exists(self.db_file_path):
            self.conn = sqlite3.connect(self.db_file_path)
            self.cursor = self.conn.cursor()
            create_toja_database(self.cursor)
        else:
            self.conn = sqlite3.connect(self.db_file_path)
            self.cursor = self.conn.cursor()

        self.sample_data = sample_data
        if sample_data:
            add_sample_data(self.cursor, self.conn)

    def get_all(self):
        home_listbox = home_view_listbox(self.cursor)
        return home_listbox

    def close_db_connections(self):
        self.conn.close()

    def get_job_data(self, job_id: int):
        query = '''
         SELECT
             company,
             position
         FROM job
         WHERE job_id = ?
         '''
        self.cursor.execute(query, (job_id,))
        results = self.cursor.fetchall()
        return results[0]
