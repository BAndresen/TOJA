CREATE TABLE jobs_applied (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    application_date TEXT DEFAULT NULL,
    position_title TEXT DEFAULT NULL,
    company TEXT DEFAULT NULL,
    job_location TEXT DEFAULT NULL,
    resume_version INT DEFAULT NULL,
    salary_top INT DEFAULT NULL,
    salary_bottom INT TEXT DEFAULT NULL,
    application_platform TEXT DEFAULT NULL,
    application_status TEXT DEFAULT NULL,
    work_type TEXT DEFAULT NULL,
    job_type TEXT DEFAULT NULL,
    job_description_file_path TEXT DEFAULT NULL
	)