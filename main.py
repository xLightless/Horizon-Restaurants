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
    navbar_buttons = dict
    def __init__(self, parent):
        self.style = ttk.Style()
        self.stringVar = tk.StringVar()
        
        # self.login_interface = login.Login(parent)
        # self.home_interface = home.Home(parent)
        
        self.btn_dict = {}

        # Banner frame and widgets
        self.frame_banner_1 = ttk.Frame(parent, style="bannerFrame.TFrame")
        self.frame_banner_1.grid(row=0, column=0, sticky=tk.EW, columnspan=3, padx=3, pady=3)
        self.frame_banner_1.grid_rowconfigure(0, weight=1)
        self.frame_banner_1.grid_rowconfigure(2, weight=1)
        self.frame_banner_1.grid_columnconfigure(0, weight=1)
        self.frame_banner_1.grid_columnconfigure(2, weight=1)

        # Some spacing/other options
        self.frame_content_1 = ttk.Frame(parent, style="frame_content_1.TFrame", width=100 // MAIN_GRID_BOXES)
        self.frame_content_1.grid(row=1, column=0, sticky=tk.NSEW, padx=3, pady=3)
        self.frame_content_1.grid_rowconfigure(0, weight=1)
        self.frame_content_1.grid_columnconfigure(0, weight=1)
        
        # Number pad
        self.frame_content_2 = ttk.Frame(parent, style="frame_content_2.TFrame", width=100 // MAIN_GRID_BOXES)
        self.frame_content_2.grid(row=1, column=1, sticky=tk.NSEW, padx=3, pady=3)
        self.frame_content_2.grid_rowconfigure(0, weight=1)
        self.frame_content_2.grid_columnconfigure(0, weight=1)

        # Some spacing/other options
        self.frame_content_3 = ttk.Frame(parent, style="frame_content_3.TFrame", width=100 // MAIN_GRID_BOXES)
        self.frame_content_3.grid(row=1, column=2, sticky=tk.NSEW, padx=3, pady=3)
        self.frame_content_3.grid_rowconfigure(0, weight=1)
        self.frame_content_3.grid_columnconfigure(0, weight=1)
        
        self.containers = [self.frame_content_1, self.frame_content_2, self.frame_content_3]

        # Frame banner content
        self.lbl_title = headings.Heading6(self.frame_banner_1, text="Horizon Restaurants")
        self.lbl_title.label.grid(row=0, column=0, sticky=tk.W)
        self.lbl_branch_id = headings.TextLabel(self.frame_banner_1, text="Branch ID: 123677")
        self.lbl_branch_id.label.grid(row=1, column=0, sticky=tk.W)

        # Configure columns and rows to expand horizontally and vertically
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_columnconfigure(2, weight=1)
        
        # Update vertical expansion due to row 0 elements not requiring it.
        # Make the next row expandable.
        parent.grid_rowconfigure(0, weight=0)
        parent.grid_rowconfigure(1, weight=1)

        # Style all elements
        self.style.configure("bannerFrame.TFrame", background=BACKGROUND_COLOR)
        self.lbl_title.label.configure(background=BACKGROUND_COLOR, fg='#FFFFFF')
        self.lbl_branch_id.label.configure(background=BACKGROUND_COLOR, fg='#FFFFFF')
        self.style.configure("frame_content_1.TFrame", background=FRAME_CONTENT_1_BG_COLOR)
        self.style.configure("frame_content_2.TFrame", background=FRAME_CONTENT_2_BG_COLOR)
        self.style.configure("frame_content_3.TFrame", background=FRAME_CONTENT_3_BG_COLOR)
        
    def _update_main(self):
        """ Internal function to 'factory reset' the main configuration. Excludes padding size."""
        width = 0
        
        # Accumulate the total width of content frames (does not include banner/navbar).
        for widget in self.containers:
            width += widget.winfo_width()
            
        for widget in range(len(self.containers)):
            self.containers[widget].configure(width=(width // len(self.containers)))
    
    def get_navbar_buttons(self, staff_role):
        navbar = self.display_navbar(staff_role, False)
        return navbar
        
        
    def display_navbar(self, staff_role, display:bool = False):
        OFFSET_LOGOUT_BTN = -1
        # Destroy any previously existing navigation bars
        if display==True:
            self.destroy_window_children(self.frame_banner_1.winfo_children())
        
        self.lbl_title.label.grid(row=0, column=0, columnspan=2, rowspan=1,sticky=tk.W)
        self.lbl_branch_id.label.grid(row=1, column=0, columnspan=2, rowspan=1,sticky=tk.W)
        
        # # Create a child frame inside the banner, give it a grid row/col then update.
        btn_frame = tk.Frame(self.frame_banner_1, background=BACKGROUND_COLOR)
        
        if display==True:
            btn_frame.grid(row=0, column=2, rowspan=2, columnspan=2, sticky=tk.NSEW, padx=16, pady=16)
        
        # Create a button and place it on the child frame.
        buttons = []
        btn_dict = {}
        
        if staff_role >= 5:
            buttons = ["Reports", "Inventory", "Events"]
            
        # Insert a prefix button Home and a suffix button logout.
        buttons.insert(0, "Home")
        buttons.insert(len(buttons), "Logout")
        
        # Configure rows and columns for the navbar so that it considers all new buttons
        btn_frame.grid_rowconfigure(0, weight=1)
        btn_frame.grid_rowconfigure(2, weight=1)
        btn_frame.grid_columnconfigure(0, weight=1)
        # btn_frame.grid_columnconfigure(len(buttons)+OFFSET_LOGOUT_BTN, weight=1)
            
        # Navigation Bar buttons
        for i in range(len(buttons)):
            btn = tk.Button(btn_frame, text=buttons[i], width=100 // len(buttons))
            if display==True:
                btn.grid(row=0, column=i, sticky=tk.NE, padx=3)
            btn_dict[buttons[i]] = btn
            
            if buttons[i] == "Logout":
                btn_dict[buttons[i]].configure(background="#dc3545", command=lambda: (self.destroy_window_children(self.containers), login.Login(self).display())) # login.Login(self).logout_user()
        return btn_dict
        
    def destroy_window_children(self, window:list | tk.Frame | ttk.Frame):
        """Destroy all child elements of a main tkinter Frame. """
        
        if isinstance(window, list):
            for i in range(len(window)):
                child = window[i].winfo_children()
                if len(child) != 0:
                    for j in range(len(child)):
                        child[j].destroy()
                        
                ## Not quite sure about this one therefore its temporary.
                # if len(child) == 0:
                #     child[j].destroy()
            return
        window.destroy()
        
    def display_window_children(self, window):
        return window.display()

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
        main_frame = ttk.Frame(self.main.master, style='main_frame.TFrame', width=self.main.master.winfo_reqwidth(), height=self.main.master.winfo_reqheight())
        main_frame.grid(row=0, column=0, sticky=tk.NSEW)        
        
        # Construct any windows/interfaces below
        self.main_window = Main(main_frame)
        self.login_interface = login.Login(self.main_window)
        self.menu_interface = menu.Menu(self.main_window)
        self.orders_interface = orders.Order(self.main_window)
        self.payment_interface = payments.Payment(self.main_window)
        
        # Home/Main
        
        # Login buttons
        self.login_interface.display()
        self.login_interface.btn_dict.get("Login").bind(
            "<Button>", func=lambda _: (
            (self.menu_interface.display(), self.orders_interface.display(), self.payment_interface.display(), self.main_window.display_navbar(self.login_interface.staff_role, True)) if self.login_interface.login_user(self.login_interface.input_box.input_box.get()) == True else ""
            )
        )
        
        # Menu buttons
        # self.menu_interface.btn_dict.get("KEY").bind("<Button>", func=lambda _: ((cmd1), (cmd2), if x == y else ""))
        
        # Orders buttons
        # self.orders_interface.btn_dict.get("KEY").bind("<Button>", func=lambda _: ((cmd1), (cmd2), if x == y else ""))
            
        # Payments buttons
        # self.payments_interface.btn_dict.get("KEY").bind("<Button>", func=lambda _: ((cmd1), (cmd2), if x == y else ""))
            
        # Kitchen/Inventory buttons
        # self.kitchen_interface.btn_dict.get("KEY").bind("<Button>", func=lambda _: ((cmd1), (cmd2), if x == y else ""))
            
        # Reports buttons
        # self.reports_interface.btn_dict.get("KEY").bind("<Button>", func=lambda _: ((cmd1), (cmd2), if x == y else ""))

if __name__ == '__main__':
    
    # Initialise the entire application and mapped settings
    app = Application(**app_settings)
    
    # Add any new settings after initialisation like below:
    # main_window.settings['SETTING_NAME'] = SETTING_VALUE
    
    # Run the tkinter event loop to control continuity
    app.main.master.mainloop()