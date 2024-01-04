from server.sql.database import database
from client.interface.toolkits import inputs, headings
from client.settings import BACKGROUND_COLOR

import tkinter as tk
import tkinter.ttk as ttk

class Kitchen(object):
    def __init__(self, parent):
        self.parent = parent
        
        if str(type(self.parent)) == "<class '__main__.Main'>":
            self.style:ttk.Style = self.parent.style
            self.style.configure("title_frame.TFrame", background=BACKGROUND_COLOR)
            
            self.title_frame = ttk.Frame(self.parent.content_frame, style="title_frame.TFrame", border=3, relief=tk.SOLID, name="title_frame_kitchen")
    
    # def get_bulk_orders(self) -> Order:
    #     return
    
    def mark_order_as_ready(self) -> bool:
        return
    
    def get_sequential_orders(self, table_number:int):
        return
    
    def check_category_item_availability(self, category_name:str) -> dict:
        return
    
    def get_item(self, item_name:int) -> dict:
        return