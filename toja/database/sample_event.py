
from utils import date_change
from random import randrange

event_applied_notes = [
    'Just submitted my application for the Software Engineer.',
    'Applied for the Data Scientist position. Fingers crossed!',
    'Just hit Submit on my application for the Frontend Developer.',
    'Excited to be in the running for the DevOps Engineer role.',
    'Applied for the UI/UX Designer position. Love their portfolio!',
    'Just sent in my application for the Backend Developer.',
    'Applied for the Machine Learning Engineer. Dream job!',
    'Submitted my application for the Mobile App Developer.',
    'Applied for the QA Tester role. Ready to show my skills!',
    'Just applied for the Product Designer position. Hope to stand out.',
    'Excited to have applied for the Software Engineer.',
    'Submitted my application for the Data Analyst position.',
    'Applied for the Full Stack Developer position. Love their work!',
    'Just applied for the Cloud Architect role. Fingers crossed!',
    'Submitted my application for the UI Designer position.',
]

events_past_notes = {
    'follow_up': [
        'Sent follow-up email regarding application status.',
        'Followed up with HR.',
        'Received positive feedback during follow-up call.'],

    'prospect': [
        'Identified potential job opening.',
        'Researching prospects for future job opportunities.',
        'Reached out to industry contacts for potential leads.'],

    'offer': [
        'Received job offer as Cloud Architect.',
        'Celebrating the offer for the Mobile App Developer position.',
        'Excited to about the offer for the QA Tester role.'],

    'rejected': [
        "Unfortunately, didn't make it.",
        'Received rejection email for the position.',
        'Not discouraged by rejection continuing job search.'],
}

events_future_notes = {
    'meeting': [
        'networking meeting with a fellow developer.',
        'Scheduled a coffee meeting with a hiring manager.',
        'Discussed job prospects in a virtual meeting.'],

    'networking': [
        'Attended Tech Summit to expand industry connections.',
        'Participated in a career fair to explore job options.',
        'Networking event was insightful for future opportunities.'],

    'interview': [
        'Preparing for upcoming technical interview.',
        'Nervous but excited about the upcoming job interview.',
        'Interviewed with the hiring team.']
}


def events_applied(events: list) -> list:
    events_applied_list = []
    index = 1
    for note in events:
        randon_hour_unit = randrange(1, 5)
        random_day_unit = randrange(5, 15)
        time = date_change(randon_hour_unit, hour=True)
        day = date_change(random_day_unit, day=True)
        contact = randrange(1, 30)
        job_id = index
        user_id = 1
        status_id = 4
        event_string = f'"{day}","{time}","{note}","{status_id}","{contact}","{job_id}","{user_id}"'
        events_applied_list.append(event_string)
        index += 1
    return events_applied_list


def insert_past_events(event: dict) -> list:
    event_list = []
    for key, value in event.items():
        if key == 'follow_up':
            for note in value:
                randon_hour_unit = randrange(1, 5)
                random_day_unit = randrange(1, 10)
                date = date_change(random_day_unit, day=True)
                time = date_change(randon_hour_unit, hour=True)
                contact = randrange(1, 30)
                job_id = randrange(1, 15)
                event_list.append(f'"{date}","{time}","{note}","3","{contact}","{job_id}", "1"')
        if key == 'prospect':
            for note in value:
                randon_hour_unit = randrange(1, 5)
                random_day_unit = randrange(20, 30)
                date = date_change(random_day_unit, day=True)
                time = date_change(randon_hour_unit, hour=True)
                contact = randrange(1, 30)
                job_id = randrange(1, 15)
                event_list.append(f'"{date}","{time}","{note}","2","{contact}","{job_id}", "1"')
        if key == 'offer':
            for note in value:
                randon_hour_unit = randrange(1, 5)
                random_day_unit = randrange(1, 2)
                date = date_change(random_day_unit, day=True)
                time = date_change(randon_hour_unit, hour=True)
                contact = randrange(1, 30)
                job_id = randrange(1, 15)
                event_list.append(f'"{date}","{time}","{note}","8","{contact}","{job_id}", "1"')
        if key == 'rejected':
            for note in value:
                randon_hour_unit = randrange(1, 5)
                random_day_unit = randrange(1, 2)
                date = date_change(random_day_unit, day=True)
                time = date_change(randon_hour_unit, hour=True)
                contact = randrange(1, 30)
                job_id = randrange(1, 15)
                event_list.append(f'"{date}","{time}","{note}","1","{contact}","{job_id}", "1"')
    return event_list


def insert_future_events(event: dict) -> list:
    event_list = []
    for key, value in event.items():
        if key == 'meeting':
            for note in value:
                randon_hour_unit = randrange(1, 5)
                random_day_unit = randrange(1, 10)
                date = date_change(random_day_unit, day=True, add=True)
                time = date_change(randon_hour_unit, hour=True)
                contact = randrange(1, 30)
                event_list.append(f'"{date}","{time}","{note}","5","{contact}",{False}, "1"')
        if key == 'networking':
            for note in value:
                randon_hour_unit = randrange(1, 5)
                random_day_unit = randrange(10, 60)
                date = date_change(random_day_unit, day=True, add=True)
                time = date_change(randon_hour_unit, hour=True)
                event_list.append(f'"{date}","{time}","{note}","6",{False},{False}, "1"')
        if key == 'interview':
            for note in value:
                randon_hour_unit = randrange(1, 5)
                random_day_unit = randrange(1, 10)
                date = date_change(random_day_unit, day=True, add=True)
                time = date_change(randon_hour_unit, hour=True)
                contact = randrange(1, 30)
                job_id = randrange(1, 15)
                event_list.append(f'"{date}","{time}","{note}","7","{contact}","{job_id}", "1"')
    return event_list
