# --------------------------------------------------------------------------------------- #
# 
#   This is the ORDERS page window manager screen module.
#   Any functions related to this particular interface should
#   specifically be programmed in this environment.
# 
# --------------------------------------------------------------------------------------- #

from client.interface.wm_screens.menu import Menu

class Order(object):
    def __init__(self, order_id:int):
        pass
    
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