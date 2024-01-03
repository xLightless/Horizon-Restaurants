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
import tkinter.ttk as ttk

class Home(object):
    def __init__(self, parent):
        self.parent = parent
        
        self.home_frame = ttk.Frame(self.parent, style="home_frame.TFrame", name="home_frame")
        
    # def display()