from server.sql.database import database
from client.interface.toolkits import inputs, headings
from client.settings import BACKGROUND_COLOR
from server.sql.database import database, SQLKitchenOrders, SQLMenu, SQLReservations
from tkinter import messagebox
from datetime import datetime

import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd


class Kitchen(object):
    def __init__(self, parent):
        self.parent = parent
        
        # Database manipulation handling
        self.kitchen_orders = SQLKitchenOrders()
        self.reservation = SQLReservations()
        self.menu = SQLMenu()
        
        # Create frames if the parent is of main window
        if str(type(self.parent)) == "<class '__main__.Main'>":
            self.style:ttk.Style = self.parent.style
            self.style.configure("title_frame.TFrame", background=BACKGROUND_COLOR)
            
            # Title Frame
            self.title_frame = ttk.Frame(self.parent.content_frame, style="title_frame.TFrame", border=3, relief=tk.SOLID, name="title_frame_kitchen")
            self.title = headings.Heading6(self.title_frame, text="Kitchen")
            
            # Kitchen Frame
            self.kitchen_frame = ttk.Frame(self.parent.content_frame, style="kitchen_frame.TFrame", border=3, relief=tk.SOLID, name="kitchen_frame")
            
            # Order Management Frame
            self.order_management_frame = ttk.Frame(self.kitchen_frame, style="order_management_frame.TFrame", name="order_management_frame", height=64)
            self.buttons = ["Mark Selected Order", "Cancel Selected Order", "View Orders in Bulk"]
            
            # Active Orders
            self.active_orders_frame = ttk.Frame(self.kitchen_frame, style="active_orders_frame.TFrame", name="active_orders_frame")
            
            # TreeView Active Orders
            # self.treeview_order_columns = self.kitchen_orders.get_unpaid_orders()
            # self.order_columns = self.kitchen_orders.get_orders().columns.to_list()
            
            self.order_columns = ["Order ID", "Order Status", "Menu Item", "Table Number"]
            self.treeview_orders = ttk.Treeview(
                self.active_orders_frame, 
                columns=self.order_columns,
                show="headings",
                name="kitchen_treeview_orders"
            )
    
    def display_frames(self):
        """Display kitchen frames to the screen. """

        # Treeview Orders
        self.style.configure("TreeView")

        # Title Frame
        self.title_frame.grid_rowconfigure(0, weight=0)
        self.title_frame.grid_columnconfigure(0, weight=1)
        self.title_frame.grid_columnconfigure(1, weight=1)
        self.title_frame.grid_columnconfigure(2, weight=1)
        
        # Title
        self.title.label.configure(bg=BACKGROUND_COLOR, fg='#FFFFFF')
        
        # Kitchen Frame
        self.style.configure("kitchen_frame.TFrame", background=BACKGROUND_COLOR, border=3, relief=tk.SOLID)
        self.kitchen_frame.grid_rowconfigure(0, weight=0) # Fix in place the button row
        self.kitchen_frame.grid_rowconfigure(1, weight=1)
        self.kitchen_frame.grid_columnconfigure(0, weight=1)
        self.kitchen_frame.grid_columnconfigure(1, weight=1)
        
        # Order Management Frame
        self.style.configure("order_management_frame.TFrame", background=BACKGROUND_COLOR)
        
        # Active Orders
        self.style.configure("active_orders_frame.TFrame", background=BACKGROUND_COLOR)
        self.active_orders_frame.grid_rowconfigure(0, weight=1)
        self.active_orders_frame.grid_rowconfigure(1, weight=1)
        self.active_orders_frame.grid_columnconfigure(0, weight=1)
        self.active_orders_frame.grid_columnconfigure(1, weight=1)
        self.active_orders_frame.grid_columnconfigure(2, weight=1)
        
        
        self.title_frame.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)
        self.title.label.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)
        
        self.kitchen_frame.grid(row=1, column=0, columnspan=3, rowspan=2, sticky=tk.NSEW)
        self.order_management_frame.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, padx=12, pady=12)
        self.active_orders_frame.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW, padx=12, pady=12)
        
        self.treeview_orders.grid(row=0, column=0, rowspan=2, columnspan=3, sticky=tk.NSEW)

        
    def create_dynamic_headings(self):
        """Gets the treeview headings dynamically. Even if one is appended, it MAY be put onto the screen."""
        
        for col in self.order_columns:
            self.treeview_orders.heading(column=col, text=col)
            self.treeview_orders.column(column=col, width=100 // len(self.order_columns), anchor="center")
        
    def unpopulate_orders_display(self):
        """Removes all data from the display to prevent duplicaiton. """
        for item in self.treeview_orders.get_children():
            self.treeview_orders.delete(item)
    
    def populate_orders_display(self):
        """Fills the table with orders to complete. """
        
        data = self.kitchen_orders.get_displayed_orders()
        data = data.astype({'table_number': int})
        
        for key, value in data.iterrows():
            self.treeview_orders.insert('', "end", values=tuple(value))
            
    def get_selected_row(self):
        row = self.treeview_orders.focus()
        return row
        
    def get_order_selection_time(self):
        """Get the serve_date and serve_time using local datetime. """
        
        date_time = datetime.now()
        date = date_time.date().strftime("%Y:%m:%d").replace(':', '-')
        time = date_time.time().strftime("%H:%M:%S")
        return date, time

        
    def update_mark_as_ready_button(self, buttons):
        """Update cancellation of orders per selection. """
        
        # Get the date and time for order row
        date, time = self.get_order_selection_time()
        

        # Bind a command to the button to update its usage per new selection by the user.
        buttons.bind("<Button>", func=lambda _, data=self.treeview_orders.item(self.get_selected_row())['values'], row_id=self.treeview_orders.selection()[0]: (
            
            # Update on the screen the order has been cancelled.
            self.treeview_orders.item(row_id, values=(data[0], "COMPLETED", data[2], int(data[3]))),
            
            # Update the database to cancel the item.
            self.kitchen_orders.mark_order_as_ready(order_primary_key=data[0], serve_date=date, serve_time=time)
        ))
        
        
        
    def update_cancel_order_button(self, buttons):
        """Update cancellation of orders per selection. """
        
        # Bind a command to the button to update its usage per new selection by the user.
        buttons.bind("<Button>", func=lambda _, data=self.treeview_orders.item(self.get_selected_row())['values'], row_id=self.treeview_orders.selection()[0]: (
            
            # Update on the screen the order has been cancelled.
            self.treeview_orders.item(row_id, values=(data[0], "CANCELLED", data[2], int(data[3]))),
            
            # Update the database to cancel the item.
            self.kitchen_orders.cancel_kitchen_order(order_id_pk=data[0])
        ))
        
    def update_bulk_orders_button(self, buttons):
        """Display the kitchen orders in bulk by their item name. """
        
        # The selected row by the user.
        item_name = self.treeview_orders.item(self.get_selected_row())['values'][2]
        kitchen_orders = self.kitchen_orders.get_displayed_orders()
        
        item_name_bulk_total = len(kitchen_orders.loc[kitchen_orders['item_name'] == item_name])
        buttons.bind("<ButtonRelease>", func=lambda _: (
            messagebox.showinfo(
                "View Kitchen Orders in Bulk!",
                f"This selection suggests there are: \n* {item_name}: {item_name_bulk_total}"
            )
        ))
           
    def create_management_buttons(self):
        btn_list = []
        
        # Create the button objects
        for i in range(len(self.buttons)):
            button_name = self.buttons[i].lower().replace(' ', '_')
            button = tk.Button(
                master=self.order_management_frame,
                text=self.buttons[i],
                width=100 // len(self.buttons),
                name=button_name,
                padx=0,
                pady=0
            )
            btn_list.append(button)
        return btn_list
            
    def display_management_buttons(self, buttons):
        self.order_management_frame.grid_rowconfigure(0, weight=1)
        
        for i in range(len(buttons)):
            # buttons[i].configure()
            self.order_management_frame.grid_columnconfigure(i, weight=1)
            buttons[i].grid(row=0, column=i, sticky=tk.NSEW)
            
        # Update the tree view selection and the buttons to modify orders.
        self.treeview_orders.bind("<ButtonRelease>", func=lambda _: (
            self.update_mark_as_ready_button(buttons=buttons[0]),
            self.update_cancel_order_button(buttons=buttons[1]),
            self.update_bulk_orders_button(buttons=buttons[2])
            ))
        
        # Populate the table when this scope of code is executed.
        self.populate_orders_display()