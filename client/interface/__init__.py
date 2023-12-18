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
from tkinter import Wm
import tkinter as tk


class Interface(object):
    """ Handles the creation of top-level tkinter application interfaces. Can be instantiated numerous times for multiple independent Interfaces."""
    
    def __init__(self, interface:tk.Tk, **args):
        """ Initialise an instance of tkinter. Pass args to dynamically interact with the internal window manager.

        Args:
            interface (tk.Tk): the tkinter top-level widget object.
            **args (dict): pass any window manager settings.
        """
        super().__init__()
        self.interface = interface
        self._settings = args
        
        # Create a Wm Master Frame to contain elements later for complexity handling
        self.main_frame = tk.Frame(self.interface, bg='lightgray', width=INITIAL_WIDTH, height=INITIAL_HEIGHT)
        self.main_frame.grid()
        
        # Check if the interface is a tkinter top level window
        if isinstance(self.interface, tk.Tk) == True:
            self.window_manager = list(Wm.__dict__.keys())
                
            preset_wm_settings = [i for i in self._settings if i in self.window_manager]
            for key in preset_wm_settings:
                
                # Gets the tkinter.Tk Wm attribute and sets the passed preset into the class object.
                wm_func = self.interface.__getattribute__(key)
                
                if (type(self._settings[key]) == dict):
                    # Dynamically unpack and assign key/values to window manager
                    wm_func(**self._settings[key])
                else:
                    # Set superset key/values to window manager
                    wm_func(self._settings[key])
            
            
    def set_grid(self, widget, num_rows:int = 5, num_cols:int = 4, **args):
        """ Converts a frame to a grid system to create GUI solutions. """
        
        for x in range(num_rows):
            for y in range(num_cols):
                widget.grid(row=x, column=y)
                widget['bg'] = 'red'
        return widget
            
    def show_interface(self, **elements):
        """ Top-level manager for showing interface elements. Useful for managing UI elements."""
        
        return f"Enabling {self.interface}: {elements}."   
 
    def hide_interface(self, **elements):
        """ Top-level manager for hiding interface elements. Useful for managing UI elements."""
        
        return f"Disabling {self.interface}: {elements}."
    
            
    
    def mainloop(self):
        """ Execute the tkinter tcl cycle. Can be called explicitly. """
        return tk.mainloop()
    
    
    