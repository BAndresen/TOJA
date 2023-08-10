from pathlib import Path

SQL_BASE_DIRECTORY = Path(__file__).resolve().parent

# SQL Queries
CREATE_JOB_APP_TABLE_SQL = Path(*[SQL_BASE_DIRECTORY, 'create_new_job_application_table.sql'])
INSERT_NEW_JOB_APP_SQL = Path(*[SQL_BASE_DIRECTORY, 'insert_new_job_application.sql'])
SELECT_ALL_JOBS_APPLIED = Path(*[SQL_BASE_DIRECTORY, 'select_all_jobs_applied.sql'])

