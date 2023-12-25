from client.interface import Interface
from client.interface.wm_screens.login import *
from client.settings import *
from tkinter import messagebox
from authors import authors
from typing import Optional

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
        
        # Create the first level screen
        self.create_app_menu()
        login = Login(interface=self.interface)
        

    def create_app_menu(self, dict_to_menus:dict = None):
        """Create a tkinter menu."""
        
        if dict_to_menus == None:
            dict_to_menus = {
                "File": {
                    "Save": None
                },
                "Edit": {
                    "Order": None
                },
                "About": self.show_creators
            }
        
        # Add a menu to the top level application window
        menu = tk.Menu(self.interface.master)
        self.interface.master.config(menu=menu)
        self.interface.master.option_add('*tearOff', False)
        menu_list = {}
        
        # Pass a dictionary into a sorted menu set
        for key in dict_to_menus.keys():
            # print(temp_menu.__dict__)
            if type(dict_to_menus[key]) == dict:
                for command_name, command in dict_to_menus[key].items():
                    menu_list[key] = tk.Menu(menu)
                    menu.add_cascade(label=key, menu=menu_list[key])
                    menu_list[key].add_command(label=command_name, command=command)
                    
            else:
                menu.add_command(label=key, command=dict_to_menus[key])
        return menu_list
        
        
        
        
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
    
    
    
    # Run the tkinter program.
    app.interface.mainloop()
