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
        self.menu_captions_frame = ttk.Frame(self.right_frame, style="menu_captions_frame.TFrame", name="menu_captions_frame")
        self.menu_items_frame = ttk.Frame(self.right_frame, style="menu_items_frame.TFrame", name="menu_items_frame")
        
        self.item_counter = 0 #Big Brain moment, interal id to replace as order_item_id when payment is clicked
        self.order_items = {} # Dictionary to track each orders details in treeview

        self.preload_menu_images()
        self.display_menu_items()
        
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

        self.menu_captions_frame.grid_columnconfigure(0, weight = 1)
        self.menu_captions_frame.grid_columnconfigure(1, weight = 1)
        self.menu_captions_frame.grid_columnconfigure(2, weight = 1)
        self.menu_captions_frame.grid_columnconfigure(3, weight = 1)
        self.menu_captions_frame.grid_columnconfigure(4, weight = 1)

        self.menu_items_frame.grid_columnconfigure(0, weight=1)
        self.menu_items_frame.grid_rowconfigure(0, weight = 1)

        # Widgets
        title = headings.Heading6(self._title_frame, text="Menu Items")
        image_caption = headings.Heading6(self.menu_captions_frame, text="Image")
        item_name_caption = headings.Heading6(self.menu_captions_frame, text="Item Name") 
        item_description_caption = headings.Heading6(self.menu_captions_frame, text="Description")
        button_caption = headings.Heading6(self.menu_captions_frame, text="Buttons")

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
        image_caption.label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")
        item_name_caption.label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")
        item_description_caption.label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")
        button_caption.label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")

        # Styling for frames
        self.style.configure("left_frame.TFrame")
        self.style.configure("right_frame.TFrame")
        self.style.configure("orders_frame.TFrame", background = "red")
        self.style.configure("total_order_frame.TFrame", background = "yellow")
        self.style.configure("payment_frame.TFrame", background = "purple")
        self.style.configure("search_frame.TFrame", background = "blue")
        self.style.configure("menu_items_frame.TFrame")
        self.style.configure("menu_title_frame.TFrame", borderwidth=1, relief="solid")
        self.style.configure("menu_captions_frame.TFrame", borderwidth=1, relief="solid")
        
        
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
        self.menu_captions_frame.grid(row=1, column = 0, sticky=tk.NSEW)
        self.menu_items_frame.grid(row=2, column =0, sticky=tk.NSEW)

        #Grid the widgets
        payment_button.grid(row=0, column =0, sticky="NSEW")
        clear_order_button.grid(row=0, column=1, sticky="NSEW")
        self.order_treeview.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=10)
        self.order_scrollbar.grid(row=0, column=1, sticky="ns", pady=10)
        self.confirm_checkbox.grid(row=0, column=2, sticky="NSEW")

        title.label.grid(row=0, column=0, columnspan=3, rowspan = 1, sticky=tk.NSEW)
        image_caption.label.grid(row=0, column=0, sticky=tk.NSEW)
        item_name_caption.label.grid(row=0, column=1, sticky=tk.NSEW)
        item_description_caption.label.grid(row=0, column=2, sticky=tk.NSEW)
        button_caption.label.grid(row=0, column=3, columnspan=2, sticky=tk.NSEW)

    def preload_menu_images(self):
        menu_items = self.menu.get_menu_table()
        self.preloaded_images = {}

        for item in menu_items:
            photo_url = item[1] 
            if photo_url:
                try:
                    response = requests.get(photo_url)
                    img_data = Image.open(BytesIO(response.content))
                    img_data = img_data.resize((64, 64), Image.Resampling.LANCZOS)
                    self.preloaded_images[photo_url] = ImageTk.PhotoImage(img_data)
                except Exception as e:
                    print(f"Error loading image from {photo_url}: {e}")
    

    def create_menu_item_row(self, parent_frame, menu_item):
        menu_item_id = menu_item[0]
        photo_url = menu_item[1]
        item_name = menu_item[2]
        description = menu_item[3]
        price = menu_item[4]

        # Frames, 
        item_frame = ttk.Frame(parent_frame)
        item_frame.grid(sticky=tk.EW)

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
        allergens_button = ttk.Button(item_frame, text="View Allergens")
        order_button = ttk.Button(item_frame, text="Add to Order", command=lambda m=menu_item_id: self.add_to_order(item_name, price, m))

        # Grid Widgets        
        img_label.grid(row=0, rowspan=3, column=0, sticky="NSEW")
        name_label.grid(row=1, column=1, sticky="NSEW")
        desc_label.grid(row=1, column=2, sticky="NSEW")
        price_label.grid(row=2, column=3, columnspan=2, sticky="NSEW")
        allergens_button.grid(row=0, rowspan=2, column=3, sticky="NSEW")
        order_button.grid(row=0, rowspan=2, column=4, sticky="NSEW")


    def display_menu_items(self):
        menu_items = self.menu.get_all_menu_items()  # Fetch all menu items at once
        for menu_item in menu_items:
            self.create_menu_item_row(self.menu_items_frame, menu_item)

    def add_to_order(self, item_name, price, menu_item_id):
        order_item_id = self.item_counter
        self.item_counter += 1

        self.order_treeview.insert("", "end", iid=order_item_id, values=(item_name, f"£{price}"))
        self.order_items[order_item_id] = {
            "menu_item_id": menu_item_id,  # No longer a list, just a single ID
            "item_name": item_name,
            "price": price
        }

    def on_treeview_item_click(self, event):
        doubleselected_item = self.order_treeview.selection() #Selection used to return the interal id of the clicked treeview item

        if doubleselected_item: 
            internal_id = doubleselected_item[0] # Picks the unique id 
            self.order_treeview.delete(internal_id)

            if internal_id in self.order_items: #Checks if its actually the one selected
                del self.order_items[internal_id]
    
    def process_payment(self):
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        for order_item_id, item_details in self.order_items.items():
            menu_item_id = item_details["menu_item_id"]
            price = str(item_details["price"])

            if self.checkbox_var.get() == 1: #Checks if "Discount" checkbox is clicked as yes.
                discount = "STAFF20"
                price = str(float(price) * 0.8)
            else:
                discount = "NO_DISCOUNT"

            self.menu.insert_new_order(current_date, current_time, price, discount, menu_item_id, "PAID")

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
