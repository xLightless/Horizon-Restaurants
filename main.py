from client.interface import Interface
from client.interface.wm_screens.login import *
from client.settings import *
from tkinter import messagebox
from authors import authors

import tkinter as tk
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
    "geometry" : "%dx%d" % (INITIAL_WIDTH, INITIAL_HEIGHT),
    "wm_resizable" : {
        "width": True,
        "height": True
    }
}

class App(object):
    """Horizon Restaurant Management System (HRMS) Application."""
    
    def __init__(self, args=None):
        """ Create a custom tkinter application.

        Args:
            app_settings (dict): _description_
            interface_options (dict): _description_
        """
        
        if args is None: args = {}
        
        # Top-most level master frame
        self.interface = Interface(**args)
        self.settings = self.interface._settings
        
    def show_creators(self):
        message = ""
        for k, v in authors.items():
            message += f"{k} : {v}\n"
            
        return messagebox.showinfo("Project Authors", f"Made by UWE Bristol Students: \n{message}")

if __name__ == '__main__':
    app = App(
        args=app_settings
    )
    
    # Add any new settings after initialisation like below:
    # app.settings['SETTING_NAME'] = SETTING_VALUE
    
    # Add a menu to the top level application window
    menu = tk.Menu(app.interface.master)
    app.interface.master.config(menu=menu)
    app.interface.master.option_add('*tearOff', False)
    app.interface.master.eval('tk::PlaceWindow . center')
    file_menu = tk.Menu(menu)
    edit_menu = tk.Menu(menu)
    
    # File Drop down menu
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label='Save')
    file_menu.add_command(label='Save As')
    
    # Edit Menu
    menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Order")
    
    # About Us
    menu.add_command(label="About us", command=app.show_creators)
    
    login = Login(app.interface)
    
    
    
    
    # Run the tkinter program.
    app.interface.mainloop()
