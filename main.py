from client.interface import Interface
from client.interface.wm_screens import login, menu, admin, events, orders, payments, reports, reservations
from client.settings import *
from client.interface.toolkits import headings
from typing import Optional
from functools import partial
from server.sql.database import Database
from tkinter import messagebox

import tkinter as tk
import tkinter.ttk as ttk

app_settings = {
    "title" : TITLE,
    "wm_resizable" : {
        "width": True,
        "height": True
    },
    "bg":'red'
}

class Main(object):
    def __init__(self, main_frame:ttk.Frame, xy_padding:bool = False):
        self.style = ttk.Style()
        
        # Toggle Relative Padding
        match (xy_padding):
            case True:
                self.padx = 3
                self.pady = 3
            case False:
                self.padx = 0
                self.pady = 0
        
        # Main Frame
        self.main_frame = main_frame
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        
        # Banner Frame
        self.banner_frame = ttk.Frame(self.main_frame, style="bannerFrame.TFrame", name="bannerFrame")
        self.banner_frame.grid_rowconfigure(0, weight=1)
        self.banner_frame.grid_rowconfigure(2, weight=1)
        self.banner_frame.grid_columnconfigure(0, weight=1)
        self.banner_frame.grid_columnconfigure(2, weight=1)
        
        # Banner Nav Frame
        self.navigation_frame = ttk.Frame(self.banner_frame, style="navigation.TFrame", name="navigation")
        
        # Frame banner content
        self.lbl_title = headings.Heading6(self.banner_frame, text="Horizon Restaurants")
        self.lbl_branch_id = headings.TextLabel(self.banner_frame, text="Branch ID: 123677")
        
        # Content frame to contain all navigation result elements
        self.content_frame = ttk.Frame(self.main_frame, style="content_frame.TFrame", name="content_frame")
        
        # Fix height of title row
        self.content_frame.grid_rowconfigure(0, weight=0)
        
        # Everything else is expandable
        self.content_frame.grid_rowconfigure(1, weight=1)
        self.content_frame.grid_rowconfigure(2, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=1)
        self.content_frame.grid_columnconfigure(2, weight=1)
        
        # self.style.configure("main_frame.TFrame", background=BACKGROUND_COLOR)
        self.style.configure("bannerFrame.TFrame", background='blue')
        self.style.configure("navigation.TFrame", background='red', border=1, relief=tk.SOLID)
        self.style.configure("content_frame.TFrame", background='yellow')
        self.lbl_title.label.configure(background=BACKGROUND_COLOR, fg='#FFFFFF')
        self.lbl_branch_id.label.configure(background=BACKGROUND_COLOR, fg='#FFFFFF')
        
        # Create the navigation bar button objects
        nav_buttons = ["Home", "Logout"]
        self.nav_buttons = self.create_navbar(nav_buttons=nav_buttons, staff_role=0)
        
        # Display all the frames with tkinter's grid manager
        self.display_frames()
        self.display_navbar() 
        
    def destroy_frames(self, window:ttk.Frame | tk.Frame | tk.Widget | ttk.Widget):
        if type(window) == list:
            for item in window:
                item.destroy()
        else:
            window.destroy()
        
    def display_frames(self):
        """ Displays the top level frame for any children to be displayed on. """
        
        # Display Banner Frame
        self.banner_frame.grid(row=0, column=0, columnspan=3, padx=self.padx, pady=self.pady, sticky=tk.EW)
        
        # Display Banner Content
        self.lbl_title.label.grid(row=0, column=0, sticky=tk.W)
        self.lbl_branch_id.label.grid(row=1, column=0, sticky=tk.W)
        
        # Display Navigation
        self.navigation_frame.grid(row=0, column=1, columnspan=2, rowspan=2, padx=12, pady=12, sticky=tk.NSEW)
        # for i in range(len(self.nav_buttons)):
            
        
        # Display Main Content Frame
        self.content_frame.grid(row=1, column=0, columnspan=3, padx=self.padx, pady=self.pady, sticky=tk.NSEW)
        
    def create_navbar(self, nav_buttons:list, staff_role):
        """Creates a list of navigation button tkinter objects for a pagination structure."""
        
        # Create a navbar
        for i in range(len(nav_buttons)):
            button = ttk.Button(self.navigation_frame, text=nav_buttons[i])
            nav_buttons[nav_buttons.index(nav_buttons[i])] = button
        return nav_buttons
        
    def del_navbar_button(self, nav_button:str):
        """ Deletes a navigation button from a button set via string type. """
        return
    
    def add_navbar_button(self, nav_button:dict):
        """Add a new or previously existing nagivation button via hashmap."""
        return
    
    def display_navbar(self):
        """ Display the top level frame navigation bar based on the hierarchical priority of the user. """
        
                
        # Get the child of the main frame
        content_frame_name = self.content_frame.winfo_name()
        content_frame_children = self.content_frame.winfo_children()
        # print(content_frame_name, content_frame_children)
        
        # if content_frame_name != content_frame_children[frame_number].winfo_name() or btn.cget('text') # name of navbar button:
            # do something
        
        # Check the page we are on to display the right nav buttons
        
    def get_current_frames(self):
        """Gets all the current active frames of a paginated section. """
        
        return self.content_frame.winfo_children()

    
class Application(object):
    def __init__(self, **args):
        
        # Configure the master interface
        self.main = Interface(**args)
        self.main.master.propagate(False)
        self.main.master.configure(width=INITIAL_WIDTH, height=INITIAL_HEIGHT, bg=BACKGROUND_COLOR)
        self.main.master.minsize(width=INITIAL_WIDTH, height=INITIAL_HEIGHT)
        
        # Allow the application to become expandable on the top level.
        self.main.master.grid_rowconfigure(0, weight=1)
        self.main.master.grid_columnconfigure(0, weight=1)
        
        # Add styling
        self.style = ttk.Style()
        
        # Add a main frame to master
        main_frame = ttk.Frame(self.main.master, style='main_frame.TFrame', name="main_frame", width=self.main.master.winfo_reqwidth(), height=self.main.master.winfo_reqheight())
        main_frame.grid(row=0, column=0, sticky=tk.NSEW)        
        
        # Construct any windows/interfaces below
        self.main_window = Main(main_frame)
        self.login_interface = login.Login(self.main_window)
        self.menu_interface = menu.Menu(self.main_window)
        # self.orders_interface = orders.Order(self.main_window)
        # self.payment_interface = payments.Payment(self.main_window)
        
        self.display_login()
        
    def display_login(self):
        """Top most level function to display the login page. """
        
        login_buttons = self.login_interface.create_login_buttons_2d_list()
        for row in range(len(login_buttons)):
            for col in range(len(login_buttons[row])):
                if self.login_interface.buttons[row][col].cget('text') != "Login":
                    if self.login_interface.buttons[row][col].cget('text') == "<<":
                        self.login_interface.buttons[row][col].configure(command=lambda: self.login_interface.input_box.on_tbx_delete(self.login_interface.input_box.input_box))
                    else:
                        self.login_interface.buttons[row][col].configure(command=lambda x=str(self.login_interface.buttons[row][col].cget("text")): self.login_interface.input_box.on_tbx_insert(self.login_interface.input_box.input_box, x))
                    
                elif self.login_interface.buttons[row][col].cget('text') == "Login":
                    self.login_interface.buttons[row][col].bind("<Button>", func=lambda _: (
                        # self.main_window.destroy_window(self.main_window.content_frame.winfo_children()),
                        self.display_menu()
                        
                        ) if self.login_interface.login_user(staff_id=self.login_interface.input_box.input_box.get()) == True else "")   
            
            
        self.login_interface.display_login_buttons(login_buttons)
        self.login_interface.display_frames()

    def display_menu(self):
        """Top most level function to display the menu page. """
        nav_buttons = self.main_window.create_navbar(nav_buttons=["Home", "Logout"], staff_role=self.login_interface.staff_role)
        self.menu_interface.display()
        
        
        # self.menu_interface.btn_dict.get("KEY").bind("<Button>", func=lambda _: ((cmd1), (cmd2), if x == y else ""))
        pass
        
    def display_orders(self):
        # self.orders_interface.btn_dict.get("KEY").bind("<Button>", func=lambda _: ((cmd1), (cmd2), if x == y else ""))
        return
    
    def display_payments(self):
        # self.payments_interface.btn_dict.get("KEY").bind("<Button>", func=lambda _: ((cmd1), (cmd2), if x == y else ""))
        return
    
    def display_kitchen(self):
        # self.kitchen_interface.btn_dict.get("KEY").bind("<Button>", func=lambda _: ((cmd1), (cmd2), if x == y else ""))
        return
    
    def display_reports(self):
        # self.reports_interface.btn_dict.get("KEY").bind("<Button>", func=lambda _: ((cmd1), (cmd2), if x == y else ""))
        return


if __name__ == '__main__':
    
    # Initialise the entire application and mapped settings
    app = Application(**app_settings)
    
    # Add any new settings after initialisation like below:
    # main_window.settings['SETTING_NAME'] = SETTING_VALUE
    
    # Run the tkinter event loop to control continuity
    app.main.master.mainloop()