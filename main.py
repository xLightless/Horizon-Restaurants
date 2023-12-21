from client.interface import Interface
from client.interface.wm_screens.login import *
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

if __name__ == '__main__':
    app = App(
        args=app_settings
    )
    
    # Add any new settings after initialisation like below:
    # app.settings['SETTING_NAME'] = SETTING_VALUE
    
    login = Login(app.interface)
    
    
    
    
    # Run the tkinter program.
    app.interface.mainloop()
