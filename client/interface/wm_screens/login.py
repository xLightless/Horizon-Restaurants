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
from client.settings import INITIAL_HEIGHT, INITIAL_WIDTH, NAVBAR_HEIGHT, BACKGROUND_COLOR
from client.errors import InvalidCredentialsError
from authors import show_creators
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk


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
        self.is_logged_in = False
        
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

class Login2(Staff):
    """ Login Interface component for the HRMS System. """
    
    def __init__(self, interface:Interface):
        super().__init__()
        self.is_logged_in = False
        self.i = interface
        
        # Initialise a Login Interface Frame
        self.i_frame = tk.Frame(interface.master, width=INITIAL_WIDTH, height=INITIAL_HEIGHT)
        
        # Create a subframe for the UI
        i_top = tk.Frame(self.i_frame, width=INITIAL_WIDTH, height=NAVBAR_HEIGHT)
        i_top.pack_propagate(False)
        i_top.pack(side=tk.TOP)
        
        # Pack a heading for the subframe
        lbl_restaurants = headings.Heading6(i_top, text="Horizon Restaurants Ltd.")
        lbl_restaurants.label.configure(bg="#1e1e1e", fg='white') # Add dark theme
        lbl_restaurants.label.pack(side="top", fill="both", expand=True)
        
        # Create a new subframe for the UI
        i_bottom = tk.Frame(self.i_frame, width=INITIAL_WIDTH, height=(INITIAL_HEIGHT - NAVBAR_HEIGHT), padx=3, pady=3)
        i_bottom.configure(bg="#1e1e1e")
        i_bottom.pack_propagate(False)
        
        # Enter login pin
        lbl_frame = tk.LabelFrame(i_bottom, text="", width=i_bottom.winfo_reqwidth()/2, height=i_bottom.winfo_reqheight())
        lbl_frame.configure(bg="#1e1e1e", fg='white', padx=3, pady=3)
        
        # Create frame seperation for the PIN Entry
        lbl_frame_top = tk.Frame(lbl_frame, width=lbl_frame.winfo_reqwidth(), height=NAVBAR_HEIGHT)
        lbl_frame_top.configure(bg="#1e1e1e")
        
        lbl_frame_bottom = tk.Frame(lbl_frame, width=lbl_frame.winfo_reqwidth(), height=lbl_frame_top.winfo_reqwidth()-NAVBAR_HEIGHT)
        lbl_frame_bottom.configure(bg="#1e1e1e")
        lbl_frame_bottom.grid_propagate(False)
        lbl_frame_bottom.pack_propagate(False)
        lbl_frame_bottom.propagate(False)
        
        # Disabled Input box for displaying staff id
        lbl_frame_top_heading = headings.TextLabel(lbl_frame_top, text="Enter your Staff ID:")
        lbl_frame_top_heading.label.configure(bg="#1e1e1e", fg='white')
        lbl_frame_top_heading.label.grid(row=0, column=0)
        tbx_input_disabled = inputs.InputBox(lbl_frame_top, label_text="", tbx_width=20, tbx_border_size=0, state='readonly')
        tbx_input_disabled.input_box.configure(fg='red')
        # tbx_input_disabled.set_input_state(state=tk.DISABLED)
        tbx_input_disabled.x += (lbl_frame.winfo_reqwidth()/2) - (tbx_input_disabled.input_box.winfo_reqwidth()/2) - (tbx_input_disabled.input_box_label.winfo_reqwidth()/2)
        # tbx_input_disabled.y += (lbl_frame.winfo_reqheight()/2) - (tbx_input_disabled.input_box.winfo_reqheight()/2)
        tbx_input_disabled.display(grid=[1, 0])
        
        # Input to entry box via Buttons
        input_btn_box = inputs.ButtonBox(
            lbl_frame_bottom, 
            buttons=[
                [1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9], 
                ["Login", 0, "<<"]
                ]
            )
        

        for btn in input_btn_box.btn_list:
            idx = input_btn_box.btn_list.index(btn)
            if (idx != 9) or (idx != 11):
                btn.configure(command = lambda x = str(btn.cget('text')): self.on_tbx_insert(tbx_input_disabled.input_box, x))
            if idx == 11:
                btn.configure(command = lambda: self.on_tbx_delete(tbx_input_disabled.input_box))
            if idx == 9:
                btn.configure(
                    command = lambda x=tbx_input_disabled.input_box: (self.login(x), self.i_frame.forget())
                    if self.get_tbx_length(x)>=STAFF_ID__MIN_LENGTH 
                    else messagebox.showwarning("Authentication Error!", InvalidCredentialsError())
                )
            
        # tbx_input_disabled.input_box.configure(textvariable=disabled_btn_text.set(disabled_btn_text + btn_text))



        i_bottom.pack(side=tk.BOTTOM)
        lbl_frame_top.pack(side=tk.TOP)
        lbl_frame_bottom.pack(side=tk.BOTTOM)
        lbl_frame.pack()
        lbl_frame.pack()
        self.i_frame.pack(fill="both", expand=True)    

    def login(self, staff_id, password:int = None):
        """Attempts to login the user with the requested access method."""
        
        # Check the parameter type
        if isinstance(staff_id, Entry):
            self.staff_id = staff_id.get()
        else:
            self.staff_id = staff_id
            
        # Get the database information about the user
        # db_staff_id = Database().get_record_row(table, staff_id)
        # self.staff_name = db_staff_id['name']
        self.is_logged_in = True
        if self.is_logged_in == True:
            print("Getting database details, logging in...")
            
            # If logged in, display menu.
            self.i.show_nav_menu()
            
        return self.is_logged_in
    
    def require_login_details(self):
        return
    
    def verify_details(self) -> bool:
        return


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
    
from main import Main

class Login(object):
    def __init__(self, parent):
        self.__logged_in = True
        self.parent = parent
        self.staff_role = 6
        
        # Check if the parent is of the main interface.
        if str(type(self.parent)) == "<class '__main__.Main'>":
            self.banner:ttk.Frame = self.parent.frame_banner_1
            self.containers = [
                self.parent.frame_content_1,
                self.parent.frame_content_2,
                self.parent.frame_content_3
            ]
            
        self.containers[1].grid_rowconfigure(0, weight=1)
        self.containers[1].grid_rowconfigure(5, weight=1)
        self.containers[1].grid_columnconfigure(0, weight=1)
        self.containers[1].grid_columnconfigure(5, weight=1)
            
        lbl_frame_title = ["", "Login with Staff ID", ""]
        frame_title = [ttk.Label(self.containers[i], text=lbl_frame_title[i]) for i in range(len(self.containers)) if lbl_frame_title[i] != ""]
        for i in range(len(frame_title)):
            frame_title[i].grid(row=0, column=0, sticky=tk.NSEW)
            
        # buttons= [
        #     [1, 2, 3], [4, 5, 6], [7, 8, 9], ["Login", 0, "<<"]
        # ]
        # for row in range(len(buttons)):
        #     for col in range(len(buttons[row])):
        #         ttk.Button(self.containers[1], )
        
        
        
    def is_logged_in(self):
        # Check that the parent is only from the Main object else ignore it.
        if str(type(self.parent)) == "<class '__main__.Main'>":
            return True if self.__logged_in else False
        return InvalidCredentialsError()
                
    # def display_logout_btn(self):
    #     if self.is_logged_in():
    #         self.parent.lbl_title.label.grid(row=0, column=0, columnspan=2, rowspan=1,sticky=tk.W)
    #         self.parent.lbl_branch_id.label.grid(row=1, column=0, columnspan=2, rowspan=1,sticky=tk.W)
            
    #         # # Create a child frame inside the banner, give it a grid row/col then update.
    #         btn_frame = tk.Frame(self.parent.frame_banner_1, background=BACKGROUND_COLOR)
    #         btn_frame.grid(row=0, column=2, rowspan=2, columnspan=2, sticky=tk.NSEW, padx=16, pady=16)
    #         btn_frame.grid_rowconfigure(0, weight=1)
    #         btn_frame.grid_rowconfigure(2, weight=1)
    #         btn_frame.grid_columnconfigure(0, weight=1)
    #         btn_frame.grid_columnconfigure(2, weight=1)
            
    #         # # Create a button and place it on the child frame.
    #         # btn_logout = tk.Button(btn_frame, text="Logout")
    #         # btn_logout.grid(row=1, column=1, sticky=tk.E)
    #         # btn_frame.configure(bd=1, relief=tk.SOLID)
    #         # btn_logout.configure(bg="#d9534f")
            
    #         # btn_logout = tk.Button(btn_frame, text="Logout")
    #         # btn_logout.grid(row=1, column=0, sticky=tk.E)
            
    #         buttons = []
            
    #         if self.staff_role > 5:
    #             buttons.append(["Reports", "Inventory", "Events"])



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
        