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
            
            # Title Frame
            self.title_frame = ttk.Frame(self.parent.content_frame, style="title_frame.TFrame", border=3, relief=tk.SOLID, name="title_frame_kitchen")
            self.title = headings.Heading6(self.title_frame, text="Kitchen")
            
            # Kitchen Frame
            self.kitchen_frame = ttk.Frame(self.parent.content_frame, style="kitchen_frame.TFrame", border=3, relief=tk.SOLID, name="kitchen_frame")
    
    def display_frames(self):
        """Display kitchen frames to the screen. """
        
        # Title Frame
        self.title_frame.grid_rowconfigure(0, weight=0)
        self.title_frame.grid_columnconfigure(0, weight=1)
        self.title_frame.grid_columnconfigure(1, weight=1)
        self.title_frame.grid_columnconfigure(2, weight=1)
        self.title_frame.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)
        
        # Title
        self.title.label.configure(bg=BACKGROUND_COLOR, fg='#FFFFFF')
        self.title.label.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)
        
        # Kitchen Frame
        self.style.configure("kitchen_frame.TFrame", background=BACKGROUND_COLOR, border=3, relief=tk.SOLID)
        self.kitchen_frame.grid(row=1, column=0, columnspan=3, rowspan=2, sticky=tk.NSEW)
        
        
        # Orders
        
    def create_order_widget(self):
        return
    
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