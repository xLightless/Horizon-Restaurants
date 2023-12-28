# --------------------------------------------------------------------------------------- #
# 
#   This is the HOME page window manager screen module.
#   Any functions related to this particular interface should
#   specifically be programmed in this environment.
# 
# --------------------------------------------------------------------------------------- #

from client.interface import Interface
from client.interface.toolkits import inputs, headings
from client.settings import NAVBAR_HEIGHT
import tkinter as tk

class Home(object):
    def __init__(self, interface:Interface):
        self.i = interface
        self.i_frame = tk.Frame(self.i.master, padx=8, pady=8)
        self.i_frame.pack(fill=tk.BOTH, expand=True) 
        
        self.i_frame_child = tk.Frame(self.i_frame)
        self.i_frame_child.configure(bg='blue', bd=1, relief=tk.SOLID)
        self.i_frame_child.rowconfigure(3)
        self.i_frame_child.columnconfigure(3)
        self.i_frame_child.grid()
        
        i_top = tk.Frame(self.i_frame_child)
        i_top.configure(bg='yellow', bd=1, relief=tk.SOLID)
        i_top.grid(row=0, column=0, columnspan=3)
        # i_bottom = tk.Frame(self.i_frame_child)
        
        
        
        # # Create the layout for the home
        heading = headings.Heading6(i_top, "Horizon Restaurants")
        # subheading = headings.Heading3(self.i_frame, "Branch ID: 123123")
        heading.label.configure(bg="#1e1e1e", fg='white') # Add dark theme
        heading.label.grid(row=0, column=0, columnspan=3,sticky=tk.NSEW) 