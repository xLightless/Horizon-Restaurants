# --------------------------------------------------------------------------------------- #
# 
#   This is the LOGIN page window manager screen module.
#   Any functions related to this particular interface should
#   specifically be programmed in this environment.
# 
# --------------------------------------------------------------------------------------- #

from client.interface.toolkits.typography.font import *
from client.interface.toolkits import inputs, headings
from client.interface.wm_screens.inventory import Inventory
from client.settings import INITIAL_HEIGHT, INITIAL_WIDTH, NAVBAR_HEIGHT, BACKGROUND_COLOR, MAIN_GRID_BOXES
from client.errors import InvalidCredentialsError
from server.sql.database import database
from tkinter import messagebox

import tkinter as tk
import tkinter.ttk as ttk
import datetime


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
    
    def set_staff_role(self):
        return
    
    def _logout(self):
        return True if len(self.staff_id)==6 else False
    
    def __get_customer(self, customer_id:int):
        """Potentially a redundant function due to the impracticalness of customer in UML. """
        return

    def get_checked_inventory(self, inventory: Inventory) -> dict:
        return
    
    def request_login_information(self) -> tuple:
        return (self.staff_id, self.staff_name)

class Login(object):  
    def __init__(self, parent):
        self.parent = parent
        self.__staff_role = 1
        
        if str(type(self.parent)) == "<class '__main__.Main'>":
            self.style:ttk.Style = self.parent.style
            self.style.configure("title_frame.TFrame", background=BACKGROUND_COLOR)
            
            # Login Buttons for entering STAFF ID
            self.buttons=[
                [1, 2, 3], [4, 5, 6], [7, 8, 9], ["Login", 0, "<<"]
            ]
            
            self.title_frame = ttk.Frame(self.parent.content_frame, style="title_frame.TFrame", border=3, relief=tk.SOLID, name="title_frame_login")
            self.input_frame = tk.Frame(self.parent.content_frame, name="input_frame_login")
            self.numberpad_frame = tk.Frame(self.parent.content_frame, name="numberpad_frame_login")
            self.input_box = inputs.InputBox(self.input_frame, label_text="Staff ID: ", state='readonly')
          
    def display_frames(self):
        """Display the login frame on the top level frame."""
          
        # Check if the parent is of the main interface.
        if str(type(self.parent)) == "<class '__main__.Main'>":
            
            button_object_dict = {}

            # Title frame for login        
            self.parent.style.configure("title_frame.TFrame", background=BACKGROUND_COLOR)
            self.title_frame.grid_columnconfigure(0, weight=1)
            self.title_frame.grid_columnconfigure(1, weight=1)
            self.title_frame.grid_columnconfigure(2, weight=1)
            
            # Title
            title = headings.Heading6(self.title_frame, text="POS Management System")
            title.label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")
            
            # STAFF ID Login Frame
            self.input_frame.grid_rowconfigure(0, weight=1)
            self.input_frame.grid_rowconfigure(1, weight=1)
            self.input_frame.grid_columnconfigure(0, weight=1)
            self.input_frame.grid_columnconfigure(1, weight=1)
            self.input_frame.configure(background='#191919')

            # STAFF ID read only input box
            self.input_box.get_frame().configure(background='#191919')
            self.input_box.input_box_label.configure(background='#191919', fg='#FFFFFF')
            
            # Login Frame
            self.numberpad_frame.configure(background='#191919', padx=32, pady=32)
                    
            # Get the list of frames to configure/display
            self.title_frame.grid(row=0, column=1, sticky=tk.NSEW)
            title.label.grid(row=0, column=1, sticky=tk.NSEW)
            self.input_frame.grid(row=1, column=1, sticky=tk.NSEW)
            self.numberpad_frame.grid(row=2, column=1, sticky=tk.NSEW)
            self.input_box.get_frame().grid(row=0, column=0, columnspan=2, rowspan=2)
            
    def display_login_buttons(self, login_buttons):
        for row in range(len(login_buttons)):
            for col in range(len(login_buttons[row])):
                login_buttons[row][col].grid(row=row, column=col, sticky=tk.NSEW)
        
    def create_login_buttons_2d_list(self):
        """Create a 2D array of button objects"""   
        # Staff Login Numberpad buttons
        for row in range(len(self.buttons)):
            for col in range(len(self.buttons[row])):
                
                # Configure the grid to expand each row/col to the correct size throughout.
                self.numberpad_frame.grid_rowconfigure(row, weight=1)
                self.numberpad_frame.grid_columnconfigure(col, weight=1)
                
                # Create a button for each grid position
                btn = ttk.Button(self.numberpad_frame, style=f"login_button_{row}_{col}.TButton", text=self.buttons[row][col], command=None)
                self.parent.style.configure(f"login_button_{row}_{col}.TButton", background=BACKGROUND_COLOR)
                
                # Update self.buttons to match the object
                self.buttons[row][col] = btn 
                    
        return self.buttons
                
    def is_logged_in(self):
        print("staff role: ", self.__staff_role)
        return True if self.__staff_role else False
    
    def get_staff_role(self):
        return self.__staff_role
    
    def set_staff_role(self, staff_role):
        self.__staff_role = staff_role
        return self.__staff_role
                    
    def _login(self, staff_id):
        """Internal function. """       
        try:
            # Raise value error if parsed staff id is not an integer
            int(staff_id)
        except ValueError:
            messagebox.showerror("Invalid Credentials Error!", InvalidCredentialsError())
            return False
        
        try:
            # Get information about the user
            record = database.get_table_records_of_key("staff", "account_number", staff_id, True)
            record = record.to_dict('records')[0]
            
            # If staff_id found, create an instance of the staff id user
            staff = Staff()
            self.__staff_role = record['branch_role']
            staff.staff_id = record['account_number']
            staff.staff_name = "%s %s" % (record['staff_first_name'], record['staff_last_name'])
            
            # If no errors and presuming credentials are accepted then login.
            print(f"Welcome, {staff.staff_name}! You've logged in at: {datetime.datetime.utcnow()}.")
            return True
        except IndexError:
            messagebox.showerror("Invalid Credentials Error!", InvalidCredentialsError())
            return False
        
    def login_user(self, staff_id):
        """Logs the user into the system if their credentials are correct. """
        
        if self._login(staff_id):
            
            # Suboptimal solution for checking if a object exists
            # if 'login' in str(active_frames[0]).find('login')
            
            # Destroy the login frame if user is found.
            active_frames = self.parent.get_current_frames()
            self.parent.forget_frames(active_frames)
            return True
        
    def logout_user(self):
        """Logs the user out of the system. """
        print("Logging out of the system...")
        exit()

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
        