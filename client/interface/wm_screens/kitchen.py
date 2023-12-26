
from client.interface.wm_screens.orders import Order


class Kitchen(object):
    def get_bulk_orders(self) -> Order:
        return
    
    def mark_order_as_ready(self) -> bool:
        return
    
    def get_sequential_orders(self, table_number:int):
        return
    
    def check_category_item_availability(self, category_name:str) -> dict:
        return
    
    def get_item(self, item_name:int) -> dict:
        return