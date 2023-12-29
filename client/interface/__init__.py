# --------------------------------------------------------------------------------------- #
# 
#   This module is boilerplate for the configuration of graphical interfaces.
#   Its important to import into main rather than editing code here.
# 
# --------------------------------------------------------------------------------------- #

# from client.interface.toolkits.mapper import Roots
# from client.interface.objects.frame
from client.settings import INITIAL_WIDTH, INITIAL_HEIGHT
from client.interface.toolkits.mapper import is_subset
from tkinter import Wm, font
from authors import authors, show_creators
import tkinter as tk


class Interface(object):
    """ Handles the creation of top-level tkinter application interfaces. Can be instantiated numerous times for multiple independent Interfaces."""
    
    def __init__(self, master:tk.Tk = tk.Tk(), **args):
        """ Initialise an instance of tkinter. Pass args to dynamically interact with the internal window manager.

        Args:
            interface (tk.Tk): the tkinter top-level widget object.
            **args (dict): pass any window manager settings.
        """
        self.master = master
        # self.master_menu = tk.Menu(self.master)
        self._settings = args

        # Check if the interface is a tkinter top level window
        if isinstance(self.master, tk.Tk) == True:
            self.window_manager = list(Wm.__dict__.keys())
                
            preset_wm_settings = [i for i in self._settings if i in self.window_manager]
            for key in preset_wm_settings:
                
                # Gets the tkinter.Tk Wm attribute and sets the passed preset into the class object.
                wm_func = self.master.__getattribute__(key)
                
                # print(wm_func)
                
                if (type(self._settings[key]) == dict):
                    # Dynamically unpack and assign key/values to window manager
                    wm_func(**self._settings[key])
                else:
                    # Set superset key/values to window manager
                    wm_func(self._settings[key])
                    
    def change_wm_screen(self, screen):
        return self.master.slaves()
                    
    def show_nav_menu(self, dict_to_menus:dict = None):
        """Create a tkinter menu. If no parameters set then defaults to implicit example."""
        
        if dict_to_menus == None:
            dict_to_menus = {
                "File": {
                    "Save": None
                },
                "View": {
                    "Order": None,
                    "Tables": None,
                    "Reservations": None,
                },
                "About": show_creators
            }
        
        # Add a menu to the top level application window
        self.master.config(menu=self.master_menu)
        self.master.option_add('*tearOff', False)
        menu_list = {}
        
        # Pass a dictionary into a sorted menu set
        for key in dict_to_menus.keys():
            # print(temp_menu.__dict__)
            if type(dict_to_menus[key]) == dict:
                menu_list[key] = tk.Menu(self.master_menu)
                self.master_menu.add_cascade(label=key, menu=menu_list[key])
                for command_name, command in dict_to_menus[key].items():
                    # menu_list[key] = tk.Menu(menu)
                    # menu.add_cascade(label=key, menu=menu_list[key])
                    menu_list[key].add_command(label=command_name, command=command)
                    
            else:
                self.master_menu.add_command(label=key, command=dict_to_menus[key])
        return menu_list   
    
    