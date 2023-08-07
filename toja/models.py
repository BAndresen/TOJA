import datetime


class JobApplication:
    def __init__(self, init_toja, user_inputs):
        self.user_inputs = user_inputs
        self.application_date = datetime.date.today()
        self.application_status = "submitted"
        self.job_description_file_name = f"{self.application_date}_{user_inputs.position_title}_{user_inputs.company}.txt"
        self.conn = init_toja.conn
        self.cursor = init_toja.cursor

    def add_to_database(self, sql_queries):
        data = (
            self.application_date,
            self.user_inputs.position_title,
            self.user_inputs.company,
            self.user_inputs.job_location,
            self.user_inputs.resume_version,
            self.user_inputs.salary_top,
            self.user_inputs.salary_bottom,
            self.user_inputs.application_platform,
            self.application_status,
            self.user_inputs.work_type,
            self.user_inputs.job_type,
            self.job_description_file_name
        )

        self.cursor.execute(sql_queries.insert_new_app, data)
        self.conn.commit()
        print(f"{self.user_inputs.position_title} position at {self.user_inputs.company} Successfully Entered")
