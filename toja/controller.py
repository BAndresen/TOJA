import customtkinter
import tkinter
from datetime import datetime
from typing import Union
from webbrowser import open
from tkinter import filedialog, messagebox
import subprocess
from pathlib import Path

from views.new_job import NewJob
from views.job_profile import JobProfile
from views.home import HomeView
from views.new_event import NewEvent
from views.new_contact import NewContact
from views.edit_job import EditJob
from views.job_description import JobDescription
from views.welcome_user import WelcomeUser
from views.user_database_select import UserSelect
from views.new_user import CreateUser
from model import Model


class Controller:
    def __init__(self, view: HomeView, model: Model, new_user: bool = False):
        self.today = datetime.today().date()
        self.new_job = None
        self.view = view
        self.model = model
        self.new_user = new_user

        # HomeView Button Commands
        self.view.events_button.configure(command=self.event_frame_button)
        self.view.home_button.configure(command=self.home_frame_button)
        self.view.analytics_button.configure(command=self.analytics_frame_button)
        self.view.new_job_button.configure(command=self.open_job_submit)
        self.view.delete_job_button.configure(command=self.delete)

        # HomeView ListBox
        self.view.job_list_box.bind('<Double-Button-1>', self.double_click_job)
        self.view.job_list_box.bind('<Return>', self.double_click_job)

        # file menu
        self.view.help_.add_command(label='About Toja', command=self.about_page)
        self.view.file.add_command(label='New User', command=self.create_user)
        self.view.file.add_command(label='Change User', command=self.change_database)
        self.view.file.add_separator()
        self.view.file.add_command(label='Exit', command=self.view.destroy)

        if new_user:
            self.welcome_window = WelcomeUser(self.view)
            self.welcome_window.start_button.configure(command=self.set_user)
        else:
            self.user_id = self.model.get_user_id(self.model.user_name)
            self.update_home_listbox()
            self.update_home_event_listbox()

    def set_user(self):
        if self.welcome_window.radio_var.get():
            self.model.user_name = self.welcome_window.name_entry.get()
        else:
            self.model.user_name = 'sample'
            self.model.set_sample_data()
        self.model.user.set_database_name(self.model.user_name)
        self.model.insert_user_db(self.model.user.user_name, 0)
        self.welcome_window.welcome_window.destroy()
        self.user_id = self.model.get_user_id(self.model.user_name)
        self.update_home_listbox()
        self.update_home_event_listbox()

    def change_database(self):
        self.user_select = UserSelect(self.view)
        self.user_select.submit_button.configure(command=self.switch_users)
        clean_list = []
        res = (self.model.get_all_users())
        for db in res:
            clean_list.append(db[0])
        self.user_select.user_entry.configure(values=clean_list)

    def switch_users(self):
        name = self.user_select.user_entry.get()
        self.user_name = name
        self.user_id = self.model.get_user_id(name)
        self.model.user.set_database_name(name)
        self.user_select.user_window.destroy()
        self.update_home_listbox()
        self.update_home_event_listbox()

    def about_page(self):
        open('https://github.com/BAndresen/TOJA')

    def create_user(self):
        self.add_user = CreateUser(self.view)
        self.add_user.create_button.configure(command=self.submit_new_user)

    def submit_new_user(self):
        new_name = self.add_user.database_name_entry.get()
        self.model.user.set_database_name(new_name)
        self.model.insert_user_db(new_name, 0)
        self.user_id = self.model.get_user_id(new_name)
        self.add_user.window.destroy()
        self.update_home_listbox()
        self.update_home_event_listbox()

    def update_home_listbox(self):
        self.current_user = self.model.get_user_id(self.model.user.user_name)
        self.view.job_list_box.delete('0', 'end')

        home_listbox = self.model.get_home_view_listbox(self.current_user)
        for item in home_listbox:
            self.view.job_list_box.insert(tkinter.END, f"{item[0]} | {item[1]} | {item[2]}")

    def double_click_job(self, event):
        event_str = (self.view.job_list_box.get(self.view.job_list_box.curselection()))
        self.job_id = (event_str.split())[0]
        self.open_job_profile()


    def update_job_profile(self):
        self.jp_results = self.model.get_job_data(self.job_id)
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

    def open_job_profile(self) -> None:
        self.job_profile = JobProfile(self.view)
        self.job_profile.new_contact_button.configure(command=self.add_contact)
        self.job_profile.new_event_button.configure(command=self.open_new_event)
        self.job_profile.edit_button.configure(command=self.edit_job)
        self.job_profile.edit_job_button.configure(command=self.edit_job_description)
        self.update_job_profile()
        self.update_event_listbox()
        self.update_contact_listbox()

    def add_contact(self):
        self.contact = NewContact(self.view)
        self.contact.submit_contact_button.configure(command=self.insert_contact)

    def edit_job(self):
        self.edit = EditJob(self.view.home_frame)
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
        self.update_home_listbox()

    def insert_contact(self):
        self.model.add_contact(
            self.contact.first_name_entry.get(),
            self.contact.last_name_entry.get(),
            self.contact.email_entry.get(),
            self.contact.phone_entry.get(),
            self.contact.position_entry.get(),
            self.job_id,
            self.current_user
        )
        self.update_contact_listbox()
        self.contact.contact_window.destroy()

    def delete(self):
        event_str = (self.view.job_list_box.get(self.view.job_list_box.curselection()))
        self.job_id = (event_str.split())[0]
        if messagebox.askyesno("Delete Job", message=f'Are you sure you want to delete?'):
            self.model.delete_job_txt_file(self.job_id)
            self.model.delete_job(self.job_id)
            self.update_home_listbox()
            self.update_home_event_listbox()

    def run(self):
        self.view.mainloop()

    def event_frame_button(self):
        self.view.home_frame.grid_forget()
        self.view.analytics_frame.grid_forget()
        self.view.event_frame.grid(row=0, column=1, sticky="nsew")

    def home_frame_button(self):
        self.view.event_frame.grid_forget()
        self.view.analytics_frame.grid_forget()
        self.view.home_frame.grid(row=0, column=1, sticky="nsew")

    def analytics_frame_button(self):
        self.view.home_frame.grid_forget()
        self.view.event_frame.grid_forget()
        self.view.analytics_frame.grid(row=0, column=1, sticky="nsew")

    def open_job_submit(self):
        self.new_job = NewJob(self.view)
        self.new_job.submit_button.configure(command=self.submit_new_job)

        current_time = datetime.today().time().strftime('%I:%M%p')
        self.current_time = customtkinter.StringVar()
        self.current_time.set(current_time)
        self.new_job.time_entry.configure(textvariable=self.current_time)

    def open_new_event(self):
        current_time = datetime.today().time().strftime('%I:%M%p')
        self.current_time = customtkinter.StringVar()
        self.current_time.set(current_time)
        self.new_event = NewEvent(self.view)
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
            self.new_event.note_entry.get("1.0", "end-1c"),
            status_id,
            contact_id,
            self.job_id,
            self.current_user)
        self.update_event_listbox()
        self.update_home_event_listbox()
        self.new_event.event_window.destroy()

    def submit_new_job(self):
        self.company = self.new_job.company_name_entry.get()
        self.position = self.new_job.position_title_entry.get()
        self.job_file = f'{self.model.user.user_name}_{self.new_job.company_name_entry.get()}_{self.new_job.position_title_entry.get()}.txt',
        job_text = self.new_job.job_description_textbox.get("1.0", "end-1c")
        self.job_file = self.check_job_file(self.job_file, job_text)
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
            self.current_user,
            self.new_job.day_entry.get(),
            self.new_job.time_entry.get(),
            self.new_job.note_entry.get("1.0", "end-1c"),
            self.new_job.event_entry.get(),
            None,
        )
        if self.job_file:
            self.model.save_job_description(self.job_file, job_text)

        self.update_home_listbox()
        self.update_home_event_listbox()
        self.new_job.aj_window.destroy()

    def check_job_file(self, job_file, job_text) -> Union[str, None]:
        if job_text == "":
            return None
        else:
            return job_file[0]

    def update_event_listbox(self):
        self.job_profile.event_scroll.delete('0', 'end')

        event_listbox = self.model.get_event(self.job_id)
        for item in event_listbox:
            self.job_profile.event_scroll.insert(tkinter.END,
                                                 f"{item[0]} | {item[1]} | {item[3]} | {item[2]}")

    def update_home_event_listbox(self):
        self.view.past_events_listbox.delete('0', 'end')
        past_event_listbox = self.model.get_all_event(self.user_id)
        for item in past_event_listbox:
            self.view.past_events_listbox.insert(tkinter.END,
                                                 f"{item[0]} | {item[1]} | {item[3]} | {item[2]}")
        self.view.upcoming_events_listbox.delete('0', 'end')
        upcoming_event_listbox = self.model.get_all_event(self.user_id, future=True)
        for item in upcoming_event_listbox:
            self.view.upcoming_events_listbox.insert(tkinter.END,
                                                     f"{item[0]} | {item[1]} | {item[3]} | {item[2]}")

    def update_contact_listbox(self):
        self.job_profile.contact_listbox.delete('0', 'end')
        contacts = self.model.get_contacts(self.job_id)
        for item in contacts:
            self.job_profile.contact_listbox.insert(tkinter.END,
                                                    f'{item[1]} | {item[2]} | {item[3]} | {item[4]} | {item[5]}')

    def edit_job_description(self):
        if self.jp_results[10]:  # return blank if file is NULL
            full_job_path = Path(*[self.model.job_description_parent, self.jp_results[10]])
            user_platform = self.model.user.get_users_system()

            if user_platform == 'Windows':
                subprocess.run(['start', '', full_job_path], shell=True, check=True)
            elif user_platform == 'Darwin':  # macOS
                subprocess.run(['open', full_job_path], check=True)
            elif user_platform == 'Linux':
                subprocess.run(['xdg-open', full_job_path], check=True)
            else:
                print("Unsupported operating system.")
        else:
            self.new_job_description = JobDescription(self.view)
            self.new_job_description.submit_job_description.configure(command=self.save_job_description)

    def save_job_description(self):
        self.job_file_only = f'{self.model.user.user_name}_{self.jp_results[0]}_{self.jp_results[2]}.txt',
        job_text = self.new_job_description.job_description_textbox_only.get("1.0", "end-1c")
        self.job_file_only = self.check_job_file(self.job_file_only, job_text)
        if self.job_file_only:
            self.model.save_job_description(self.job_file_only, job_text)

        self.new_job_description.jd_window.destroy()

        self.model.update_job(self.job_id, 'job_description_file', self.job_file_only)
        self.update_job_description()

    def update_job_description(self):
        self.job_profile.job_description_label.configure(text=self.model.open_job_description(self.job_file_only))
