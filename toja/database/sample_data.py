import sqlite3
from typing import Union
import datetime


def sample_data(cursor: sqlite3.Cursor, conn: sqlite3.connect):
    job_insert = """
        INSERT INTO job (position, company, website, location, commitment, work_type, salary_top, salary_bottom, salary_type, resume_version, job_description_file, user_id)
        VALUES
            ('Software Engineer', 'TechCo', 'www.techco.com', 'San Francisco, CA', 'Full-Time', 'Onsite', 120000, 90000, 'Annual', '1.1', NULL, 1),
            ('Data Scientist', 'DataTech', 'www.datatech.com', 'New York, NY', 'Part-Time', 'Remote', 95000, 75000, 'Annual', '1.2', NULL, 1),
            ('Frontend Developer', 'WebSolutions', 'www.websolutions.com', 'Seattle, WA', 'Full-Time', 'Hybrid', 110000, 85000, 'Annual', '1.1', NULL, 1),
            ('DevOps Engineer', 'CloudOps', 'www.cloudops.com', 'Austin, TX', 'Full-Time', 'Onsite', 130000, 100000, 'Annual', '1.2', NULL, 1),
            ('UI/UX Designer', 'DesignIt', 'www.designit.com', 'Los Angeles, CA', 'Contract', 'Remote', 85000, 65000, 'Annual', '1.1', NULL, 1),
            ('Backend Developer', 'CodeCraft', 'www.codecraft.com', 'San Francisco, CA', 'Full-Time', 'Onsite', 125000, 95000, 'Annual', '1.1', NULL, 1),
            ('Machine Learning Engineer', 'AI Innovations', 'www.aiinnovations.com', 'New York, NY', 'Full-Time', 'Hybrid', 140000, 110000, 'Annual', '1.2', NULL, 1),
            ('Mobile App Developer', 'AppGenius', 'www.appgenius.com', 'Seattle, WA', 'Part-Time', 'Remote', 90000, 70000, 'Annual', '1.1', NULL, 1),
            ('QA Tester', 'TestMasters', 'www.testmasters.com', 'Austin, TX', 'Contract', 'Onsite', 95000, 75000, 'Annual', '1.2', NULL, 1),
            ('Product Designer', 'InnovateUX', 'www.innovateux.com', 'Los Angeles, CA', 'Full-Time', 'Hybrid', 115000, 90000, 'Annual', '1.1', NULL, 1),
            ('Software Engineer', 'CodeTech', 'www.codetech.com', 'San Francisco, CA', 'Full-Time', 'Onsite', 130000, 100000, 'Annual', '1.1', NULL, 1),
            ('Data Analyst', 'DataInsights', 'www.datainsights.com', 'New York, NY', 'Part-Time', 'Remote', 97000, 77000, 'Annual', '1.2', NULL, 1),
            ('Full Stack Developer', 'WebWizards', 'www.webwizards.com', 'Seattle, WA', 'Full-Time', 'Hybrid', 120000, 95000, 'Annual', '1.1', NULL, 1),
            ('Cloud Architect', 'CloudSolutions', 'www.cloudsolutions.com', 'Austin, TX', 'Full-Time', 'Onsite', 140000, 110000, 'Annual', '1.2', NULL, 1),
            ('UI Designer', 'PixelPerfect', 'www.pixelperfect.com', 'Los Angeles, CA', 'Contract', 'Remote', 87000, 67000, 'Annual', '1.1', NULL, 1);
    """
    cursor.execute(job_insert)
    conn.commit()
