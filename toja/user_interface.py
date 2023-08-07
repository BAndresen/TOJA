


class JobInputs:
    def __init__(self):
        print('\nEnter Application Details Below or Leave Blank\n')
        self.position_title = input('Enter the Position Title: ').lower()

        self.company = input('Enter the Company Name: ').lower()
        self.job_location = input('Enter the Job Location: ').lower()
        try:
            self.resume_version = float(input('Enter the Resume Version: '))
        except ValueError:
            self.resume_version = None
        try:
            self.salary_top = int(input('Enter the Salary Top-End Range: '))
        except ValueError:
            self.salary_top = None
        try:
            self.salary_bottom = int(input('Enter the Salary Bottom-End Range: '))
        except ValueError:
            self.salary_bottom = None

        self.application_platform = input('Enter the Application Platform: ').lower()
        self.application_status = "submitted"
        self.work_type = input('Location Type (remote,hybrid,onsite): ').lower()
        self.job_type = input('Job Type (full-time, part-time, contract, freelance): ').lower()

        self._check_null()

    def _check_null(self):
        if self.position_title == "":
            self.position_title = None
        if self.company == "":
            self.company = None
        if self.job_location == "":
            self.job_location = None
        if self.application_platform == "":
            self.application_platform = None
        if self.application_status == "":
            self.application_status = None
        if self.work_type == "":
            self.work_type = None
        if self.job_type == "":
            self.job_type = None