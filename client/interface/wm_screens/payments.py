
from client.interface.toolkits.typography.font import *
from client.interface.toolkits import inputs, headings
# from client.interface.wm_screens.inventory import Inventory
from client.settings import INITIAL_HEIGHT, INITIAL_WIDTH, NAVBAR_HEIGHT, BACKGROUND_COLOR, MAIN_GRID_BOXES
from client.errors import InvalidCredentialsError
from server.sql.database import database
from tkinter import messagebox

import tkinter as tk
import tkinter.ttk as ttk

class Offers(object):
    def get_discounts():
        return
    
    def validate_discount(self, discount_code:str):
        return
    
    def _create_discount(self, discount_code:str):
        return
    
    def _update_discount(self, discount_code:str, percentage:float):
        return
    
    def _delete_discount(self, discount_code:str):
        return


class Payment(object):
    def __init__(self, parent):
        """ Construct a tkinter frame for Menu. """
        self.parent = parent
        
        self.main_frame = tk.Frame(self.parent.frame_content_3)
        
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
        title = headings.Heading6(title_frame, text="PAYMENTS")
        title.label.grid(row=0, column=1, sticky=tk.NSEW)
        title.label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")
    
    def check_for_discounted_offers(self) -> Offers:
        return Offers.get_discounts()
    
    def validate_payment(self) -> bool:
        return
    
    def cancel_payment(self):
        return
    
    def refund_payment(self):
        return