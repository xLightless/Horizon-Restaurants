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
from server.sql.database import database
# from server.sql.database import Database
from PIL import Image, ImageTk
import requests
from io import BytesIO
import tkinter.ttk as ttk
import tkinter as tk

class Menu(object):
    def __init__(self, parent):
        """ Construct a tkinter frame for Menu. """
        # self._inventory = Inventory()
        self.parent = parent
        self.style = ttk.Style()
        
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
        self.menu_items_frame = ttk.Frame(self.right_frame, style="menu_items_frame.TFrame", name="menu_items_frame")
        self.menu_items_frame.bind("<Configure>", lambda e: self.update_scroll_region())

        self.menu_captions_frame = ttk.Frame(self.right_frame, style="menu_captions_frame.TFrame", name="menu_captions_frame")
        

        self.menu_items_canvas = tk.Canvas(self.right_frame, bg=BACKGROUND_COLOR)
        self.menu_items_scrollbar = ttk.Scrollbar(self.right_frame, orient="vertical", command=self.menu_items_canvas.yview)
        self.menu_items_canvas.configure(yscrollcommand=self.menu_items_scrollbar.set)
        self.menu_items_frame = ttk.Frame(self.menu_items_canvas)
        self.menu_items_canvas.create_window((0, 0), window=self.menu_items_frame, anchor="nw") #tk is not capital letters

        # self.display_menu_items() # Function to display menu items by repeating create_menu_item_row for number of rows in the table.
        #self. 
        
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
        self.orders_frame.grid_rowconfigure(1, weight=1)
        self.orders_frame.grid_rowconfigure(2, weight = 6)
        self.orders_frame.grid_columnconfigure(0, weight=1)
        self.orders_frame.grid_columnconfigure(1, weight=1)
       
        # Right Side / Menu Frame
        self.right_frame.grid_rowconfigure(0, weight=0)
        self.right_frame.grid_rowconfigure(1, weight=0)
        self.right_frame.grid_rowconfigure(2, weight=10)
        self.right_frame.grid_columnconfigure(0, weight=9)
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
        self.style.configure("search_frame.TFrame", background = "blue")
        self.style.configure("menu_items_frame.TFrame")
        self.style.configure("menu_title_frame.TFrame", borderwidth=1, relief="solid")
        self.style.configure("menu_captions_frame.TFrame", borderwidth=1, relief="solid")
        # Grid The Frames
#----------------------------------Left Side-------------------------------------------------------------------------#
        self.left_frame.grid(row=0, column=0, rowspan=3, sticky=tk.NSEW)
        self.search_frame.grid(row=0, column =0, sticky=tk.NSEW)
        self.orders_frame.grid(row=1, column =0, sticky=tk.NSEW)

#-----------------------------------Right Side-----------------------------------------------------------------------#      

        self.right_frame.grid(row=0, column=1, rowspan=3, columnspan=2, sticky=tk.NSEW)
        self._title_frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.menu_captions_frame.grid(row=1, column = 0, sticky=tk.NSEW)
        self.menu_items_frame.grid(row=2, column =0, sticky=tk.NSEW)

        self.menu_items_canvas.grid(row=2, column=0, sticky=tk.NSEW)
        self.menu_items_scrollbar.grid(row=2, column=1, sticky=tk.NSEW)

        #Grid the widgets
        title.label.grid(row=0, column=0, columnspan=3, rowspan = 1, sticky=tk.NSEW)
        image_caption.label.grid(row=0, column=0, sticky=tk.NSEW)
        item_name_caption.label.grid(row=0, column=1, sticky=tk.NSEW)
        item_description_caption.label.grid(row=0, column=2, sticky=tk.NSEW)
        button_caption.label.grid(row=0, column=3, columnspan=2, sticky=tk.NSEW)

    def create_menu_item_row(self, parent_frame, database, row_number): # self is referring to a instance of menu class   
        menu_item = database.get_table_record("menu_items", row_number) # uses function from database.py to use "row_number" variable as index
        
        # Hacking the main database  
        photo_url, item_name, description, price = menu_item[1], menu_item[2], menu_item[3], menu_item[4]
        
        #Frames
        item_frame = ttk.Frame(parent_frame)
        item_frame.grid(row=row_number, column=0, sticky=tk.EW)

        #Grid Configurations

        for a in range(3):
            item_frame.grid_columnconfigure(a, weight=1)
        for b in range(5):
            item_frame.grid_rowconfigure(b, weight=1)


        #--------StackOF-------# 
        # if photo_url and photo_url.startswith(('http://', 'https://')): # Exception handling mechanism
        #     try:
        #         response = requests.get(photo_url)
        #         response.raise_for_status()  # Error checker
        #         img_data = Image.open(BytesIO(response.content))
        #     except Exception as e:
        #         print(f"Error fetching image from {photo_url}: {e}")
        #         img_data = Image.open("C:\\Users\\grgbi\\OneDrive\\Desktop\\Horizon_Restaurants\\chicken.jpg")#Load the chicken c:
        # else:
        #     # Load a default image if photo_url is None or not a valid URL
        #     img_data = Image.open("C:\\Users\\grgbi\\OneDrive\\Desktop\\Horizon_Restaurants\\chicken.jpg")

        # img_data = img_data.resize((100, 100), Image.Resampling.LANCZOS)
        #------------------#
        
        if photo_url is not None:
            response = requests.get(photo_url) # HTTP Get request to URL
            img_data = Image.open(BytesIO(response.content)) # "response.content" is byte data so creates images frmo bytes
        else:
            img_data = Image.new("RGB", (800, 1280), (255, 255, 255))
            
        img_data = img_data.resize((64, 64), Image.Resampling.LANCZOS) # resizes, use LANCZOS instead of ANTIALIAS for some reason, newer version uses LANCZOS
        photo = ImageTk.PhotoImage(img_data) #===============================================#
        img_label = ttk.Label(item_frame, image=photo) # Can't move this or wont access     #                                 
        img_label.image = photo  #Very important step, fixes the whole image displaying code#
        
        # Widgets
        name_label = ttk.Label(item_frame, text=item_name, anchor="w", justify="center")
        desc_label = ttk.Label(item_frame, text=description, font=('Helvetica', 8), anchor="w", justify="center")
        price_label = ttk.Label(item_frame, text=f"£{price}", anchor="w", justify="center")
        allergens_button = ttk.Button(item_frame, text="View Allergens")
        order_button = ttk.Button(item_frame, text="Add to Order")

        # Grid Widgets        
        img_label.grid(row=0, rowspan=3, column=0, sticky="NSEW")
        name_label.grid(row=1, column=1, sticky="NSEW")
        desc_label.grid(row=1, column=2, sticky="NSEW")
        price_label.grid(row=2, column=3, columnspan=2, sticky="NSEW")
        allergens_button.grid(row=0, rowspan=2, column=3, sticky="NSEW")
        order_button.grid(row=0, rowspan=2, column=4, sticky="NSEW")


    def display_menu_items(self):
        # database = Database(database="horizon_restaurants")
        num_rows = database.count_table_rows("menu_items")
        for row_number in range(num_rows):
            self.create_menu_item_row(self.menu_items_frame, database, row_number)
        
        self.menu_items_frame.update_idletasks()  # Update the frame's size
        self.menu_items_canvas.config(scrollregion=self.menu_items_canvas.bbox("all"))
        
        self.update_scroll_region()


    def update_scroll_region(self):
        self.menu_items_canvas.config(scrollregion=self.menu_items_canvas.bbox("all"))


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
    
    def get_selected_food_items(self, **args) -> dict: #search for itemsWWW
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