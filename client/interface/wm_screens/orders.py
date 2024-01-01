# --------------------------------------------------------------------------------------- #
# 
#   This is the ORDERS page window manager screen module.
#   Any functions related to this particular interface should
#   specifically be programmed in this environment.
# 
# --------------------------------------------------------------------------------------- #

from client.interface.toolkits.typography.font import *
from client.interface.toolkits import inputs, headings
from client.interface.wm_screens.inventory import Inventory
from client.interface.wm_screens.menu import Menu
from client.settings import INITIAL_HEIGHT, INITIAL_WIDTH, NAVBAR_HEIGHT, BACKGROUND_COLOR, MAIN_GRID_BOXES
from client.errors import InvalidCredentialsError
from server.sql.database import database
from tkinter import messagebox

import tkinter as tk
import tkinter.ttk as ttk

class Order(object):
    def __init__(self, parent):
        """ Construct a tkinter frame for Orders. """
        self.parent = parent
        
        self.main_frame = tk.Frame(self.parent.frame_content_2)
        
    def display(self):
        self.main_frame.grid(sticky=tk.NSEW)
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        # Title frame for menu        
        title_frame = ttk.Frame(self.main_frame, style="title_frame.TFrame", border=3, relief=tk.SOLID)
        title_frame.grid(row=0, column=0, sticky=tk.NSEW)
        title_frame.grid_columnconfigure(0, weight=1)
        title_frame.grid_columnconfigure(1, weight=1)
        title_frame.grid_columnconfigure(2, weight=1)
        
        # Title
        title = headings.Heading6(title_frame, text="ORDERS")
        title.label.grid(row=0, column=1, sticky=tk.NSEW)
        title.label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")
    
    def get_menu(self) -> Menu:
        return Menu.get_menu()
    
    def place_order(self, order_id:int):
        return
    
    def cancel_order(self, order_id:int):
        return
    
    def pack_order(self, order_id:int):
        return
    
    def deliver_order(self, order_id:int):
        return
    
    def update_order(self, order_id:int):
        return