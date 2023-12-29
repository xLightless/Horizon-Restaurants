# --------------------------------------------------------------------------------------- #
# 
#   This is the MENU page window manager screen module.
#   Any functions related to this particular interface should
#   specifically be programmed in this environment.
# 
# --------------------------------------------------------------------------------------- #

from client.interface.wm_screens.inventory import Inventory
import tkinter.ttk as ttk

class Menu(object):
    def __init__(self, parent):
        """ Construct a tkinter frame for Menu. """
        self._inventory = Inventory()
        self.parent = parent
    
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