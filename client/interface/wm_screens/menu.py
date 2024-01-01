# --------------------------------------------------------------------------------------- #
# 
#   This is the MENU page window manager screen module.
#   Any functions related to this particular interface should
#   specifically be programmed in this environment.
# 
# --------------------------------------------------------------------------------------- #

from client.interface.wm_screens.inventory import Inventory
from client.interface.toolkits import headings
from client.settings import BACKGROUND_COLOR
import tkinter.ttk as ttk
import tkinter as tk

class Menu(object):
    def __init__(self, parent):
        """ Construct a tkinter frame for Menu. """
        self._inventory = Inventory()
        self.parent = parent
        
        self.main_frame = tk.Frame(self.parent.frame_content_1)
        self.btn_dict = {}
        
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
        title = headings.Heading6(title_frame, text="MENU")
        title.label.grid(row=0, column=1, sticky=tk.NSEW)
        title.label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")
        
    def hide(self):
        self.main_frame.forget()
    
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