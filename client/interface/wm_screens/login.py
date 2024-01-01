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
        self.staff_role = 0
        
        if str(type(self.parent)) == "<class '__main__.Main'>":
            self.main_frame = tk.Frame(self.parent.frame_content_2)
            self.banner:ttk.Frame = self.parent.frame_banner_1
            self.parent.style.configure("self.main_frame.TFrame", background=BACKGROUND_COLOR, bd=1, relief=tk.SOLID)
            self.parent.style.configure("title_frame.TFrame", background=BACKGROUND_COLOR)
            
            self.btn_dict = {}
            
    def display(self):
        login_buttons = self.get_login_buttons()
        self.enable_login_buttons(login_buttons)
            
    def get_login_buttons(self) -> dict:
        """Get a dictionary of the login interface staff id buttons. """
        
        button_dict = {}
        
        # Check if the parent is of the main interface.
        if str(type(self.parent)) == "<class '__main__.Main'>":
            self.buttons=[
                [1, 2, 3], [4, 5, 6], [7, 8, 9], ["Login", 0, "<<"]
            ]
            
            self.main_frame.grid(sticky=tk.NSEW)
            self.main_frame.grid_rowconfigure(0, weight=0)
            self.main_frame.grid_rowconfigure(1, weight=1)
            self.main_frame.grid_rowconfigure(2, weight=1)
            self.main_frame.grid_columnconfigure(0, weight=1)
            
            # Title frame for login        
            title_frame = ttk.Frame(self.main_frame, style="title_frame.TFrame", border=3, relief=tk.SOLID)
            title_frame.grid(row=0, column=0, sticky=tk.NSEW)
            title_frame.grid_columnconfigure(0, weight=1)
            title_frame.grid_columnconfigure(1, weight=1)
            title_frame.grid_columnconfigure(2, weight=1)
            
            # Title
            title = headings.Heading6(title_frame, text="POS Management System")
            title.label.grid(row=0, column=1, sticky=tk.NSEW)
            title.label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")
            
            # Error frame for login
            input_frame = tk.Frame(self.main_frame) # style="input_frame.TFrame"
            input_frame.grid(row=1, column=0, sticky=tk.NSEW)
            input_frame.grid_rowconfigure(0, weight=1)
            input_frame.grid_rowconfigure(1, weight=1)
            input_frame.grid_columnconfigure(0, weight=1)
            input_frame.grid_columnconfigure(1, weight=1)
            input_frame.configure(background='#191919')

            # Read only input box
            input_box = inputs.InputBox(input_frame, label_text="Staff ID: ", state='readonly')
            input_box.get_frame().grid(row=0, column=0, columnspan=2, rowspan=2)
            input_box.get_frame().configure(background='#191919')
            input_box.input_box_label.configure(background='#191919', fg='#FFFFFF')
            
            self.input_box = input_box
            
            # Content frame for login
            content_frame = tk.Frame(self.main_frame) # style="content_frame.TFrame"
            content_frame.grid(row=2, column=0, sticky=tk.NSEW)
            content_frame.configure(background='#191919', padx=32, pady=32)
            
            # Staff Login Numberpad buttons
            for row in range(len(self.buttons)):
                for col in range(len(self.buttons[row])):
                    
                    # Configure the grid to expand each row/col to the correct size throughout.
                    content_frame.grid_rowconfigure(row, weight=1)
                    content_frame.grid_columnconfigure(col, weight=1)
                    
                    # Create a button for each grid position
                    btn = ttk.Button(content_frame, style=f"{row}_{col}.TButton", text=self.buttons[row][col], command=None)
                    self.parent.style.configure(f"{row}_{col}.TButton", background=BACKGROUND_COLOR)
                    button_dict[self.buttons[row][col]] = btn

            self.parent.style.configure("title_frame.TFrame", background=BACKGROUND_COLOR)
            return button_dict
                            
    def enable_login_buttons(self, login_buttons):
        """Enable the login interface staff id buttons. """
        
        for row in range(len(self.buttons)):
            for col in range(len(self.buttons[row])):
                login_buttons[self.buttons[row][col]].grid(row=row, column=col, sticky=tk.NSEW)

                # Configure the buttons command callbacks.
                if self.buttons[row][col] != "Login":
                    if self.buttons[row][col] == "<<":
                        login_buttons[self.buttons[row][col]].configure(command=lambda: self.input_box.on_tbx_delete(self.input_box.input_box))
                    # elif self.buttons[row][col] == "Login":
                    #     login_buttons[self.buttons[row][col]].bind(
                    #         "<Button>", func=lambda _: (self.parent.display_navbar(self.staff_role, True) if self.login_user(self.input_box.input_box.get()) == True else "")
                    #     )
                    else:
                        login_buttons[self.buttons[row][col]].configure(command=lambda x=str(login_buttons[self.buttons[row][col]].cget("text")): self.input_box.on_tbx_insert(self.input_box.input_box, x))
                
                self.btn_dict[self.buttons[row][col]] = login_buttons[self.buttons[row][col]]
                
    def is_logged_in(self):
        print("staff role: ", self.staff_role)
        return True if self.staff_role else False
                    
    def _login(self, staff_id):
        """Internal function. """       
        try:
            # Raise value error if parsed staff id is not an integer
            int(staff_id)
        except ValueError:
            messagebox.showerror("Invalid Credentials Error!", InvalidCredentialsError())
            return False
        
        # Get information about the user
        try:
            record = database.get_table_records_of_key("staff", "account_number", staff_id, True)
            record = record.to_dict('records')[0]
            
            # If staff_id found, create an instance of the staff id user
            staff = Staff()
            self.staff_role = record['branch_role']
            staff.staff_id = record['account_number']
            staff.staff_name = "%s %s" % (record['staff_first_name'], record['staff_last_name'])
            
            # If no errors and presuming credentials are accepted then login.
            print(f"Welcome, {staff.staff_name}! You've logged in at: {datetime.datetime.utcnow()}.")
            return True
        except IndexError:
            messagebox.showerror("Invalid Credentials Error!", InvalidCredentialsError())
            return False
        
    def login_user(self, staff_id):
        """Logs the user into the system if credentials are correct. """
        
        if self._login(staff_id):
            # Destroy the login frame if user is found.
            # self.parent.destroy_window_children(self.parent.frame_content_2.winfo_children())
            self.main_frame.destroy()
            self.parent._update_main()
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
        