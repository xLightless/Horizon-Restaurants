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
    
    def hide_nav_menu(self):
        return self.master.forget(self.master_menu)
    
    
    
    
    
    
    
            
    def set_grid(self, widget, num_rows:int = 5, num_cols:int = 4, **args):
        """ Converts a frame to a grid system to create GUI solutions. """
        
        for x in range(num_rows):
            for y in range(num_cols):
                widget.grid(row=x, column=y)
                widget['bg'] = 'red'
        return widget
    
    
    # def grid_configure(self, tilemap:list[list], widget_to_tilemap):
    #     """
    #     Creates a grid with weighted columns visually. Provides better scaling for widgets.
        
    #     Example:
    #     [
    #         [0,0,0],
    #         [0,0,0],
    #         [0,0,0],
    #     ] - Creates a 3x3 tilemap where each element has no weight per row.
        
    #     [
    #         [0,1,0],
    #         [0,1,0],
    #         [0,1,0],
    #     ] - Creates a 3x3 tilemap where each 1 represents a column configure weighting.
    #     """
        
    #     for col in range(len(tilemap)):
    #         for row in range(len(tilemap[col])):
    #             position = tilemap[col][row] # Get the current position in an XY Tilemap.
            
                
                

    def add_h1(self, master, widget, ):
        h1_font = font.Font(family="Open Sans", size=12, weight="bold")
    
            
    def show_interface(self, **elements):
        """ Top-level manager for showing interface elements. Useful for managing UI elements."""
        
        print(elements)
        
        return f"Enabling {self.master}: {elements}."   
 
    def hide_interface(self, **elements):
        """ Top-level manager for hiding interface elements. Useful for managing UI elements."""
        
        for k,v in elements.items():
            elements[k].forget()
        
        return f"Disabling {self.master}: {elements}."
    
            
    
    def mainloop(self):
        """ Execute the tkinter tcl cycle. Can be called explicitly. """
        return tk.mainloop()
    
    
    