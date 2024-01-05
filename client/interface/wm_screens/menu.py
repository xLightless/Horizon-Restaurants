# --------------------------------------------------------------------------------------- #
# 
#   This is the MENU page window manager screen module.
#   Any functions related to this particular interface should
#   specifically be programmed in this environment.
# 
# --------------------------------------------------------------------------------------- #

# from client.interface.wm_screens.inventory import Inventory
from client.interface.toolkits import headings
from client.settings import BACKGROUND_COLOR
from tkinter import simpledialog
import tkinter.ttk as ttk
import tkinter as tk

class Menu(object):
    def __init__(self, parent):
        """ Construct a tkinter frame for Menu. """
        # self._inventory = Inventory()
        self.parent = parent
        self.style = ttk.Style()
        
        # Search bar, orders review, payment
        # Each item should be treated as its own independent object however hardcoding orders/payments is fine
        self.left_frame = ttk.Frame(self.parent.content_frame, style="left_frame.TFrame", name="left_frame", border=1, relief=tk.SOLID)
        
        # Menu
        self.right_frame = ttk.Frame(self.parent.content_frame, style="right_frame.TFrame", name="right_frame", border=1, relief=tk.SOLID)
        self._title_frame = ttk.Frame(self.right_frame, style="menu_title_frame.TFrame", name="menu_title_frame")
        
    def display_frames(self):
        # Search bar, orders review, payment
        self.left_frame.grid(row=0, column=0, rowspan=3, sticky=tk.NSEW)
        
        # Menu
        self.right_frame.grid(row=0, column=1, rowspan=3, columnspan=2, sticky=tk.NSEW)
        self.right_frame.grid_rowconfigure(0, weight=0)
        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)
        
        self._title_frame.grid(row=0, column=0, sticky=tk.NSEW)
        self._title_frame.grid_columnconfigure(0, weight=1)
        self._title_frame.grid_columnconfigure(1, weight=1)
        self._title_frame.grid_columnconfigure(2, weight=1)
        
        title = headings.Heading6(self._title_frame, text="Menu Items")
        title.label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")
        title.label.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)
        
        # Styling
        self.style.configure("left_frame.TFrame", background='yellow')
        self.style.configure("right_frame.TFrame", background='lightblue')
        
    
    
    def get_menu(self):
        """ Gets the menu and returns all items. """
        return
    
    def get_item(self, item_name:str):
        """ Get an items data from menu. """
        return
    
    def get_item_description(self, item_name:str):
        """ Get the description of a menu item. """
        return
    
    def get_description_allergens(self):
        """ Get the allgerns of an item. """
        return
    
    def get_selected_food_items(self, **args) -> dict:
        return
    
    def suggest_food_items(self):
        """ Arbitrarily suggest food to purchase. """
        return
    
    def mark_items_as_unavailable(self):
        """ Update the menu item as unavailable. """
        return
    
    def check_item_availability(self, item_name:str) -> int:
        """ Check the availablity of a menu item. """
        return self._inventory.check_inventory_stock(item_name)
    
    def _set_item(self, item_name:str, description:str, photo_url:str = None):
        """ Private method for inserting a menu item. """
        return
    
    def _set_item_description(self, description:str):
        """ Private method for inserting a menu item description. """
        return
    
    def _set_item_price(self, price:float):
        """ Private method for inserting a menu item price. """
        return
    
    def _delete_item(self, item_name:str):
        """ Private method for deleting a menu item. """
        return
    
    def _set_category(self, category_name:str):
        """ Private method for inserting a menu item category. """
        return
    
    def _update_category(self, category_name:str):
        """ Private method for updating a menu item category. """
        return

    def _delete_category(self, category_name:str):
        """ Private method for deleting a menu item category. """
        return