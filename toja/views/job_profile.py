import tkinter
import customtkinter
import os
from PIL import Image
import webbrowser

from views.theme import Theme
import constants as constant


class JobProfile:
    def __init__(self, root, theme: Theme):
        self.root = root
        self.jp_window = customtkinter.CTkToplevel(root)
        self.jp_window.attributes('-topmost', 'true')
        self.jp_window.title("Job")

        screen_width = self.jp_window.winfo_screenwidth()
        screen_height = self.jp_window.winfo_screenheight()
        x_position = 450  # Start from the left edge
        y_position = 10  # Start from the top edge

        self.jp_window.geometry(f'{screen_width - 1020}x{screen_height - 180}+{x_position}+{y_position}')
        self.jp_window.grid_columnconfigure(0, weight=1)

        icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), constant.ICON_FILE_DIRECTORY)
        pencil_white = customtkinter.CTkImage(Image.open(os.path.join(icon_path, theme.icon_pencil)),
                                              size=(17, 17))
        writing_white = customtkinter.CTkImage(Image.open(os.path.join(icon_path, theme.icon_writing)),
                                               size=(20, 20))
        add_event_white = customtkinter.CTkImage(Image.open(os.path.join(icon_path, theme.icon_event)),
                                                 size=(20, 20))
        contact_white = customtkinter.CTkImage(Image.open(os.path.join(icon_path, theme.icon_contact)),
                                               size=(20, 20))

        # job_profile
        self.jp_frame = customtkinter.CTkFrame(self.jp_window)
        self.jp_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')
        self.jp_frame.grid_columnconfigure(0, weight=1)

        # company website
        self.company_frame = customtkinter.CTkFrame(self.jp_frame, fg_color=theme.main_frame)
        self.company_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5), sticky='nsew')
        self.company_frame.grid_columnconfigure(2, weight=1)

        self.company_name_user = customtkinter.CTkLabel(self.company_frame, text='', font=theme.title_font)
        self.company_name_user.grid(row=0, column=0, padx=20, pady=(6, 0), sticky='w')
        self.position_user = customtkinter.CTkLabel(self.company_frame, text='', font=theme.header_font)
        self.position_user.grid(row=1, column=0, padx=20, pady=(0, 10), stick='w')

        # job info
        self.job_info_frame = customtkinter.CTkFrame(self.jp_frame, fg_color=theme.main_frame)
        self.job_info_frame.grid(row=1, column=0, padx=10, pady=5, sticky='nsew')
        self.job_info_frame.grid_columnconfigure(0, weight=1)
        self.job_info_frame.grid_columnconfigure(1, weight=4)
        self.company_button_frame = customtkinter.CTkFrame(self.company_frame)
        self.company_button_frame.grid(row=0, column=2, sticky="e", pady=10, padx=10, rowspan=2)

        self.edit_button = customtkinter.CTkButton(self.company_button_frame, text="", image=pencil_white, width=35,
                                                   height=35,
                                                   fg_color=theme.button_color, hover_color='grey15')
        self.edit_button.grid(row=0, column=0, padx=6, pady=6)

        self.job_id = customtkinter.CTkLabel(self.job_info_frame, text="job_id:")
        self.job_id.grid(row=0, column=0, padx=5, pady=(10, 1), stick='e')
        self.job_id_user = customtkinter.CTkLabel(self.job_info_frame, text='', font=theme.main_font_bold)
        self.job_id_user.grid(row=0, column=1, padx=5, pady=(10, 1), stick='w')
        self.company_web = customtkinter.CTkLabel(self.job_info_frame, text="Website:")
        self.company_web.grid(row=1, column=0, padx=5, pady=1, sticky='e')
        self.company_web_user = customtkinter.CTkLabel(self.job_info_frame, text='', font=theme.main_font_bold)
        self.company_web_user.grid(row=1, column=1, padx=5, pady=1, sticky='w')
        self.company_web_user.bind("<Button-1>", self.open_link)
        self.company_web_user.configure(cursor="hand2", text_color=theme.button_color)

        self.location = customtkinter.CTkLabel(self.job_info_frame, text="Location:")
        self.location.grid(row=2, column=0, padx=5, pady=1, stick='e')
        self.location_user = customtkinter.CTkLabel(self.job_info_frame, text='', font=theme.main_font_bold)
        self.location_user.grid(row=2, column=1, padx=5, pady=1, stick='w')

        self.commitment = customtkinter.CTkLabel(self.job_info_frame, text="Commitment:")
        self.commitment.grid(row=3, column=0, padx=5, pady=1, stick='e')
        self.commitment_user = customtkinter.CTkLabel(self.job_info_frame, text='', font=theme.main_font_bold)
        self.commitment_user.grid(row=3, column=1, padx=5, pady=1, stick='w')

        self.work_type = customtkinter.CTkLabel(self.job_info_frame, text="Work Type:")
        self.work_type.grid(row=4, column=0, padx=5, pady=1, stick='e')
        self.work_type_user = customtkinter.CTkLabel(self.job_info_frame, text='', font=theme.main_font_bold)
        self.work_type_user.grid(row=4, column=1, padx=5, pady=1, stick='w')

        self.salary_top = customtkinter.CTkLabel(self.job_info_frame, text="Salary Top:")
        self.salary_top.grid(row=5, column=0, padx=5, pady=1, stick='e')
        self.salary_top_user = customtkinter.CTkLabel(self.job_info_frame, text='', font=theme.main_font_bold)
        self.salary_top_user.grid(row=5, column=1, padx=5, pady=1, stick='w')

        self.salary_bottom = customtkinter.CTkLabel(self.job_info_frame, text="Salary Bottom:")
        self.salary_bottom.grid(row=6, column=0, padx=5, pady=1, stick='e')
        self.salary_bottom_user = customtkinter.CTkLabel(self.job_info_frame, text='', font=theme.main_font_bold)
        self.salary_bottom_user.grid(row=6, column=1, padx=5, pady=1, stick='w')

        self.salary_type = customtkinter.CTkLabel(self.job_info_frame, text="Salary Type:")
        self.salary_type.grid(row=7, column=0, padx=5, pady=1, stick='e')
        self.salary_type_user = customtkinter.CTkLabel(self.job_info_frame, text='', font=theme.main_font_bold)
        self.salary_type_user.grid(row=7, column=1, padx=5, pady=1, stick='w')

        self.resume = customtkinter.CTkLabel(self.job_info_frame, text="Resume Version:")
        self.resume.grid(row=8, column=0, padx=5, pady=(1, 10), stick='e')
        self.resume_user = customtkinter.CTkLabel(self.job_info_frame, text='', font=theme.main_font_bold)
        self.resume_user.grid(row=8, column=1, padx=5, pady=(1, 10), stick='w')

        self.event_contact_frame = customtkinter.CTkFrame(self.jp_frame, fg_color=theme.main_frame)
        self.event_contact_frame.grid(row=1, column=1, stick='nsew', padx=(0, 10), pady=5)

        self.event_contact_tabview = customtkinter.CTkTabview(self.event_contact_frame, text_color=theme.text_color,
                                                              segmented_button_selected_color=theme.accent_color,
                                                              segmented_button_fg_color=theme.main_frame,
                                                              segmented_button_unselected_color=theme.main_frame
                                                              )
        self.event_contact_tabview.grid(row=0, column=0, padx=(20, 10), pady=10, rowspan=2, sticky='nsew')
        self.event_contact_tabview.add("Events")
        self.event_contact_tabview.add('Contacts')

        self.contact_event_button_frame = customtkinter.CTkFrame(self.event_contact_frame)
        self.contact_event_button_frame.grid(row=0, column=1, pady=10, padx=10, sticky='n')
        self.new_contact_button = customtkinter.CTkButton(self.contact_event_button_frame, text="", image=contact_white,
                                                          width=35,
                                                          height=35,
                                                          fg_color=theme.button_color, hover_color='grey15')
        self.new_contact_button.grid(row=1, column=1, pady=(0, 6), padx=6, sticky='n')
        self.new_event_button = customtkinter.CTkButton(self.contact_event_button_frame, text="", image=add_event_white,
                                                        width=35,
                                                        height=35,
                                                        fg_color=theme.button_color, hover_color='grey15')
        self.new_event_button.grid(row=0, column=1, pady=6, padx=6, stick='n')

        self.event_scroll = tkinter.Listbox(self.event_contact_tabview.tab('Events'),
                                            font=theme.main_font,
                                            fg=theme.text_color,
                                            bg=theme.listbox_bg,
                                            selectbackground=theme.accent_color,
                                            selectforeground=theme.text_color,
                                            activestyle='none',
                                            width=40,
                                            height=10,
                                            borderwidth=0)
        self.event_scroll.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        self.contact_listbox = tkinter.Listbox(self.event_contact_tabview.tab('Contacts'),
                                               font=theme.main_font,
                                               fg=theme.text_color,
                                               bg=theme.listbox_bg,
                                               selectbackground=theme.accent_color,
                                               selectforeground=theme.text_color,
                                               activestyle='none',
                                               width=40,
                                               height=10,
                                               borderwidth=0)
        self.contact_listbox.grid(row=0, column=0, padx=10, pady=10)

        # description

        self.job_tabview_frame = customtkinter.CTkFrame(self.jp_frame, fg_color=theme.main_frame)
        self.job_tabview_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=(5, 10), sticky='nsew')
        self.job_tabview_frame.grid_columnconfigure(0, weight=1)

        self.job_tabview = customtkinter.CTkTabview(self.job_tabview_frame, width=500, text_color=theme.text_color,
                                                    segmented_button_selected_color=theme.accent_color,
                                                    segmented_button_fg_color=theme.main_frame,
                                                    segmented_button_unselected_color=theme.main_frame
                                                    )
        self.job_tabview.grid(row=0, column=0, columnspan=2, padx=(10, 0), pady=10, sticky='nsew')
        self.job_tabview.add("Description")
        self.job_tabview.add('Key Words')

        self.job_tabview.grid_columnconfigure(0, weight=1)
        self.job_tabview.grid_rowconfigure(0, weight=1)

        self.job_description_scroll = customtkinter.CTkScrollableFrame(self.job_tabview.tab('Description'),
                                                                       width=700,
                                                                       height=350, fg_color=theme.main_frame)

        self.job_description_scroll.grid(row=0, column=0, padx=10, pady=10)

        self.job_description_label = customtkinter.CTkLabel(self.job_description_scroll, wraplength=687, justify='left')
        self.job_description_label.grid(row=0, column=0)

        self.keyword_scroll = tkinter.Listbox(self.job_tabview.tab('Key Words'), width=101,
                                              font=theme.main_font,
                                              fg=theme.text_color,
                                              bg=theme.listbox_bg,
                                              selectbackground=theme.accent_color,
                                              selectforeground=theme.text_color,
                                              activestyle='none',
                                              borderwidth=0,
                                              height=18)
        self.keyword_scroll.grid(row=0, column=0, padx=10, pady=10)

        # buttons
        self.button_frame = customtkinter.CTkFrame(self.job_tabview_frame)
        self.button_frame.grid(row=0, column=3, sticky="n", pady=10, padx=10)

        self.edit_job_button = customtkinter.CTkButton(self.button_frame, text="", image=writing_white, width=35,
                                                       height=35,
                                                       fg_color=theme.button_color, hover_color='grey15')
        self.edit_job_button.grid(row=0, column=0, pady=6, padx=6)

    def open_link(self, event):
        webbrowser.open(self.company_web_user.cget("text"))
