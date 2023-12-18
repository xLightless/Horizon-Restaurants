from client.interface import Interface
from client.interface.wm_screens import login
from client.settings import *

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
        "width": False,
        "height": False
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
        self.master = Interface(interface=tk.Tk(), **args)
        self.settings = self.master._settings
        self.login_interface = login.LoginInterface(self.master)
        
        
        
if __name__ == '__main__':
    app = App(
        args=app_settings
    )
    
    # Add any new settings after initialisation like below:
    # app.settings['SETTING_NAME'] = SETTING_VALUE
    
    # Run the tkinter program.
    app.master.mainloop()
