# --------------------------------------------------------------------------------------- #
# 
#   This is the LOGIN page window manager screen module.
#   Any functions related to this particular interface should
#   specifically be programmed in this environment.
# 
# --------------------------------------------------------------------------------------- #

from client.interface import Interface
from client.interface.authentication import AuthenticateUser
from client.interface.toolkits.typography.font import *
from client.interface.toolkits import inputs, headings
from client.interface.wm_screens.inventory import Inventory
from client.settings import INITIAL_HEIGHT, INITIAL_WIDTH, NAVBAR_HEIGHT, BACKGROUND_COLOR, MAIN_GRID_BOXES
from client.errors import InvalidCredentialsError
from server.sql.database import database

import tkinter as tk
import tkinter.ttk as ttk
import sys
import datetime
import pandas as pd


# Login Interface options
widget_options = {
    "bd" : 1,
    "relief" : tk.SOLID,
    # "padx" : 5,
    # "pady" : 5
}

# Login parameter constants
STAFF_ID__MIN_LENGTH = 6

class Staff(object):
    def __init__(self):
        self.staff_id:str = f"{0}"
        self.staff_name:str = ""
        
    def accept_order(self):
        return
    
    def _logout(self):
        return True if len(self.staff_id)==6 else False
    
    def __get_customer(self, customer_id:int):
        """Potentially a redundant function due to the impracticalness of customer in UML. """
        return
    
    def _logout_to_wm_screen(self, screen):
        """ Logs out the Staff member if already logged in."""
        
        result = self._logout()
        if result == True:
            for widget in screen.master.winfo_children():
                # widget.destroy()
                print(widget)
                
            return screen

    def get_checked_inventory(self, inventory: Inventory) -> dict:
        return
    
    def request_login_information(self) -> tuple:
        return (self.staff_id, self.staff_name)

class Login(object):
    __logged_in = False   
    def __init__(self, parent):
        # self.__logged_in = False
        self.parent = parent
        self.staff_role = 6
            
    def display(self):
        """Display the Login Interface. """
        
        # Check if the parent is of the main interface.
        if str(type(self.parent)) == "<class '__main__.Main'>":
            self.parent.style.configure("main_frame.TFrame", background=BACKGROUND_COLOR, bd=1, relief=tk.SOLID)
            self.banner:ttk.Frame = self.parent.frame_banner_1
            container_titles = ["", "Login with Staff ID", ""]
            self.buttons=[
                [1, 2, 3], [4, 5, 6], [7, 8, 9], ["Login", 0, "<<"]
            ]
            
            # self.parent.style.configure("frame_content_1.TFrame")
            
            main_frame = tk.Frame(self.parent.frame_content_2)
            main_frame.grid(sticky=tk.NSEW)
            main_frame.grid_rowconfigure(0, weight=0)
            main_frame.grid_rowconfigure(1, weight=1)
            main_frame.grid_rowconfigure(2, weight=1)
            main_frame.grid_columnconfigure(0, weight=1)
            
            self.main_frame = main_frame
            
            # Title frame for login        
            title_frame = ttk.Frame(main_frame, style="title_frame.TFrame", border=3, relief=tk.SOLID)
            title_frame.grid(row=0, column=0, sticky=tk.NSEW)
            title_frame.grid_columnconfigure(0, weight=1)
            title_frame.grid_columnconfigure(1, weight=1)
            title_frame.grid_columnconfigure(2, weight=1)
            
            # Title
            title = headings.Heading6(title_frame, text="POS Management System")
            title.label.grid(row=0, column=1, sticky=tk.NSEW)
            title.label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")
            
            # Error frame for login
            input_frame = tk.Frame(main_frame) # style="input_frame.TFrame"
            input_frame.grid(row=1, column=0, sticky=tk.NSEW)
            input_frame.grid_rowconfigure(0, weight=1)
            input_frame.grid_rowconfigure(1, weight=1)
            # input_frame.grid_rowconfigure(2, weight=1)
            
            input_frame.grid_columnconfigure(0, weight=1)
            input_frame.grid_columnconfigure(1, weight=1)
            input_frame.configure(background='#191919')

            # Read only input box
            input_box = inputs.InputBox(input_frame, label_text="Staff ID: ")
            input_box.get_frame().grid(row=0, column=0, columnspan=2, rowspan=2)
            input_box.get_frame().configure(background='#191919')
            input_box.input_box_label.configure(background='#191919', fg='#FFFFFF')
            
            self.input_box = input_box
            
            # Content frame for login
            content_frame = tk.Frame(main_frame) # style="content_frame.TFrame"
            content_frame.grid(row=2, column=0, sticky=tk.NSEW)
            content_frame.configure(background='#191919', padx=32, pady=32)
            
            # Number pad
            # number_pad = [ttk.Button(content_frame, style=f"{row}_{col}.TButton") for row in range(len(self.buttons)) for col in range(len(self.buttons[row]))]
            for row in range(len(self.buttons)):
                for col in range(len(self.buttons[row])):
                    
                    # Configure the grid to expand each row/col to the correct size throughout.
                    content_frame.grid_rowconfigure(row, weight=1)
                    content_frame.grid_columnconfigure(col, weight=1)
                    
                    # Create a button for each grid position
                    btn = ttk.Button(content_frame, style=f"{row}_{col}.TButton", text=self.buttons[row][col], command=None)
                    btn.grid(row=row, column=col, sticky=tk.NSEW)
                    self.parent.style.configure(f"{row}_{col}.TButton", background=BACKGROUND_COLOR)
                    
                    # btn_dict[self.buttons[row][col]] = btn
                    
            self.parent.style.configure("title_frame.TFrame", background=BACKGROUND_COLOR)

    def is_logged_in(self):
        # Check that the parent is only from the Main object else ignore it.
        if str(type(self.parent)) == "<class '__main__.Main'>":
            return True if self.__logged_in else False
        return InvalidCredentialsError()
    
    def login(self, staff_id):        
        try:
            int(staff_id)
        except ValueError:
            return print(InvalidCredentialsError())
        
        # Get information about the user
        try:
            record = database.get_table_records_of_key("staff", "account_number", staff_id, True)
            record = record.to_dict('records')[0]
            
            # If found, create an instance of the staff id user
            staff = Staff()
            self.staff_role = record['branch_role']
            staff.staff_id = record['account_number']
            staff.staff_name = f"{record['staff_first_name']}{record['staff_last_name']}"
            
            print(f"Welcome, {staff.staff_name}! You've logged in at: {datetime.datetime.utcnow()}.")
        except IndexError:
            return print(InvalidCredentialsError())
        
        # If no errors and presuming credentials are accepted. Login.
        # Also, destroy any login interface children.
        # self.parent.display_navbar(self.staff_role)
        # self.__class__.__logged_in = True
        # self.parent.destroy_window_children(self.parent.containers[1])
        # self.parent.display_navbar(self.staff_role)
        # # self.parent.__init__(self.parent.)
        # # return self.is_logged_in()
        
    
    def on_tbx_insert(self, tbx_input, args):
        tbx_input.configure(state="normal")
        tbx_input.insert(tk.END, args)
        tbx_input.configure(state="readonly")
        
    def on_tbx_delete(self, tbx_input):
        tbx_input.configure(state="normal")
        tbx_input.delete(0, tk.END)
        tbx_input.configure(state="readonly")
        
    def get_tbx_length(self, tbx_input):
        return len(tbx_input.get())

class Chef(Staff):
    def __init__(self):
        self._chef_id = self.staff_id
        self._chef_name = self.staff_name
    
class Manager(Chef):
    def __init__(self):
        self.manager_id = self.staff_id
        self.manager_name = self.staff_name
        
class Admin(Manager):
    def __init__(self):
        self.admin_id = self.staff_id
        self.admin_name = self.staff_name
        
    def create_user(self, staff_type:str, account_password:str, account_email:str, staff_account_id:int):
        return
    
    def update_user(self, staff_account_number:int, **args):
        return
    
    def view_users(self):
        return
        