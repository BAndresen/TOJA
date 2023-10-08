from typing import Union
import os
import sqlite3
from pathlib import Path
from datetime import datetime
import csv
import sys
from fuzzywuzzy import fuzz

current_directory = os.getcwd()
parent = os.path.dirname(current_directory)
sys.path.append(parent)

from toja.config import Config
from toja.database.create_database import create_toja_database
from toja.database.sample_event import events_applied, insert_future_events, insert_past_events
from toja.database.sample_event import event_applied_notes, events_past_notes, events_future_notes
import toja.constants


class Model:
    def __init__(self, user: Config):
        self.user = user
        self.db_file_path = user.get_database()
        self.job_description_parent = user.get_job_description_dir()
        self.user_name = user.user_name
        self.connect_database(self.db_file_path)

    def connect_database(self, db_path):
        if not os.path.exists(db_path):
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()
            create_toja_database(self.cursor, self.conn)
        else:
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()

    def close_db_connections(self):
        self.conn.close()

    def set_sample_data(self):
        relative_path_job = 'database/sample_job.sql'
        relative_path_contact = 'database/sample_contact.sql'
        file_path_job = os.path.join(current_directory, relative_path_job)
        file_path_contact = os.path.join(current_directory, relative_path_contact)

        if not os.path.exists(file_path_job):
            relative_path_job = 'toja/database/sample_job.sql'
            relative_path_contact = 'toja/database/sample_contact.sql'
            file_path_job = os.path.join(current_directory, relative_path_job)
            file_path_contact = os.path.join(current_directory, relative_path_contact)

        with open(file_path_job, 'r') as file:
            sql_query = file.read()
        self.cursor.execute(sql_query)

        with open(file_path_contact, 'r') as file:
            sql_query = file.read()
        self.cursor.execute(sql_query)
        self._add_dynamic_sample_events(events_applied(event_applied_notes))
        self._add_dynamic_sample_events(insert_past_events(events_past_notes))
        self._add_dynamic_sample_events(insert_future_events(events_future_notes))
        self._null_empty_events()

    def update_database_path(self, new_db: Path):
        self.user.config['database']['database_path'] = str(new_db)
        with open(self.user.config_file, "w") as file:
            self.user.config.write(file)

    def _add_dynamic_sample_events(self, event_insert: list):
        # allow for dynamic dates
        for event in event_insert:
            query = f'''
            INSERT INTO event (date,time,note,status_id,contact_id,job_id,user_id)
            VALUES ({event})
            '''
            self.cursor.execute(query)
            self.conn.commit()

    def _null_empty_events(self):
        query = '''
            UPDATE event
        SET note = NULLIF(note, ''),
            contact_id = NULLIF(contact_id, 0),
            job_id = NULLIF(job_id, 0)
        WHERE
            note = '' OR contact_id = 0 OR job_id = 0
        '''
        self.cursor.execute(query)
        self.conn.commit()

    def get_user_id(self, user_name: str) -> int:
        query = '''
        SELECT user_id
        FROM user
        WHERE name = ?
        '''
        self.cursor.execute(query, (user_name,))
        results = self.cursor.fetchall()
        return results[0][0]

    def get_all_users(self) -> list:
        query = '''
        SELECT name
        FROM user
        '''
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def insert_user_db(self, user_name: str, points: int):
        query = '''
        INSERT INTO user(
        name,
        total_points
        )
        VALUES (?,?)
        '''
        insert = (user_name, points)
        self.cursor.execute(query, insert)
        self.conn.commit()

    def update_points(self, user_id: int, status_id: int):
        query = '''
        SELECT points
        FROM status
        WHERE status_id = ?
        '''
        self.cursor.execute(query, (status_id,))
        results = self.cursor.fetchall()[0][0]
        second_query = f'''
        UPDATE user
        SET total_points = total_points + {results}
        WHERE user_id = ?
        '''
        self.cursor.execute(second_query, (user_id,))
        self.conn.commit()

    def get_total_points(self, user_id: int) -> int:
        query = '''
        SELECT total_points
        FROM user
        WHERE user_id = ?
        '''
        self.cursor.execute(query, (user_id,))
        results = self.cursor.fetchall()[0][0]
        return results

    def delete_entry(self, table: str, column_id_name: str, identity: str, ) -> None:
        query = f'''
        DELETE
        FROM {table}
        WHERE {column_id_name} = ?
        '''
        self.cursor.execute(query, (identity,))
        self.conn.commit()

    def delete_job_txt_file(self, job_id: str) -> None:
        query = '''
        SELECT job_description_file
        FROM job
        WHERE job_id = ?
        '''
        self.cursor.execute(query, (job_id,))
        results = self.cursor.fetchall()
        if results[0][0]:
            delete_path = Path(*[self.job_description_parent, results[0][0]])
            if os.path.exists(delete_path):
                os.remove(delete_path)

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

    def get_job_data(self, job_id: Union[str, int]) -> tuple:
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

        self.update_points(user_id, status_id)

    def update_job(self, job_id: int, column_name: str, update_value: Union[str, int]):
        query = f'''
        UPDATE job
        SET {column_name} = ?
        WHERE job_id = ?
        '''
        self.cursor.execute(query, (update_value, job_id))
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

    def add_event(self, date: Union[str, datetime.date], time: str,
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
        self.update_points(user_id, status_id)

    def get_event(self, identity: int, job=False, event=False) -> list[tuple]:
        query = ''
        if job:
            query = '''
            SELECT
                e.event_id,
                e.date,
                e.time,
                e.note,
                s.status
            FROM event e
               JOIN status s USING(status_id)
            WHERE e.job_id = ?
            ORDER BY e.date
            '''
        if event:
            query = '''
             SELECT
                e.date,
                e.time,
                s.status,
                j.company,
                j.position,
                c.first_name,
                c.last_name,
                e.note
            FROM event e
               LEFT JOIN status s USING(status_id)
               LEFT JOIN job j USING(job_id)
               LEFT JOIN contact c USING(contact_id)
            WHERE e.event_id = ?
            '''
        self.cursor.execute(query, (identity,))
        results = self.cursor.fetchall()
        return results

    def get_all_event(self, user: int, future=False) -> list:
        today = datetime.today().strftime('%Y-%m-%d')
        symbol = '<='
        if future:
            symbol = '>'
        query = f'''
        SELECT
            e.event_id,
            e.date,
            e.time,
            e.note,
            s.status
        FROM event e
           JOIN status s USING(status_id)
        WHERE e.date {symbol} '{today}' AND e.user_id = {user}
        ORDER BY e.date
        '''
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def get_contacts(self, id_: int, get_contact_by_id: bool = False) -> list:
        column_id = 'job_id'
        if get_contact_by_id:
            column_id = 'contact_id'
        query = f'''
        SELECT 
            contact_id,
            first_name,
            last_name,
            email,
            phone,
            position,
            job_id
        FROM contact
        WHERE {column_id} = ?
        '''
        self.cursor.execute(query, (id_,))
        results = self.cursor.fetchall()
        return results

    def get_all_contacts(self, user_id: int, ) -> list:
        query = '''
        SELECT 
            contact_id,
            first_name,
            last_name,
            email,
            phone,
            position
        FROM contact
        WHERE user_id = ?
        '''
        self.cursor.execute(query, (user_id,))
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

    def export_database(self, user_id: int, path):
        query = '''
        SELECT
            job_id,
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
            job_description_file
        FROM job
        WHERE user_id = ?
        '''
        self.cursor.execute(query, (user_id,))
        data = self.cursor.fetchall()
        csv_job_file_path = os.path.join(path, 'exported_job_data.csv')

        with open(csv_job_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([description[0] for description in self.cursor.description])
            csv_writer.writerows(data)

        query = '''
        SELECT
             e.event_id,
             e.date,
             e.time,
             s.status,
             e.contact_id,
             e.job_id,
             e.note
        FROM event e
        JOIN status s USING(status_id)
        WHERE user_id = ?
        '''
        self.cursor.execute(query, (user_id,))
        data = self.cursor.fetchall()
        csv_event_file_path = os.path.join(path, 'exported_event_data.csv')

        with open(csv_event_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([description[0] for description in self.cursor.description])
            csv_writer.writerows(data)

        query = '''
        SELECT
            contact_id,
            first_name,
            last_name,
            email,
            phone,
            position,
            job_id
        FROM contact
        WHERE user_id = ?
        '''
        self.cursor.execute(query, (user_id,))
        data = self.cursor.fetchall()
        csv_contact_file_path = os.path.join(path, 'exported_contact_data.csv')

        with open(csv_contact_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([description[0] for description in self.cursor.description])
            csv_writer.writerows(data)

    def get_filenames(self, user_id, job_id=None, single_job=False) -> list:
        jobs = ''
        if single_job:
            jobs = f'AND job_id = {job_id}'
        query = f'''
        SELECT
            job_description_file
        FROM job
        WHERE user_id = {user_id} {jobs}    
        '''
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        print(results)
        return results

    def get_filenames_fuzzy(self, user_id, position: str, threshold: int):
        query = f'''
            SELECT
                position,
                job_description_file
            FROM job
            WHERE user_id = {user_id}        
            '''
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        print(results)

        matching_rows = []
        for row in results:
            if fuzz.token_sort_ratio(row[0], position) >= threshold:
                matching_rows.append(row[1])
        print(matching_rows)

        return tuple(matching_rows)

