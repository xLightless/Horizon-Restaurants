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