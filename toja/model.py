from __future__ import annotations
from typing import TYPE_CHECKING

import datetime
import os
import sqlite3

from sql_query import select_home_view_listbox

if TYPE_CHECKING:
    from pathlib import Path


class Model:
    def __init__(self, db_file_path: Path):
        # self.home_listbox = None
        self.today = datetime.date.today()
        self.db_file_path = db_file_path

        # Check if database exists, if not create
        if not os.path.exists(self.db_file_path):
            self.conn = sqlite3.connect(self.db_file_path)
            self.cursor = self.conn.cursor()
        else:
            self.conn = sqlite3.connect(self.db_file_path)
            self.cursor = self.conn.cursor()

    def create_table(self):
        pass

    def get_all(self):
        self.cursor.execute(select_home_view_listbox)
        home_listbox = self.cursor.fetchall()
        return home_listbox


    def close_db_connections(self):
        self.conn.close()

