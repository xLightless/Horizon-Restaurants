# --------------------------------------------------------------------------------------- #
# 
#   This is the LOGIN page window manager screen module.
#   Any functions related to this particular interface should
#   specifically be programmed in this environment.
# 
# --------------------------------------------------------------------------------------- #

from client.interface.toolkits.typography.font import *
from client.interface.toolkits import inputs, headings
# from client.interface.wm_screens.inventory import Inventory
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

class Login(object):  
    def __init__(self, parent):
        self._parent = parent
        self._branch_role = 1
        
        if str(type(self._parent)) == "<class '__main__.Main'>":
            self.style:ttk.Style = self._parent.style
            self.style.configure("title_frame.TFrame", background=BACKGROUND_COLOR)
            
            # Login Buttons for entering STAFF ID
            self.buttons=[
                [1, 2, 3], [4, 5, 6], [7, 8, 9], ["Login", 0, "<<"]
            ]
            
            self._title_frame = ttk.Frame(self._parent.content_frame, style="title_frame.TFrame", border=3, relief=tk.SOLID, name="title_frame_login")
            self._input_frame = tk.Frame(self._parent.content_frame, name="input_frame_login")
            self._numberpad_frame = tk.Frame(self._parent.content_frame, name="numberpad_frame_login")
            self._input_box = inputs.InputBox(self._input_frame, label_text="Staff ID: ", state='readonly')
          
    def display_frames(self):
        """Display the login frame on the top level frame."""
          
        # Check if the parent is of the main interface.
        if str(type(self._parent)) == "<class '__main__.Main'>":
            
            button_object_dict = {}

            # Title frame for login        
            self.style.configure("title_frame.TFrame", background=BACKGROUND_COLOR)
            self._title_frame.grid_columnconfigure(0, weight=1)
            self._title_frame.grid_columnconfigure(1, weight=1)
            self._title_frame.grid_columnconfigure(2, weight=1)
            
            # Title
            title = headings.Heading6(self._title_frame, text="POS Management System")
            title.label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")
            
            # STAFF ID Login Frame
            self._input_frame.grid_rowconfigure(0, weight=1)
            self._input_frame.grid_rowconfigure(1, weight=1)
            self._input_frame.grid_columnconfigure(0, weight=1)
            self._input_frame.grid_columnconfigure(1, weight=1)
            self._input_frame.configure(background='#191919')

            # STAFF ID read only input box
            self._input_box.get_frame().configure(background='#191919')
            self._input_box.input_box_label.configure(background='#191919', fg='#FFFFFF')
            
            # Login Frame
            self._numberpad_frame.configure(background='#191919', padx=32, pady=32)
                    
            # Get the list of frames to configure/display
            self._title_frame.grid(row=0, column=1, sticky=tk.NSEW)
            title.label.grid(row=0, column=1, sticky=tk.NSEW)
            self._input_frame.grid(row=1, column=1, sticky=tk.NSEW)
            self._numberpad_frame.grid(row=2, column=1, sticky=tk.NSEW)
            self._input_box.get_frame().grid(row=0, column=0, columnspan=2, rowspan=2)
            
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
                self._numberpad_frame.grid_rowconfigure(row, weight=1)
                self._numberpad_frame.grid_columnconfigure(col, weight=1)
                
                # Create a button for each grid position
                btn = ttk.Button(self._numberpad_frame, style=f"login_button_{row}_{col}.TButton", text=self.buttons[row][col], command=None)
                self._parent.style.configure(f"login_button_{row}_{col}.TButton", background=BACKGROUND_COLOR)
                
                # Update self.buttons to match the object
                self.buttons[row][col] = btn 
                    
        return self.buttons
    
    def get_branch_role(self):
        return self._branch_role
        
    def _login_user(self, staff_id):
        """Internal function. """       
        try:
            # Raise value error if parsed staff id is not an integer
            int(staff_id)
        except ValueError:
            messagebox.showerror("Invalid Credentials Error!", InvalidCredentialsError())
            return False
        
        try:
            # Get information about the user
            record = database.get_table_records_of_key("staff", "staff_id_number", staff_id, True)
            record = record.to_dict('records')[0]
            
            # If staff_id found, create an instance of the staff id user
            staff = Staff()
            self._branch_role = record['branch_role']
            staff.staff_id = record['staff_id_number']
            staff_name = "%s %s" % (record['first_name'], record['last_name'])
            
            # If no errors and presuming credentials are accepted then login.
            print(f"Welcome, {staff_name}! You've logged in at: {datetime.datetime.utcnow()}.")
            return True
        except IndexError:
            messagebox.showerror("Invalid Credentials Error!", InvalidCredentialsError())
            return False
        
    def login(self, staff_id) -> bool:
        """Logs the user into the system if their credentials are correct. """
        if self._login_user(staff_id):
            
            # Destroy the login frame if user is found.
            active_frames = self._parent.get_current_frames()
            self._parent.forget_frames(active_frames)
            return True
        
class Staff(object):
    def __init__(self):
        self.staff_id = tk.IntVar()
        
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.branch_role = tk.IntVar()
        self.branch_id = tk.IntVar()
        
    def init_staff(self, staff_id):
        """Set staff record variables to the database information from staff table."""
    
        # Get information about the user
        record = database.get_table_records_of_key("staff", "staff_id_number", staff_id, True)
        record = record.to_dict('records')[0]
        
        # Set object instance variables to record values
        self.staff_id.set(record['staff_id_number'])
        self.first_name.set(record['first_name'])
        self.last_name.set(record['last_name'])
        self.branch_id.set(record['branch_id'])
        self.branch_role.set(record['branch_role'])
        

    def accept_order(self):
        return

    def _logout(self):
        return True if len(self.staff_id)==6 else False
    
    def __get_customer(self, customer_id:int):
        """Potentially a redundant function due to the impracticalness of customer in UML. """
        return

    # def get_checked_inventory(self, inventory: Inventory) -> dict:
    #     return
    
    def request_login_information(self) -> tuple:
        return (self.staff_id, self.first_name)
    

class Chef(Staff):
    def __init__(self):
        """Chef Staff Object. Inherits functionality from Staff. """
        super().__init__()
        
        self._chef_id = self.staff_id
        self._chef_name = self.first_name
    
    
class Manager(Chef):
    def __init__(self):
        """Manager Staff Object. Inherits functionality from Chef. """

        super().__init__()
        self._manager_id = self.staff_id
        self._manager_name = self.first_name
        
        
class Admin(Manager):
    def __init__(self):
        """Admin Staff Object. Inherits functionality from Manager. """
        
        super().__init__()
        self.admin_id = self.staff_id
        self.admin_name = self.first_name
        
    def create_user(self, first_name, last_name, staff_id_number, staff_id_password, phone, email, branch_role, branch_id):
        return
    
    def update_user(self, staff_id_number:int, **args):
        return
    
    def get_users(self, df=False):
        record = database.get_table("staff", df)
        return record
    
    
    
    
    
    