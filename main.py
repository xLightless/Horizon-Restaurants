from client.interface import Interface
from client.interface.wm_screens import login, menu, admin, payments, reports, reservations
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
        self.banner_frame = ttk.Frame(self.main_frame, style="bannerframe.TFrame", name="bannerframe")
        self.banner_frame.grid_rowconfigure(0, weight=1)
        self.banner_frame.grid_rowconfigure(2, weight=1)
        self.banner_frame.grid_columnconfigure(0, weight=1)
        self.banner_frame.grid_columnconfigure(1, weight=1)
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
        self.style.configure("bannerframe.TFrame", background=BACKGROUND_COLOR)
        self.style.configure("navigation.TFrame", background=BACKGROUND_COLOR)
        self.style.configure("content_frame.TFrame", background=BACKGROUND_COLOR)
        self.lbl_title.label.configure(background=BACKGROUND_COLOR, fg='#FFFFFF')
        self.lbl_branch_id.label.configure(background=BACKGROUND_COLOR, fg='#FFFFFF')
        
        # Display all the frames with tkinter's grid manager
        self.display_frames()
    
    def destroy_frames(self, window: ttk.Frame | tk.Frame | tk.Widget | ttk.Widget):
        if type(window) == list:
            for item in window:
                if item != self.navigation_frame:  # Exclude navigation frame from destruction
                    item.destroy()
        else:
            if window != self.navigation_frame:  # Exclude navigation frame from destruction
                window.destroy()
            
    def forget_frames(self, window:ttk.Frame | tk.Frame | tk.Widget | ttk.Widget):
        # Check if the window is the banner_frame and skip removal
        try:
            if window.winfo_name() == "bannerframe":
                return
        except AttributeError:
            pass

        if type(window) == list:
            for item in window:
                item.grid_forget()
        else:
            window.grid_forget()
        
    def display_frames(self):
        """ Displays the top level frame for any children to be displayed on. """
        
        # Display Banner Frame
        self.banner_frame.grid(row=0, column=0, columnspan=3, padx=self.padx, pady=self.pady, sticky=tk.EW)
        
        # Display Banner Content
        self.lbl_title.label.grid(row=0, column=0, sticky=tk.W)
        self.lbl_branch_id.label.grid(row=1, column=0, sticky=tk.W)
        
        # Display Navigation
        self.navigation_frame.grid(row=0, column=1, columnspan=2, rowspan=2, padx=12, pady=12, sticky=tk.NSEW)
        
        # Display Main Content Frame
        self.content_frame.grid(row=1, column=0, columnspan=3, padx=self.padx, pady=self.pady, sticky=tk.NSEW)
    
    def create_navbar(self, nav_buttons: list, staff_role):
        """Creates a navbar from a list of button names. """
        navbar_buttons = []
        base_navbar = ["Menu", "Logout"]
        if staff_role >= 5:  
            for i in range(len(nav_buttons)):
                button_name = nav_buttons[i].lower()
                button = tk.Button(
                    self.navigation_frame,
                    text=nav_buttons[i],
                    width=100 // len(nav_buttons),
                    name=button_name,
                    padx=self.padx,
                    pady=self.pady
                )
                navbar_buttons.append(button)
                
        if (staff_role <= 4) and (staff_role >= 1):
            for i in range(len(base_navbar)):
                button_name = base_navbar[i].lower()
                button = tk.Button(
                    self.navigation_frame,
                    text=base_navbar[i],
                    width=100 // len(base_navbar),
                    name=button_name,
                    padx=self.padx,
                    pady=self.pady
                )
                navbar_buttons.append(button)
              
                

        # Check if the logout button is in button name and make it a 'danger' color
        # This gives UX a peace of mind.
        if "logout" == nav_buttons[i].lower():
            button.configure(background='#FF5252', activebackground='#FF5252')
        elif "logout" == base_navbar[i].lower():
            button.configure(background='#FF5252', activebackground='#FF5252')

        return navbar_buttons
        
    def del_navbar_button(self, nav_button:str):
        """ Deletes a navigation button from a button set via string type. """
        return
    
    def add_navbar_button(self, nav_button:dict):
        """Add a new or previously existing navigation button via hashmap."""
        return
    
    def display_navbar_buttons(self, nav_buttons:list):
        """ Display the top level frame navigation bar based on the hierarchical priority of the user. """
                
        self.destroy_frames(self.navigation_frame)
        # Get the child of the main frame
        content_frame_name = self.content_frame.winfo_name()
        content_frame_children = self.content_frame.winfo_children()
        
        self.navigation_frame.grid_rowconfigure(0, weight=1)
        self.navigation_frame.grid_columnconfigure(0, weight=1)
        
        # If 0, then frame is empty, resort to default nav.
        # The other option is to get next content frame children as a baseline
        # so we know which navigation items to display.
        # for i in range(len(nav_buttons)):
            
        #         # If empty, create default navbar based on user access.
        #         if len(content_frame_children) == 0:
        #             self.style.configure(nav_buttons[i].winfo_name())
        #             nav_buttons[i].grid(row=0, column=i, sticky=tk.NS+tk.E)
        
        
        # ---------------------------------------------------------------------------------#
        # Remove later. This is a test to see if the navbar displays after updating a frame.
        for i in range(len(nav_buttons)):
            self.style.configure(nav_buttons[i].winfo_name())
            nav_buttons[i].grid(row=0, column=i, sticky=tk.NS+tk.E)
        # ---------------------------------------------------------------------------------#

        
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
        
        # Create the navigation bar button objects based on this list of application level tabs.
        self.nav_btn_list = ["Menu", "Kitchen", "Reports", "Logout"]       
        
        # Main Window
        self.main_window = Main(main_frame)
        
        # Sub Windows
        self.login_interface = login.Login(self.main_window)
        self.menu_interface = menu.Menu(self.main_window)
        
        # Lowest level of staff
        self.staff = login.Staff()
        self.chef = login.Chef()
        self.manager = login.Manager()
        self.admin = login.Admin()
        
        # Create a staff instance
        self.login_staff = login.Staff()
        
        self.display_login()
        # self.display_menu()
        
    def display_login(self):
        """Top most level function to display the login page. """
        
        staff_id = tk.StringVar()
        
        # destroy the previous frames
        self.main_window.destroy_frames(self.main_window.navigation_frame.winfo_children())
        login_buttons = self.login_interface.create_login_buttons_2d_list()
        for row in range(len(login_buttons)):
            for col in range(len(login_buttons[row])):
                if self.login_interface.buttons[row][col].cget('text') != "Login":
                    if self.login_interface.buttons[row][col].cget('text') == "<<":
                        self.login_interface.buttons[row][col].configure(
                            command=lambda: self.login_interface._input_box.on_tbx_delete(self.login_interface._input_box.input_box)
                        )
                    else:
                        self.login_interface.buttons[row][col].configure(
                            command=lambda x=str(self.login_interface.buttons[row][col].cget("text")): self.login_interface._input_box.on_tbx_insert(self.login_interface._input_box.input_box, x)
                        )
                    
                elif self.login_interface.buttons[row][col].cget('text') == "Login":
                    # self.login_interface.buttons[row][col].bind(
                    #     "<Button>", 
                    #     func=lambda _: (
                    #         self.display_menu(),
                    #     )
                        
                    #     if self.login_interface.login_user(staff_id=self.login_interface._input_box.input_box.get()) == True else False
                    # )   
                    
                    self.login_interface.buttons[row][col].configure(
                        command=lambda: (
                            staff_id.set(self.login_interface._input_box.input_box.get()),
                            self.staff.init_user(**staff_id)
                        )
                        if self.login_interface.login_user(staff_id=self.login_interface._input_box.input_box.get()) == True else False
                    )
            
        self.login_interface.display_frames()  
        self.login_interface.display_login_buttons(login_buttons)
        # print("STAFF ROLE: " + self.login_interface.get_staff_role())
    
    def display_menu(self):
        """Top most level function to display the menu page. """

        # Create a new Login instance in the case that the previous has been destroyed, forgotten, or removed by tkinter.
        self.login_interface = login.Login(self.main_window)
        
        # Create and display navbar
        nav_buttons = self.main_window.create_navbar(nav_buttons=self.nav_btn_list, staff_role=self.login_interface.get_staff_role())
        self.main_window.display_navbar_buttons(nav_buttons=nav_buttons)
        
        # Logout button
        nav_buttons[-1].bind("<Button>", func=lambda _: (self.display_login()))

    
    
    
        
    def display_orders(self):
        ## Create Orders object 
        
        ## Display objects frames
        
        ## Display the widgets
        
        ## Update any functionality e.g. widget buttons, treeview, etc etc.
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