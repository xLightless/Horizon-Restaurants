from client.interface import Interface
from client.interface.wm_screens import home, login
from client.settings import *
from client.interface.toolkits import headings
from typing import Optional

import tkinter as tk
import tkinter.ttk as ttk
import asyncio
import logging
import traceback

# Configure the application to set logging levels in terminal.
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S'
# )

app_settings = {
    "title" : TITLE,
    "wm_resizable" : {
        "width": True,
        "height": True
    },
    "bg":'red'
}


class Main(object):
    def __init__(self, parent):
        self.style = ttk.Style()
        self.stringVar = tk.StringVar()

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
        
        # for i in range(1, MAIN_GRID_BOXES+1):
        #     frame = ttk.Frame(parent, style=f"frame_content_{i}.TFrame", width=100 // MAIN_GRID_BOXES)
        #     frame.grid(row=1, column=i, sticky=tk.NSEW, padx=3, pady=3)
        #     frame.grid_rowconfigure(0, weight=1)
        #     frame.grid_columnconfigure(0, weight=1)
            
        #     # Add each container to a dictionary to modify efficiently.
        #     self.containers[f"frame_content_{i}.TFrame"] = frame
            
            
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
        self.style.configure("frame_content_1.TFrame", background=BACKGROUND_COLOR)
        self.style.configure("frame_content_2.TFrame", background=BACKGROUND_COLOR)
        self.style.configure("frame_content_3.TFrame", background=BACKGROUND_COLOR)
        
        
    def display_navbar(self, staff_role):
        OFFSET_LOGOUT_BTN = -1
        
        self.lbl_title.label.grid(row=0, column=0, columnspan=2, rowspan=1,sticky=tk.W)
        self.lbl_branch_id.label.grid(row=1, column=0, columnspan=2, rowspan=1,sticky=tk.W)
        
        # # Create a child frame inside the banner, give it a grid row/col then update.
        btn_frame = tk.Frame(self.frame_banner_1, background=BACKGROUND_COLOR)
        btn_frame.grid(row=0, column=2, rowspan=2, columnspan=2, sticky=tk.NSEW, padx=16, pady=16)
        # btn_frame.configure(bd=1, relief=tk.SOLID)
        
        # # Create a button and place it on the child frame.
        
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
        btn_frame.grid_columnconfigure(len(buttons)+OFFSET_LOGOUT_BTN, weight=1)
            
        for i in range(len(buttons)):
            btn = tk.Button(btn_frame, text=buttons[i], width=100 // len(buttons))
            btn.grid(row=0, column=i, sticky=tk.NE, padx=3)
            btn_dict[buttons[i]] = btn
            
        # Logout button. Make it obvious.
        btn_dict['Logout'].configure(background='#d9534f')

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
        style = ttk.Style()
        
        # Add a main frame to master
        main_frame = ttk.Frame(self.main.master, style='main_frame.TFrame', width=self.main.master.winfo_reqwidth(), height=self.main.master.winfo_reqheight())
        main_frame.grid(row=0, column=0, sticky=tk.NSEW)        
        style.configure("main_frame.TFrame", background=BACKGROUND_COLOR, bd=1, relief=tk.SOLID)
        
        # The first screen and fall back screen when all gets destroyed
        main_window = Main(main_frame)
        
        # An interface for login built ontop of main_window
        login_interface = login.Login(main_window)
        if login_interface.is_logged_in():
            
            # Display the navigation system based on the database staff role.
            # Acts as an additional security measure for checking if someone should be allowed to do specific tasks.
            login_interface.parent.display_navbar(staff_role = login_interface.staff_role)
        

if __name__ == '__main__':
    
    app = Application(**app_settings)
    app.main.master.mainloop()
    
    # Add any new settings after initialisation like below:
    # main_window.settings['SETTING_NAME'] = SETTING_VALUE