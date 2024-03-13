import customtkinter
import tkinter
from datetime import datetime, timedelta
from typing import Union
from webbrowser import open
from tkinter import filedialog, messagebox
import subprocess
from pathlib import Path
import os
from PIL import Image
from loguru import logger

from views.job_new import NewJob
from views.job_profile import JobProfile
from views.home import HomeView
from views.event_new import NewEvent
from views.contact_new import NewContact
from views.job_edit import EditJob
from views.job_description import JobDescriptionView
from views.user_welcome import WelcomeUser
from views.user_select import UserSelect
from views.user_new import CreateUser
from views.event import Event
from views.settings import Settings
from views.contact_view import Contact
from views.generate_report import GenerateReport
from views.report import Report
from model import Model
from keywords import JobDescription, KeywordExtractor, Resume, resume_score
import utils as utils
import constants as constant


class Controller:
    def __init__(self, view: HomeView, model: Model, new_user: bool = False):
        self.today = datetime.today().date()
        self.new_job = None
        # self.user_id = None
        self.view = view
        self.model = model

        # HomeView Button Commands
        self.view.events_button.configure(command=self.view.event_frame_button)
        self.view.home_button.configure(command=self.view.home_frame_button)
        self.view.keyword_button.configure(command=self.view.keyword_frame_button)
        self.view.network_button.configure(command=self.view.network_frame_button)
        self.view.new_job_button.configure(command=self.open_job_submit)
        self.view.delete_job_button.configure(command=self.delete_job)
        self.view.open_jobs_switch.configure(command=self.open_job_listbox_view)

        # set switch from config
        self.set_open_jobs_only_switch()

        self.view.network_new_contact_button.configure(command=self.add_contact_home)
        self.view.network_delete_job_button.configure(command=self.delete_contact)

        self.view.event_new_button.configure(command=self.new_event_home)
        self.view.event_delete_button.configure(command=self.delete_event)

        #  Keywords
        self.view.jd_search_button.configure(command=self.search_job_button)
        self.view.resume_browse_button.configure(command=self.browse_resume_button)
        self.view.resume_search_button.configure(command=self.search_resume_button)
        self.view.view_position.configure(command=self.display_position)

        # HomeView ListBox Bind
        self.view.job_list_box.bind('<Double-Button-1>', self.double_click_job)
        self.view.job_list_box.bind('<Return>', self.double_click_job)

        # Event Listbox Bind
        self.view.past_events_listbox.bind('<Double-Button-1>', self.double_click_event_past)
        self.view.past_events_listbox.bind('<Return>', self.double_click_event_past)
        self.view.upcoming_events_listbox.bind('<Double-Button-1>', self.double_click_event_upcoming)
        self.view.upcoming_events_listbox.bind('<Return>', self.double_click_event_upcoming)

        # Contact Listbox Bind
        self.view.contact_listbox.bind('<Double-Button-1>', self.double_click_contact_home)
        self.view.contact_listbox.bind('<Return>', self.double_click_contact_home)

        # file menu
        self.view.help_.add_command(label='About Toja', command=self.about_page)
        self.view.file.add_command(label='New User', command=self.create_user)
        self.view.file.add_command(label='Change User', command=self.change_user)
        self.view.file.add_command(label='Settings', command=self.open_settings)
        self.view.file.add_command(label='Generate Report', command=self.generate_report)
        self.view.file.add_command(label='Export', command=self.export_database)
        self.view.file.add_separator()
        self.view.file.add_command(label='Exit', command=self.view.destroy)

        if new_user:
            self.welcome_window = WelcomeUser(self.view, self.view.theme)
            self.welcome_window.start_button.configure(command=self.set_user)
        else:
            self.user_id = self.model.get_user_id(self.model.config.user_name)
            # Initialize Day vs Events Graph
            self.initialize_day_event_graph()
            self.update_home()

    def update_home(self):
        self.auto_close_events()
        self.update_contact_listbox_home()
        self.open_job_listbox_view()
        # self.update_home_listbox()
        self.update_home_event_listbox()
        self.update_points_view()
        self.display_user_name()
        self.update_day_event_graph(self.model.config.get_num_of_days())

    def initialize_day_event_graph(self):
        today = datetime.today()
        data = {}
        num_of_days = self.model.config.get_num_of_days()
        days_of_the_week = utils.get_past_dates(today, num_of_days)
        for day in days_of_the_week:
            data[day] = self.model.get_event_count_by_date(day, self.user_id)
        status_values = [status for date_statuses in data.values() for status, _ in date_statuses]
        events = set(status_values)
        self.view.de_graph.day_event_graph(self.view.calendar_frame, data, events)

    def auto_close_events(self):
        """auto close any jobs older the x-days"""
        if self.model.config.get_auto_close_status():

            old_jobs = self.model.get_old_open_jobs(user_id=self.user_id,
                                                    days_since_last_event=self.model.config.get_auto_close_days())
            if old_jobs:
                for job in old_jobs:
                    current_time = datetime.today().time().strftime(constant.CURRENT_TIME_FORMAT)
                    logger.info(f'Auto no response event added to job:{job[0]}')
                    self.model.add_event(date=self.today.strftime(constant.CURRENT_DATE_FORMAT),
                                         time=current_time,
                                         note=constant.AUTO_CLOSE_NOTE,
                                         status_id=11,
                                         contact_id=None,
                                         job_id=job[0],
                                         user_id=self.user_id
                                         )

    def update_day_event_graph(self, num_of_days: int):
        today = datetime.today()
        data = {}
        days_of_the_week = utils.get_past_dates(today, num_of_days)
        for day in days_of_the_week:
            data[day] = self.model.get_event_count_by_date(day, self.user_id)
        status_values = [status for date_statuses in data.values() for status, _ in date_statuses]
        events = set(status_values)
        self.view.de_graph.update_graph(data, events)

    def generate_report(self):
        self.generate_report = GenerateReport(self.view, self.view.theme)
        self.generate_report.generate_button.configure(command=self.open_report)

    def open_report(self):
        start_date = datetime.strptime(self.generate_report.start_date.get(), '%Y-%m-%d')
        end_date = datetime.strptime(self.generate_report.end_date.get(), '%Y-%m-%d')

        self.generate_report.generate_report_window.destroy()
        report = Report(self.view, self.view.theme)

        dates_inbetween = utils.get_dates_between(start_date, end_date)
        data = {}
        for day in dates_inbetween:
            data[day] = self.model.get_event_count_by_date(day, self.user_id)
        status_values = [status for date_statuses in data.values() for status, _ in date_statuses]
        events = set(status_values)
        logger.debug(f'event_vs_day data:{data}')
        report.de_graph.day_event_graph(report.days_vs_event_frame, data, events)

        pie_list = self.model.get_event_total(start_date.strftime('%Y-%m-%d'),end_date.strftime('%Y-%m-%d'), self.user_id)
        pie_data = dict(pie_list)
        logger.debug(f'pie_dict:{pie_data}')
        report.pie_graph.show_pie_chart(report.event_pie_frame, pie_data)

    def set_user(self):
        points = 0
        if self.welcome_window.radio_var.get():
            self.model.config.user_name = self.welcome_window.name_entry.get()
        else:
            self.model.config.user_name = constant.SAMPLE_USER_NAME
            self.model.set_sample_data()
            points = 285
        self.model.config.update_user_name(self.model.config.user_name)
        self.model.add_user(self.model.config.user_name, points)
        self.welcome_window.welcome_window.destroy()
        self.user_id = self.model.get_user_id(self.model.config.user_name)
        self.update_home()
        self.initialize_day_event_graph()

    def change_user(self):
        self.user_select = UserSelect(self.view, self.view.theme)
        self.user_select.submit_button.configure(command=self.switch_users)
        clean_list = []
        res = (self.model.get_all_users())
        for db in res:
            clean_list.append(db[0])
        self.user_select.user_entry.configure(values=clean_list)

    def export_database(self):
        path = filedialog.askdirectory()
        if path:
            self.model.export_database(self.user_id, path)

    def switch_users(self):
        name = self.user_select.user_entry.get()
        self.user_name = name
        self.user_id = self.model.get_user_id(name)
        self.model.config.update_user_name(name)
        self.user_select.user_window.destroy()
        self.update_home()

    def about_page(self):
        open(constant.TOJA_GITHUB_URL)

    def create_user(self):
        self.add_user = CreateUser(self.view, self.view.theme)
        self.add_user.create_button.configure(command=self.submit_new_user)

    def open_settings(self):
        self.settings = Settings(self.view, self.view.theme)
        self.settings.accent_color_button.configure(fg_color=self.model.config.get_accent_color())
        self.settings.button_color_button.configure(fg_color=self.model.config.get_button_color())
        self.settings.num_of_days_dv_graph_entry.configure(placeholder_text=self.model.config.get_num_of_days())
        if self.model.config.icon_mode == constant.DARK_MODE:
            self.settings.icon_mode_switch.select()
        if self.model.config.appearance_mode == constant.DARK_MODE:
            self.settings.appearance_mode_switch.select()

        self.settings.job_keyword_results_entry.configure(
            placeholder_text=self.model.config.get_num_keywords(job_description=True))
        self.settings.resume_keyword_entry.configure(placeholder_text=self.model.config.get_num_keywords(resume=True))
        if self.model.config.get_auto_close_status():
            self.settings.auto_close_switch.select()
        self.settings.auto_close_days_entry.configure(placeholder_text=self.model.config.get_auto_close_days())
        self.settings.apply_button.configure(command=self.apply_settings)
        self.settings.submit_button.configure(command=self.submit_settings)

    def apply_settings(self):
        self.update_icon_mode()
        self.update_appearance_mode()
        self.update_button_color()
        self.update_accent_color()
        num_of_days = self.settings.num_of_days_dv_graph_entry.get()
        if num_of_days:
            self.update_day_event_graph(num_of_days)
        self.view.update_day_event_graph_color_scheme()

    def update_accent_color(self):
        if self.settings.accent_color_button.cget('fg_color'):
            self.model.config.update_accent_color(self.settings.accent_color_button.cget('fg_color'))
            self.model.config.set_accent_color()
            self.view.update_accent_color()
            self.settings.update_accent_color()

    def update_button_color(self):
        if self.settings.button_color_button.cget('fg_color') != self.model.config.theme.button_color:
            self.model.config.update_button_color(self.settings.button_color_button.cget('fg_color'))
            self.model.config.set_button_color()
            self.view.update_button_color()
            self.settings.update_button_color()

    def update_icon_mode(self):
        if not self.settings.icon_mode_switch.get():  # Light mode
            self.model.config.icon_mode = constant.LIGHT_MODE
            self.model.config.update_icon_mode(constant.LIGHT_MODE)
        else:  # Dark mode
            self.model.config.icon_mode = constant.DARK_MODE
            self.model.config.update_icon_mode(constant.DARK_MODE)
        self.model.config.set_icon_mode()
        self.view.update_icon_mode()
        self.model.config.set_button_text_color(self.model.config.icon_mode)
        self.settings.update_icon_text()

    def submit_settings(self):
        if not self.settings.appearance_mode_switch.get():  # Light mode
            self.model.config.appearance_mode = constant.LIGHT_MODE
            self.model.config.update_appearance_mode(constant.LIGHT_MODE)
            customtkinter.set_appearance_mode(constant.LIGHT_MODE)
        else:  # Dark mode
            self.model.config.appearance_mode = constant.DARK_MODE
            self.model.config.update_appearance_mode(constant.DARK_MODE)
            customtkinter.set_appearance_mode(constant.DARK_MODE)
        self.update_keyword_settings()
        self.update_appearance_mode()
        num_of_days = self.settings.num_of_days_dv_graph_entry.get()
        if num_of_days:
            self.model.config.set_num_of_days(num_of_days)
            self.update_day_event_graph(num_of_days)
        days_after = self.settings.auto_close_days_entry.get()
        if days_after:
            self.model.config.set_auto_close_days(days_after)
        if self.settings.auto_close_switch.get():
            self.model.config.set_auto_close_status(True)
        else:
            self.model.config.set_auto_close_status(False)
        self.settings.settings_window.destroy()

    def update_keyword_settings(self):
        if self.settings.job_keyword_results_entry.get():
            self.model.config.update_keywords(self.settings.job_keyword_results_entry.get(), job_description=True)
        if self.settings.resume_keyword_entry.get():
            self.model.config.update_keywords(self.settings.resume_keyword_entry.get(), resume=True)

    def update_appearance_mode(self):
        if not self.settings.appearance_mode_switch.get():  # Light mode
            self.model.config.appearance_mode = constant.LIGHT_MODE
            self.model.config.update_appearance_mode(constant.LIGHT_MODE)
        else:  # Dark mode
            self.model.config.appearance_mode = constant.DARK_MODE
            self.model.config.update_appearance_mode(constant.DARK_MODE)
        self.model.config.set_appearance_mode()
        self.view.update_icon_paths()
        self.view.update_home_theme()
        self.model.config.set_button_color()

    def submit_new_user(self):
        new_name = self.add_user.user_name_entry.get()
        self.model.config.update_user_name(new_name)
        self.model.add_user(new_name, 0)
        self.user_id = self.model.get_user_id(new_name)
        self.add_user.window.destroy()
        self.update_home()

    def update_home_listbox(self, home_listbox: list):
        # self.current_user = self.model.get_user_id(self.model.config.user_name)
        self.view.job_list_box.delete(constant.START_RANGE_LISTBOX, constant.END_RANGE_LISTBOX)

        # home_listbox = self.model.get_home_view_listbox(self.user_id)
        for item in home_listbox:
            self.view.job_list_box.insert(tkinter.END,
                                          f"{item[0]}  |  {item[1]}  |  {item[2]}")

    def open_job_listbox_view(self):
        if self.view.open_jobs_switch.get() == 0:
            self.update_home_listbox(self.model.get_home_view_listbox(self.user_id))
            self.model.config.set_open_jobs_only(False)
        else:
            self.update_home_listbox(self.model.get_open_home_view_listbox(self.user_id))
            self.model.config.set_open_jobs_only(True)

    def set_open_jobs_only_switch(self):
        switch = self.model.config.get_open_jobs_only()
        if switch:
            self.view.open_jobs_switch.select()

    def double_click_job(self, event):
        event_str = (self.view.job_list_box.get(self.view.job_list_box.curselection()))
        self.job_id = (event_str.split())[0]
        self.open_job_profile()

    def double_click_event_past(self, event):
        past_event = self.view.past_events_listbox.get(self.view.past_events_listbox.curselection())
        self.event_id = (past_event.split())[0]
        self.open_event()

    def double_click_event_upcoming(self, event):
        upcoming_event = self.view.upcoming_events_listbox.get(self.view.upcoming_events_listbox.curselection())
        self.event_id = (upcoming_event.split())[0]
        self.open_event()

    def double_click_event_job_profile(self, event):
        event_job = self.job_profile.event_scroll.get(self.job_profile.event_scroll.curselection())
        self.job_profile.event_scroll.bind('<Double-Button-1>', self.double_click_event_job_profile)
        self.event_id = (event_job.split())[0]
        self.open_event()

    def double_click_contact_home(self, event):
        contact = self.view.contact_listbox.get(self.view.contact_listbox.curselection())
        self.contact_id = (contact.split())[0]
        self.open_contact()

    def double_click_contact(self, event):
        contact = self.job_profile.contact_listbox.get(self.job_profile.contact_listbox.curselection())
        self.contact_id = (contact.split())[0]
        self.open_contact()

    def open_event(self):
        self.event = Event(self.view)
        self.event.event_window.grab_set()
        event_results = self.model.get_event(self.event_id, event=True)[0]
        self.event.event_id.configure(text=self.event_id)
        self.event.event_status.configure(text=event_results[2])
        self.event.day_entry.configure(text=event_results[0])
        self.event.time_entry.configure(text=event_results[1])
        self.event.company_entry.configure(text=event_results[3])
        self.event.position_entry.configure(text=event_results[4])
        self.event.contact_entry.configure(text=f'{event_results[5]} {event_results[6]}')
        self.event.note_entry.configure(text=event_results[7])

    def open_contact(self):
        self.contact = Contact(self.view)
        self.contact.contact_window.grab_set()
        contact_results = self.model.get_contacts(self.contact_id, get_contact_by_id=True)[0]
        self.contact.contact_id.configure(text=self.contact_id)
        self.contact.first_name.configure(text=contact_results[1])
        self.contact.last_name.configure(text=contact_results[2])
        self.contact.email.configure(text=contact_results[3])
        self.contact.phone.configure(text=contact_results[4])
        self.contact.position.configure(text=contact_results[5])
        self.contact.job_id.configure(text=contact_results[6])

    def update_job_profile(self):
        self.jp_results = self.model.get_job_data(self.job_id)
        self.job_profile.job_id_user.configure(text=self.job_id)
        self.job_profile.company_name_user.configure(text=self.jp_results[0])
        self.job_profile.company_web_user.configure(text=self.jp_results[1])
        self.job_profile.position_user.configure(text=self.jp_results[2])
        self.job_profile.location_user.configure(text=self.jp_results[3])
        self.job_profile.commitment_user.configure(text=self.jp_results[4])
        self.job_profile.work_type_user.configure(text=self.jp_results[5])
        self.job_profile.salary_top_user.configure(text=self.jp_results[6])
        self.job_profile.salary_bottom_user.configure(text=self.jp_results[7])
        self.job_profile.salary_type_user.configure(text=self.jp_results[8])
        self.job_profile.resume_user.configure(text=self.jp_results[9])
        if self.jp_results[10]:  # return blank if file is NULL
            self.job_profile.job_description_label.configure(text=self.model.open_job_description(self.jp_results[10]))
        else:
            self.job_profile.job_description_label.configure(text='')
        self.update_profile_keywords()

    def open_job_profile(self) -> None:
        self.job_profile = JobProfile(self.view, self.model.config.theme)
        self.job_profile.new_contact_button.configure(command=self.add_contact)
        self.job_profile.new_event_button.configure(command=self.open_new_event)
        self.job_profile.edit_button.configure(command=self.edit_job)
        self.job_profile.edit_job_button.configure(command=self.edit_job_description)
        self.update_job_profile()
        self.update_event_listbox()
        self.update_contact_listbox()

    def update_profile_keywords(self):
        self.profile_keywords = KeywordExtractor()
        self.profile_keywords.text = self.job_profile.job_description_label.cget("text")
        extracted_keywords = self.profile_keywords.extract_keywords(self.profile_keywords.text.lower())
        for keywords in extracted_keywords:
            self.job_profile.keyword_scroll.insert(tkinter.END, keywords)

    def add_contact(self):
        self.contact = NewContact(self.view, self.view.theme)
        self.contact.contact_window.grab_set()
        self.contact.submit_contact_button.configure(command=self.insert_contact)

    def add_contact_home(self):
        self.contact = NewContact(self.view, self.view.theme)
        self.contact.job_id_entry.grid(row=1, column=1, padx=(5, 20), pady=10)
        self.contact.job_id_label.grid(row=1, column=0, padx=(20, 5), pady=10, sticky="e")
        self.contact.submit_contact_button.configure(command=self.insert_contact_home)

    def edit_job(self):
        self.edit = EditJob(self.view.home_frame, self.view.theme)
        self.edit.ej_window.grab_set()
        self.edit.submit_edit_button.configure(command=self.submit_job_edit)
        self.edit.position_title_entry.configure(placeholder_text=self.jp_results[2])
        self.edit.company_name_entry.configure(placeholder_text=self.jp_results[0])
        self.edit.company_website_entry.configure(placeholder_text=self.jp_results[1])
        self.edit.job_location_entry.configure(placeholder_text=self.jp_results[3])
        self.edit.resume_version_entry.configure(placeholder_text=self.jp_results[9])
        self.edit.salary_top_entry.configure(placeholder_text=self.jp_results[6])
        self.edit.salary_bottom_entry.configure(placeholder_text=self.jp_results[7])

    def submit_job_edit(self):
        entry_list = {
            'position': self.edit.position_title_entry,
            'company': self.edit.company_name_entry,
            'website': self.edit.company_website_entry,
            'location': self.edit.job_location_entry,
            'resume_version': self.edit.resume_version_entry,
            'salary_top': self.edit.salary_top_entry,
            'salary_bottom': self.edit.salary_bottom_entry,
            'salary_type': self.edit.salary_type_entry,
            'work_type': self.edit.location_type_entry,
            'commitment': self.edit.job_type_entry,
        }
        for key, value in entry_list.items():
            if value.get():
                self.model.update_job(self.job_id, key, value.get())

        self.edit.ej_window.destroy()
        self.update_job_profile()
        self.open_job_listbox_view()
        # self.update_home_listbox()

    def insert_contact(self):
        self.model.add_contact(
            self.contact.first_name_entry.get(),
            self.contact.last_name_entry.get(),
            self.contact.email_entry.get(),
            self.contact.phone_entry.get(),
            self.contact.position_entry.get(),
            self.job_id,
            self.user_id
        )
        self.update_contact_listbox()
        self.update_contact_listbox_home()
        self.contact.contact_window.destroy()

    def insert_contact_home(self):
        self.model.add_contact(
            self.contact.first_name_entry.get(),
            self.contact.last_name_entry.get(),
            self.contact.email_entry.get(),
            self.contact.phone_entry.get(),
            self.contact.position_entry.get(),
            self.contact.job_id_entry.get(),
            self.user_id
        )
        self.update_contact_listbox_home()
        self.contact.contact_window.destroy()

    def delete_job(self):
        event_str = (self.view.job_list_box.get(self.view.job_list_box.curselection()))
        self.job_id = (event_str.split())[0]
        company = (event_str.split("|"))[1]
        position = (event_str.split("|"))[2]
        if messagebox.askyesno("Delete Job", message=f'Are you sure you want to delete{company}{position}?'):
            self.model.delete_job_txt_file(self.job_id)
            self.model.delete_entry('job', 'job_id', self.job_id)
            self.update_home()

    def delete_contact(self):
        event_str = self.view.contact_listbox.get(self.view.contact_listbox.curselection())
        contact_id = (event_str.split())[0]
        name = (event_str.split("|"))[1]
        if messagebox.askyesno("Delete Contact", message=f'Are you sure you want to delete{name}?'):
            self.model.delete_entry('contact', 'contact_id', contact_id)
            self.update_contact_listbox_home()

    def delete_event(self):
        past_event = self.view.past_events_listbox.curselection()
        upcoming_event = self.view.upcoming_events_listbox.curselection()
        event_str = ''
        if past_event:
            event_str = self.view.past_events_listbox.get(self.view.past_events_listbox.curselection())
        if upcoming_event:
            event_str = self.view.upcoming_events_listbox.get(self.view.upcoming_events_listbox.curselection())
        event_id = (event_str.split())[0]
        if messagebox.askyesno("Delete Contact", message=f'Are you sure you want to delete event?'):
            self.model.delete_entry('event', 'event_id', event_id)
            self.update_home_event_listbox()
            self.update_day_event_graph(self.model.config.get_num_of_days())

    def run(self):
        self.view.mainloop()

    def open_job_submit(self):
        self.new_job = NewJob(self.view, self.view.theme)
        self.new_job.submit_button.configure(command=self.validate_new_job)

        current_time = datetime.today().time().strftime(constant.CURRENT_TIME_FORMAT)
        self.current_time = customtkinter.StringVar()
        self.current_time.set(current_time)
        self.new_job.time_entry.configure(textvariable=self.current_time)

    def open_new_event(self):
        current_time = datetime.today().time().strftime(constant.CURRENT_TIME_FORMAT)
        self.current_time = customtkinter.StringVar()
        self.current_time.set(current_time)
        self.new_event = NewEvent(self.view, self.view.theme)
        self.new_event.event_window.grab_set()
        contacts = self.model.get_contacts(self.job_id)
        self.new_event.time_entry.configure(textvariable=self.current_time)
        contact_list = []
        for contact in contacts:
            contact_list.append(f'{contact[0]}| {contact[1]} {contact[2]}')
        self.new_event.contact_entry.configure(values=contact_list)
        self.new_event.submit_event_button.configure(command=self.submit_new_event)

    def submit_new_event(self):
        contact_id = (self.new_event.contact_entry.get().split("|")[0])
        status_id = self.model.get_status_id(self.new_event.event_entry.get())[0][0]
        self.model.add_event(
            self.new_event.day_entry.get(),
            self.new_event.time_entry.get(),
            self.new_event.note_entry.get(constant.START_RANGE_TEXTBOX, constant.END_RANGE_TEXTBOX),
            status_id,
            contact_id,
            self.job_id,
            self.user_id)
        self.update_home()
        self.update_event_listbox()
        self.new_event.event_window.destroy()

    def auto_close_jobs(self):
        """Add 'no-response' event to job after x-days defined by user"""
        old_jobs = self.model.get_old_open_jobs(self.user_id, 30)
        print(old_jobs)

    def submit_new_event_home(self):
        contact_id = (self.new_event.contact_entry.get().split("|")[0])
        status_id = self.model.get_status_id(self.new_event.event_entry.get())[0][0]
        job_id = self.new_event.job_id_entry.get()
        if not job_id:
            job_id = None

        self.model.add_event(
            self.new_event.day_entry.get(),
            self.new_event.time_entry.get(),
            self.new_event.note_entry.get(constant.START_RANGE_TEXTBOX, constant.END_RANGE_TEXTBOX),
            status_id,
            contact_id,
            job_id,
            self.user_id)
        self.update_home()
        self.new_event.event_window.destroy()

    def new_event_home(self):
        current_time = datetime.today().time().strftime(constant.CURRENT_TIME_FORMAT)
        self.current_time = customtkinter.StringVar()
        self.current_time.set(current_time)
        self.new_event = NewEvent(self.view, self.view.theme)
        self.new_event.job_id_entry.grid(row=0, column=1, padx=(5, 20), pady=10)
        self.new_event.job_id_label.grid(row=0, column=0, padx=(20, 5), pady=10, sticky="e")
        contacts = self.model.get_all_contacts(self.user_id)
        self.new_event.time_entry.configure(textvariable=self.current_time)
        contact_list = []
        for contact in contacts:
            contact_list.append(f'{contact[0]}| {contact[1]} {contact[2]}')
        self.new_event.contact_entry.configure(values=contact_list)
        self.new_event.submit_event_button.configure(command=self.submit_new_event_home)

    def validate_new_job(self):
        self.company = self.new_job.company_name_entry.get()
        self.position = self.new_job.position_title_entry.get()
        if utils.validate_file_name(f'{self.company}{self.position}'):
            self.submit_new_job()
        else:
            utils.showerror(self.new_job.aj_window, 'Invalid character in Position or Company')

    def submit_new_job(self):
        self.job_file = None
        job_text = self.new_job.job_description_textbox.get(constant.START_RANGE_TEXTBOX, constant.END_RANGE_TEXTBOX)
        if job_text:
            self.job_file = f'{self.model.config.user_name}_{self.company}_{self.position}.txt'

        self.model.add_new_job(
            self.position,
            self.company,
            self.new_job.company_website_entry.get(),
            self.new_job.job_location_entry.get(),
            self.new_job.job_type_entry.get(),
            self.new_job.location_type_entry.get(),
            self.new_job.salary_top_entry.get(),
            self.new_job.salary_bottom_entry.get(),
            self.new_job.salary_type_entry.get(),
            self.new_job.resume_version_entry.get(),
            self.job_file,
            self.user_id,
            self.new_job.day_entry.get(),
            self.new_job.time_entry.get(),
            self.new_job.note_entry.get(constant.START_RANGE_TEXTBOX, constant.END_RANGE_TEXTBOX),
            self.new_job.event_entry.get(),
            None,
        )
        if self.job_file:
            self.model.save_job_description(self.job_file, job_text)
        self.update_home()
        self.new_job.aj_window.destroy()

    def update_event_listbox(self):
        self.job_profile.event_scroll.bind('<Double-Button-1>', self.double_click_event_job_profile)
        self.job_profile.event_scroll.delete(constant.START_RANGE_LISTBOX, constant.END_RANGE_LISTBOX)
        event_listbox = self.model.get_event(self.job_id, job=True)
        for item in event_listbox:
            self.job_profile.event_scroll.insert(tkinter.END,
                                                 f"{item[0]} | {item[1]} | {item[2]} | {item[4]} ")

    def update_home_event_listbox(self):
        self.view.past_events_listbox.delete(constant.START_RANGE_LISTBOX, constant.END_RANGE_LISTBOX)
        past_event_listbox = self.model.get_all_event(self.user_id)
        for item in past_event_listbox:
            self.view.past_events_listbox.insert(tkinter.END,
                                                 f"{item[0]} | {item[1]} | {item[2]} | {item[4]}")
        self.view.upcoming_events_listbox.delete(constant.START_RANGE_LISTBOX, constant.END_RANGE_LISTBOX)
        upcoming_event_listbox = self.model.get_all_event(self.user_id, future=True)
        for item in upcoming_event_listbox:
            self.view.upcoming_events_listbox.insert(tkinter.END,
                                                     f"{item[0]} | {item[1]} | {item[2]} | {item[4]} ")

    def update_contact_listbox(self):
        self.job_profile.contact_listbox.bind('<Double-Button-1>', self.double_click_contact)
        self.job_profile.contact_listbox.delete(constant.START_RANGE_LISTBOX, constant.END_RANGE_LISTBOX)
        contacts = self.model.get_contacts(self.job_id)
        for item in contacts:
            self.job_profile.contact_listbox.insert(tkinter.END,
                                                    f'{item[0]} | {item[1]} {item[2]} ')

    def update_contact_listbox_home(self):
        self.view.contact_listbox.delete(constant.START_RANGE_LISTBOX, constant.END_RANGE_LISTBOX)
        contacts = self.model.get_all_contacts(self.user_id)
        for item in contacts:
            self.view.contact_listbox.insert(tkinter.END,
                                             f'{item[0]} | {item[1]} {item[2]} | {item[5]}')

    def edit_job_description(self):
        if self.jp_results[10]:  # return blank if file is NULL
            full_job_path = Path(*[self.model.config.job_description_parent, self.jp_results[10]])
            user_platform = self.model.config.get_users_system()

            if user_platform == 'Windows':
                subprocess.run(['start', '', full_job_path], shell=True, check=True)
            elif user_platform == 'Darwin':  # macOS
                subprocess.run(['open', full_job_path], check=True)
            elif user_platform == 'Linux':
                subprocess.run(['xdg-open', full_job_path], check=True)
            else:
                print("Unsupported operating system.")
        else:
            self.new_job_description = JobDescriptionView(self.view)
            self.new_job_description.submit_job_description.configure(command=self.save_job_description)

    def save_job_description(self):
        self.job_file_only = None
        job_text = self.new_job_description.job_description_textbox_only.get(
            constant.START_RANGE_TEXTBOX, constant.END_RANGE_TEXTBOX)

        if job_text:
            self.job_file_only = f'{self.model.config.user_name}_{self.jp_results[0]}_{self.jp_results[2]}.txt'
            self.model.save_job_description(self.job_file_only, job_text)

        self.new_job_description.jd_window.destroy()
        self.model.update_job(self.job_id, 'job_description_file', self.job_file_only)
        self.update_job_description()

    def update_job_description(self):
        self.job_profile.job_description_label.configure(text=self.model.open_job_description(self.job_file_only))

    def update_points_view(self):
        total_points = self.model.get_total_points(self.user_id)
        self.view.total_points.configure(text=total_points)
        progress = total_points / 50
        level, progress_value = divmod(progress, 1)
        self.view.current_level.configure(text=(int(level)))
        self.view.progress_bar.set(progress_value)

    def display_user_name(self):
        self.view.user_name_label.configure(text=self.model.config.user_name)

    def search_job_button(self):
        self.list_of_jobs = None
        if self.view.radio_var.get() == 0:
            self.list_of_jobs = self.model.get_filenames(self.user_id)
        elif self.view.radio_var.get() == 1:
            job_entry = self.view.job_id_entry.get()
            self.list_of_jobs = self.model.get_filenames(self.user_id, job_id=job_entry, single_job=True)
        elif self.view.radio_var.get() == 2:
            position = self.view.position_entry.get()
            if self.view.threshold_entry.get():
                threshold = int(self.view.threshold_entry.get())
            else:
                threshold = 80
            self.list_of_jobs = self.model.get_filenames_fuzzy(self.user_id, position, threshold=threshold)
        self.job_description = JobDescription()
        self.job_description.num_of_jobs = len(self.list_of_jobs)
        text = utils.load_job_file(self.list_of_jobs, self.model.config.job_description_parent)
        self.jd_keywords = KeywordExtractor()
        self.extracted_keywords = self.jd_keywords.extract_keywords(text,
                                                                    num_keywords=self.model.config.get_num_keywords(
                                                                        job_description=True))
        self.update_jd_keyword_listbox()
        self.job_description.keywords = self.extracted_keywords

    def get_position_fuzzy(self):
        if self.view.threshold_entry.get():
            threshold = int(self.view.threshold_entry.get())
        else:
            threshold = 80
        return self.model.get_position_fuzzy(self.user_id, self.view.position_entry.get(), threshold=threshold)

    def display_position(self):
        results = self.get_position_fuzzy()
        display_results = ''
        for position in results:
            display_results += str(position)
            display_results += '\n'
        self.view.position_tooltip.configure(message=display_results)

    def update_jd_keyword_listbox(self):
        self.view.jd_search_listbox.delete(constant.START_RANGE_LISTBOX, constant.END_RANGE_LISTBOX)
        for item in self.extracted_keywords:
            self.view.jd_search_listbox.insert(tkinter.END, f'{item[0]} | {item[1]} ')

    def browse_resume_button(self):
        self.resume = Resume()
        self.resume.resume_path = filedialog.askopenfilename()
        file_name = os.path.basename(self.resume.resume_path)
        self.view.upload_resume.configure(text=file_name)

    def search_resume_button(self):
        resume_extractor = KeywordExtractor()
        self.resume.keywords = resume_extractor.extract_pdf_text(self.resume.resume_path)
        self.extracted_resume_keywords = resume_extractor.extract_keywords(self.resume.keywords,
                                                                           num_keywords=self.model.config.get_num_keywords(
                                                                               resume=True))
        self.update_resume_keyword_listbox()
        self.resume.keywords = self.extracted_resume_keywords
        self.get_resume_score()

    def get_resume_score(self):
        score = resume_score(self.resume.keywords, self.job_description.keywords, self.job_description.num_of_jobs)
        self.view.resume_score.configure(text=score)

    def update_resume_keyword_listbox(self):
        self.view.resume_search_listbox.delete(constant.START_RANGE_LISTBOX, constant.END_RANGE_LISTBOX)
        for item in self.extracted_resume_keywords:
            self.view.resume_search_listbox.insert(tkinter.END, f'{item[0]} | {item[1]} ')
