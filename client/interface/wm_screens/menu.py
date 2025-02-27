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
from server.sql.database import SQLMenu
from PIL import Image, ImageTk
import requests
from io import BytesIO
import tkinter.ttk as ttk
import tkinter as tk
import datetime
from tkinter.messagebox import showinfo
import pandas as pd


class Menu(object):
    def __init__(self, parent):
        """ Construct a tkinter frame for Menu. """
        # self._inventory = Inventory()
        self.parent = parent
        self.style = ttk.Style()
        self.menu = SQLMenu()
        #sql.menu.get

        # Search bar, orders review, payment
        # Each item should be treated as its own independent object ho lwever hardcoding orders/payments is fine
        self.left_frame = ttk.Frame(self.parent.content_frame, style="left_frame.TFrame", name="left_frame", border=1, relief=tk.SOLID)
        self.search_frame = ttk.Frame(self.left_frame, style ="search_frame.TFrame", name = "search_frame")
        self.orders_frame = ttk.Frame(self.left_frame, style ="orders_frame.TFrame", name = "order_frame")
        self.total_order_frame = ttk.Frame(self.orders_frame, style="total_order_frame.TFrame", name = "total_order_frame") # WIP
        self.payment_frame = ttk.Frame(self.orders_frame, style = "payment_frame.TFrame", name = "payment_frame") # Include Payment and Delete orders button.
        
        # Menu
        self.right_frame = ttk.Frame(self.parent.content_frame, style="right_frame.TFrame", name="right_frame", border=1, relief=tk.SOLID)
        self._title_frame = ttk.Frame(self.right_frame, style="menu_title_frame.TFrame", name="menu_title_frame")
        self.menu_entry_frame = ttk.Frame(self.right_frame, style="menu_entry_frame.TFrame", name="menu_entry_frame")
        self.menu_items_frame = ttk.Frame(self.right_frame, style="menu_items_frame.TFrame", name="menu_items_frame")
        
        self.item_counter = 0 #Big Brain moment, interal id to replace as order_item_id when payment is clicked
        self.order_items = {} # Dictionary to track each orders details in treeview

        self.preload_menu_images()
        
    def display_frames(self):
        # Left side with includes the frames for the search bars and orders
        self.left_frame.grid_rowconfigure(0, weight=1)
        self.left_frame.grid_rowconfigure(1, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)

        # Search bar frame
        self.search_frame.grid_rowconfigure(0, weight=0)
        self.search_frame.grid_rowconfigure(1, weight=1)
        self.search_frame.grid_rowconfigure(2, weight=6)
        self.search_frame.grid_columnconfigure(0, weight=1)
        self.search_frame.grid_columnconfigure(1, weight=1)
        self.search_frame.grid_columnconfigure(2, weight=1)

        # Order frame including payment widget
        self.orders_frame.grid_rowconfigure(0, weight=0)
        self.orders_frame.grid_rowconfigure(1, weight=6)
        self.orders_frame.grid_rowconfigure(2, weight =2)
        self.orders_frame.grid_columnconfigure(0, weight=1)
        self.orders_frame.grid_columnconfigure(1, weight=1)

        self.total_order_frame.grid_rowconfigure(0, weight = 1)
        self.total_order_frame.grid_columnconfigure(0, weight =1)
        self.total_order_frame.grid_columnconfigure(1, weight = 1)
        self.total_order_frame.grid_columnconfigure(2, weight =1)

        self.payment_frame.grid_rowconfigure(0, weight = 1)
        self.payment_frame.grid_columnconfigure(0, weight = 1)
        self.payment_frame.grid_columnconfigure(1, weight = 1)
        self.payment_frame.grid_columnconfigure(2, weight = 1)

        # Right Side / Menu Frame
        self.right_frame.grid_rowconfigure(0, weight=0)
        self.right_frame.grid_rowconfigure(1, weight=0)
        self.right_frame.grid_rowconfigure(2, weight=10)
        self.right_frame.grid_columnconfigure(0, weight=10)
        self.right_frame.grid_columnconfigure(1, weight=0)

        self._title_frame.grid_columnconfigure(0, weight=1)
        self._title_frame.grid_columnconfigure(1, weight=1)
        self._title_frame.grid_columnconfigure(2, weight=1)

        self.menu_entry_frame.grid_columnconfigure(0, weight = 1)

        self.menu_items_frame.grid_columnconfigure(0, weight=10)
        self.menu_items_frame.grid_columnconfigure(1, weight=0)
        self.menu_items_frame.grid_rowconfigure(0, weight = 1)

        # Widgets
        title = headings.Heading6(self._title_frame, text="Menu Items")
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self.search_frame, textvariable=self.search_var)
        self.search_button = ttk.Button(self.search_frame, text="Search", command=self.search_menu_items)

        payment_button = ttk.Button(self.payment_frame, text="Pay", command=self.process_payment) 
        clear_order_button = ttk.Button(self.payment_frame, text="Clear Order", command=self.clear_order)
        
        # Initalised to access in other methods
        self.order_treeview = ttk.Treeview(self.total_order_frame, columns=("Item Name", "Price"))
        self.order_treeview.heading("#0", text="ID", anchor="w") 
        self.order_treeview.heading("Item Name", text="Item Name", anchor="w")
        self.order_treeview.heading("Price", text="Price", anchor="w")
        self.order_treeview.column("#0", width=0, stretch=tk.NO)#Way to hide it
        self.order_treeview.column("Item Name", anchor="w", width=100)
        self.order_treeview.column("Price", anchor="w", width=100)

        self.order_scrollbar = ttk.Scrollbar(self.total_order_frame, orient="vertical", command=self.order_treeview.yview)
        self.order_treeview.configure(yscrollcommand=self.order_scrollbar.set)
        self.order_treeview.bind("<Double-1>", self.on_treeview_item_click) 
        self.checkbox_var = tk.IntVar() # Checks the state, where clicked or not
        self.confirm_checkbox = ttk.Checkbutton(self.payment_frame, text="Discount", variable=self.checkbox_var)


        # Configure Widgets
        
        title.label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")

        # Styling for frames
        self.style.configure("left_frame.TFrame", background =BACKGROUND_COLOR)
        self.style.configure("right_frame.TFrame", background =BACKGROUND_COLOR)
        self.style.configure("orders_frame.TFrame", background =BACKGROUND_COLOR)
        self.style.configure("total_order_frame.TFrame", background =BACKGROUND_COLOR)
        self.style.configure("payment_frame.TFrame", background =BACKGROUND_COLOR)
        self.style.configure("search_frame.TFrame", background =BACKGROUND_COLOR)
        self.style.configure("menu_items_frame.TFrame", background =BACKGROUND_COLOR)
        self.style.configure("menu_title_frame.TFrame", background =BACKGROUND_COLOR)
        self.style.configure("menu_entry_frame.TFrame", background =BACKGROUND_COLOR)
        
        
        # Grid The Frames
#----------------------------------Left Side-------------------------------------------------------------------------#
        self.left_frame.grid(row=0, column=0, rowspan=3, sticky=tk.NSEW)
        self.search_frame.grid(row=0, column =0, sticky=tk.NSEW)
        self.orders_frame.grid(row=1, column =0, sticky=tk.NSEW)
        self.total_order_frame.grid(row =1 , column =0, columnspan=2, sticky=tk.NSEW)
        self.payment_frame.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW)

#-----------------------------------Right Side-----------------------------------------------------------------------#      
                
        self.right_frame.grid(row=0, column=1, rowspan=3, columnspan=2, sticky=tk.NSEW)
        self._title_frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.menu_entry_frame.grid(row=1, column = 0, sticky=tk.NSEW)
        self.menu_items_frame.grid(row=2, column =0, sticky=tk.NSEW)

        #Grid the widgets
        payment_button.grid(row=0, column =0, sticky="NSEW")
        clear_order_button.grid(row=0, column=1, sticky="NSEW")
        self.order_treeview.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=10)
        self.order_scrollbar.grid(row=0, column=1, sticky="ns", pady=10)
        self.confirm_checkbox.grid(row=0, column=2, sticky="NSEW")

        title.label.grid(row=0, column=0, columnspan=3, rowspan = 1, sticky=tk.NSEW)
        self.search_entry.grid(row=0, column=0, sticky="ew", padx=(10, 0), pady=(10, 10))
        self.search_button.grid(row=0, column=1, padx=(10, 0), pady=(10, 10))
    
    def show_allergens_popup(self, item_name):
        additional_items = self.menu.get_menu_allergen(item_name)

        if additional_items:
            allergen_info = "Allergen Name: {}\nAllergen ID: {}".format(
                additional_items['allergen_name'], additional_items['allergen_id']
            )
            # Use showinfo directly to display allergen information
            showinfo("Allergen Information for {}".format(item_name), allergen_info)
        else:
            # If no additional items are found, display an information message using showinfo
            showinfo("No Allergens", "{} has no additional items (allergens)".format(item_name))

    def preload_menu_images(self):
            menu_items = self.menu.get_menu_table()
            self.preloaded_images = {}

            for photo_url in menu_items['photo_url']:
                if pd.notna(photo_url):  # Check the URL
                    try:
                        response = requests.get(photo_url)
                        if response.status_code == 200:
                            img_data = Image.open(BytesIO(response.content))
                            img_data = img_data.convert("RGBA")
                            img_data = img_data.resize((64, 64), Image.Resampling.LANCZOS)
                            final_img = ImageTk.PhotoImage(img_data)
                            self.preloaded_images[photo_url] = final_img
                        else:
                            print(f"Failed to download image: {photo_url} with status code: {response.status_code}")
                    except Exception as e:
                        print(f"Error loading image from {photo_url}: {e}")
            self.display_menu_items()
#===================================

    def create_menu_item_row(self, parent_frame, menu_item):
        print(f"Creating row for menu item: {menu_item}")

        menu_item_id = menu_item[0]
        photo_url = menu_item[1]
        item_name = menu_item[2]
        description = menu_item[3]
        price = menu_item[4]
        stock_level = menu_item[5]


        # Frames, 
        item_frame = ttk.Frame(parent_frame)
        item_frame.grid(sticky=tk.EW)
        edit_button = ttk.Button(item_frame, text="Edit", command=lambda m=menu_item_id: self.edit_menu_item(m))
        edit_button.grid(row=2, column=4, sticky="NSEW")


        for a in range(3):
            item_frame.grid_columnconfigure(a, weight=1)
        for b in range(5):
            item_frame.grid_rowconfigure(b, weight=1)

        img_label = None
        photo = self.preloaded_images.get(photo_url, None)
        if photo:
            img_label = ttk.Label(item_frame, image=photo)
            img_label.image = photo
        else:
            img_label = ttk.Label(item_frame, text="Error") 


        # Widgets
        name_label = ttk.Label(item_frame, text=item_name, anchor="w", justify="center")
        desc_label = ttk.Label(item_frame, text=description, font=('Helvetica', 8), anchor="w", justify="center")
        price_label = ttk.Label(item_frame, text=f"£{price}", anchor="w", justify="center")
        allergens_button = ttk.Button(item_frame, text="View Allergens", command=lambda item_name=item_name: self.show_allergens_popup(item_name))
        order_button = ttk.Button(item_frame, text="Add to Order", command=lambda m=menu_item_id: self.add_to_order(item_name, price, m))
        stock_label = ttk.Label(item_frame, text=f"Stock: {stock_level}", anchor="w", justify="center")

        # Grid Widgets    
        img_label.grid(row=0, rowspan=3, column=0, sticky="NSEW")
        name_label.grid(row=1, column=1, sticky="NSEW")
        desc_label.grid(row=1, column=2, sticky="NSEW")
        price_label.grid(row=2, column=3, columnspan=2, sticky="NSEW")
        allergens_button.grid(row=0, column=3, sticky="NSEW")
        order_button.grid(row=0, column=4, sticky="NSEW")
        stock_label.grid(row=2, column=2, sticky="NSEW")
        edit_button.grid(row=2, column=4, sticky="NSEW")
   
    def search_menu_items(self):
        search_query = self.search_var.get().lower()

        all_menu_items = self.menu.get_all_menu_items()

        filtered_items = [item for item in all_menu_items if search_query in item[2].lower()]

        self.clear_menu_items_frame()
        self.display_filtered_menu_items(filtered_items)

    def display_filtered_menu_items(self, items):
        for widget in self.menu_items_frame.winfo_children():
            widget.destroy()

        for item in items:
            self.create_menu_item_row(self.menu_items_frame, item)
            
    def clear_menu_items_frame(self):
        # Destroy all widgets from the menu_items_frame.
        for widget in self.menu_items_frame.winfo_children():
            widget.destroy()

    def display_menu_items(self):
        menu_items = self.menu.get_all_menu_items()  # Fetch all menu items at once

        canvas = tk.Canvas(self.menu_items_frame)
        scrollbar = ttk.Scrollbar(self.menu_items_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        #Frame
        inner_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        def _on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        inner_frame.bind("<Configure>", _on_frame_configure)

        # Creates the item frames in the canvas instead
        for menu_item in menu_items:
            self.create_menu_item_row(inner_frame, menu_item)

        canvas.configure(scrollregion=canvas.bbox("all"))

    def add_to_order(self, item_name, price, menu_item_id):
        # Generate a unique internal ID
        unique_order_item_id = f"{menu_item_id}-{self.item_counter}"
        self.item_counter += 1

        self.order_treeview.insert("", "end", iid=unique_order_item_id, values=(item_name, f"£{price}"))

        self.order_items[unique_order_item_id] = {
            "menu_item_id": menu_item_id, 
            "price": price,
            "quantity": 1 
        }

    def on_treeview_item_click(self, event):
        selected_item = self.order_treeview.selection()
        if selected_item:
            unique_order_item_id = selected_item[0]

            self.order_treeview.delete(unique_order_item_id)

            if unique_order_item_id in self.order_items:
                del self.order_items[unique_order_item_id]

    
    def process_payment(self):
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        total_price = 0

        for order_item_id, item_details in self.order_items.items():
            menu_item_id = item_details["menu_item_id"]
            price = str(item_details["price"])
            
            total_price += float(item_details['price'])

            if self.checkbox_var.get() == 1: #Checks if "Discount" checkbox is clicked as yes. andsomehow put it into reservations. 
                discount = "STAFF20"
                price = str(float(price) * 0.8)
            else:
                discount = "NO_DISCOUNT"

            self.menu.insert_new_order(current_date, current_time, price, discount, menu_item_id, "PAID")
            
        showinfo("Payment successful!", f"Your total payment price is £{total_price}.")

        self.clear_order()

    def clear_order(self): #Gets and clears all inputs in treeview.
        self.order_treeview.delete(*self.order_treeview.get_children()) 
        self.order_items.clear()
        self.item_counter = 0


#--------------------------------------------------------------------------------------------#
    
    
    # def get_menu(self):
    #     """ Gets the menu and returns all items. """
    #     return
    
    # def get_item(self, item_name:str):
    #     """ Get an items data from menu. """
    #     return
    
    # def get_item_description(self, item_name:str):
    #     """ Get the description of a menu item. """
    #     return
    
    # def get_description_allergens(self):
    #     """ Get the allgerns of an item. """
    #     return
    
    # def get_selected_food_items(self, **args) -> dict: #search for itemsWWW
    #     return
    
    # def suggest_food_items(self):
    #     """ Arbitrarily suggest food to purchase. """
    #     return
    
    # def mark_items_as_unavailable(self):
    #     """ Update the menu item as unavailable. """
    #     return
    
    # def check_item_availability(self, item_name:str) -> int:
    #     """ Check the availablity of a menu item. """
    #     return self._inventory.check_inventory_stock(item_name)
    
    # def _set_item(self, item_name:str, description:str, photo_url:str = None):
    #     """ Private method for inserting a menu item. """
    #     return
    
    # def _set_item_description(self, description:str):
    #     """ Private method for inserting a menu item description. """
    #     return
    
    # def _set_item_price(self, price:float):
    #     """ Private method for inserting a menu item price. """
    #     return
    
    # def _delete_item(self, item_name:str):
    #     """ Private method for deleting a menu item. """
    #     return
    
    # def _set_category(self, category_name:str):
    #     """ Private method for inserting a menu item category. """
    #     return
    
    # def _update_category(self, category_name:str):
    #     """ Private method for updating a menu item category. """
    #     return

    # def _delete_category(self, category_name:str):
    #     """ Private method for deleting a menu item category. """
    #     return
