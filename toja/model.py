from __future__ import annotations
from typing import TYPE_CHECKING

import datetime
import os
import sqlite3

if TYPE_CHECKING:
    from pathlib import Path


class Database:
    def __init__(self, db_file_path: Path):
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

    def close_db_connections(self):
        self.conn.close()
