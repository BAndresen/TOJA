from __future__ import annotations
from typing import Union
import os
import sqlite3
from pathlib import Path

from create_database import create_toja_database, add_sample_data
from config import Config
from utils import get_file_from_path


class Model:
    def __init__(self, user: Config, sample_data=False):
        self.user = user
        self.db_file_path = user.get_database()
        self.job_description_parent = user.get_job_description_dir()
        self.user_name = user.user_name

        self.connect_database(self.db_file_path)
        self.sample_data = sample_data
        if sample_data:
            add_sample_data(self.cursor, self.conn)

    def connect_database(self, db_path):
        if not os.path.exists(db_path):
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()
            create_toja_database(self.cursor, self.conn)
            # self.insert_user_db(self.user.user_db_name,0)
        else:
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()

    def get_user(self, user_name: str) -> int:
        query = '''
        SELECT user_id
        FROM database
        WHERE name = ?
        '''
        self.cursor.execute(query, (user_name,))
        results = self.cursor.fetchall()
        return results[0][0]

    def get_all_users(self) -> list:
        query = '''
        SELECT name
        FROM database
        '''
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def insert_user_db(self, db_name: str, points: int):
        query = '''
        INSERT INTO database(
        name,
        total_points
        )
        VALUES (?,?)
        '''
        insert = (db_name, points)
        self.cursor.execute(query, insert)
        self.conn.commit()

    def get_home_view_listbox(self, user_id) -> list:
        query = '''
        SELECT
            job_id,
            company,
            position
        FROM job
        WHERE user_id = ?
        '''
        self.cursor.execute(query, (user_id,))
        results = self.cursor.fetchall()
        return results

    def close_db_connections(self):
        self.conn.close()

    def get_job_data(self, job_id: str) -> tuple:
        query = '''
         SELECT
             company,
             website,
             position,
             location,
             commitment,
             work_type,
             salary_top,
             salary_bottom,
             salary_type,
             resume_version,
             job_description_file
             
         FROM job
         WHERE job_id = ?
         '''
        self.cursor.execute(query, (job_id,))
        results = self.cursor.fetchall()
        return results[0]

    def delete_job(self, job_id: str) -> None:
        query = '''
        DELETE
        FROM job
        WHERE job_id = ?
        '''
        self.cursor.execute(query, (job_id,))
        self.conn.commit()

    def add_new_job(self, position: str, company: str, website: str, location: str, commitment: str,
                    work_type: str,
                    salary_top: int, salary_bottom: int,
                    salary_type: str, resume: float, job_description_file: str, user_id: int,
                    date, time, note, status, contact_id) -> None:
        query = '''
        INSERT INTO job(
             position,
             company,
             website,
             location,
             commitment,
             work_type,
             salary_top,
             salary_bottom,
             salary_type,
             resume_version,
             job_description_file,
             user_id
        )
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        '''
        insert = (
            position, company, website, location, commitment, work_type, salary_top, salary_bottom, salary_type,
            resume, job_description_file, user_id)

        self.cursor.execute(query, insert)

        # add to event table
        job_id = self.cursor.lastrowid
        status_id = self.get_status_id(status)[0][0]

        query_event = '''
        INSERT INTO event(
            date,
            time,
            note,
            status_id,
            contact_id,
            job_id,
            user_id
            )
        VALUES (?,?,?,?,?,?,?)
        '''
        insert_event = (date, time, note, status_id, contact_id, job_id, user_id)
        self.cursor.execute(query_event, insert_event)
        self.conn.commit()

        self.conn.commit()

    def add_event(self, date: str, time: str,
                  note: Union[str, None],
                  status_id: int, contact_id: Union[int, None], job_id: int, user_id: int) -> None:
        query = '''
        INSERT INTO event(
            date,
            time,
            note,
            status_id,
            contact_id,
            job_id,
            user_id
            )
        VALUES (?,?,?,?,?,?,?)
        '''
        insert = (date, time, note, status_id, contact_id, job_id, user_id)
        self.cursor.execute(query, insert)
        self.conn.commit()

    def get_status_id(self, status: str) -> list:
        query = '''
        SELECT status_id
        FROM status
        WHERE status = ?'''

        self.cursor.execute(query, (status,))
        results = self.cursor.fetchall()
        return results

    def open_job_description(self, job_file: Union[Path, tuple[str]]) -> str:
        try:
            with open(f'{self.job_description_parent}\\{job_file}', "r", encoding='utf-8') as file:
                results = file.read()
        except UnicodeDecodeError:
            with open(f'{self.job_description_parent}\\{job_file}', "r") as file:
                results = file.read()

        return results

    def save_job_description(self, job_file: str, job_text: str) -> None:

        with open(f'{self.job_description_parent}/{job_file}', 'w', encoding='utf-8') as file:
            file.write(job_text)

    def get_event(self, job_id: int) -> list:
        query = '''
        SELECT
            e.date,
            e.time,
            e.note,
            s.status
        FROM event e
           JOIN status s USING(status_id)
        WHERE e.job_id = ?
        '''
        self.cursor.execute(query, (job_id,))
        results = self.cursor.fetchall()
        return results

    def get_all_event(self) -> list:
        query = '''
        SELECT
            e.date,
            e.time,
            e.note,
            s.status
        FROM event e
           JOIN status s USING(status_id)
        '''
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def get_contacts(self, job_id: int) -> list:
        query = '''
        SELECT 
            contact_id,
            first_name,
            last_name,
            email,
            phone,
            position
        FROM contact
        WHERE job_id = ?
        '''
        self.cursor.execute(query, (job_id,))
        results = self.cursor.fetchall()
        return results

    def add_contact(self, first_name: str, last_name: str, email: str, phone: str, position: str, job_id: int,
                    user_id: int):
        query = '''
        INSERT INTO contact(
            first_name,
            last_name,
            email,
            phone,
            position,
            job_id,
            user_id
            )
        VALUES (?,?,?,?,?,?,?)
        '''
        insert = (first_name, last_name, email, phone, position, job_id, user_id)
        self.cursor.execute(query, insert)
        self.conn.commit()

    def update_database_path(self, new_db: Path):
        self.user.config['database']['database_path'] = str(new_db)
        with open(self.user.config_file, "w") as file:
            self.user.config.write(file)

    def update_job(self, job_id: int, column_name: str, update_value: str):
        query = f'''
        UPDATE job
        SET {column_name} = ?
        WHERE job_id = ?
        '''
        self.cursor.execute(query, (update_value, job_id))
        self.conn.commit()
