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
from tkinter import simpledialog
import tkinter.ttk as ttk
import tkinter as tk

class Menu(object):
    def __init__(self, parent):
        """ Construct a tkinter frame for Menu. """
        self._inventory = Inventory()
        self.parent = parent
        self.style = ttk.Style()
        self.configure_style()

    def configure_style(self):

        frame_width = self.parent.content_frame.winfo_reqwidth()

        #self.style.configure("Binayam.TLabel", foreground="black", background = "black", font=("Helvetica", 12))
        #button = ttk.Button(root, text="Binayam", style="Binayam.TButton")
        self.style.configure("Binayam.TLabel", foreground="blue", background="black", font=("Helvetica", 12, "italic"), borderwidth=frame_width, relief="solid", bordercolor="red")

        self.btn_dict = {}
        
    def display(self):
        if str(type(self.parent)) == "<class '__main__.Main'>":
            self.parent.style.configure("self.parent.content_frame.TFrame", background=BACKGROUND_COLOR, bd=1, relief=tk.SOLID)
            # self.parent.content_frame.grid(row=0, column=0, sticky=tk.NSEW)
            # self.parent.content_frame.grid_rowconfigure(0, weight=1)
            # self.parent.content_frame.grid_rowconfigure(1, weight=1)
            # self.parent.content_frame.grid_rowconfigure(2, weight=1)
            # self.parent.content_frame.grid_columnconfigure(0, weight=1)

            menu_title_frame = ttk.Frame(self.parent.content_frame)
            menu_title_frame.grid(row=0, column=1)
            menu_title_frame.grid_rowconfigure(0, weight=1)
            menu_title_frame.grid_rowconfigure(1, weight=1)
            menu_title_frame.grid_rowconfigure(2, weight=2)

            menu_search_frame = ttk.Frame(self.parent.content_frame)
            menu_search_frame.grid(row=1, column=0)

            menu_tree_frame = ttk.Frame(self.parent.content_frame)
            menu_tree_frame.grid(row=2, column=0)

            search_label = ttk.Label(menu_search_frame, text="Search", style = "Binayam.TLabel")
            search_label.grid(row=0, column=0, padx=10, pady=10)
            search_label.bind("<Button>", self._query_menu_items)

            # menu_label = ttk.Label(menu_title_frame, text="Menu", background="black", foreground="white",font=("Helvetica", int(self.parent.content_frame.winfo_reqheight() * 0.1), "bold"))
            # menu_label.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)
            # menu_label.configure(anchor="center")

            menu_label = headings.Heading6(menu_title_frame, text="Menu")
            menu_label.label.configure(bg="#1e1e1e", fg='white') # Add dark theme
            # menu_label.label.pack(side="top", fill="both", expand=True)
            menu_label.label.grid(row=0, column=0, sticky=tk.NSEW)

            # binayam_label= ttk.Label(menu_tree_frame, text="Binayam")
            # binayam_label.grid(row=0, column = 0)

            menu_tree = ttk.Treeview(menu_tree_frame, columns=("Items","Description"), show="headings")
            menu_tree.grid(row=0, column=0, sticky="NSEW")
            
            for i in range(len(menu_tree["columns"])):
                menu_tree.column(menu_tree["columns"][i], width=(100))
            
            menu_tree.heading("Items", text="Items")
            menu_tree.heading("Description", text = "Description")

            for i in range(1, 26):
                item = f"Item {i}"
                description = f"Description {i}"
                menu_tree.insert("", "end", values=(item,))

            scrollbar = ttk.Scrollbar(menu_tree_frame, orient="vertical", command=menu_tree.yview)
            scrollbar.grid(row=0, column=1, sticky="NS")

            menu_tree.configure(yscrollcommand=scrollbar.set)

        return
    
    def _query_menu_items(self, event):
        """Internal function. Search box for menu items. """
        search_query = simpledialog.askstring("Menu Items", "SEARCH")
        if search_query is not None:
            print(f"Menu: {search_query}")
        
    def hide(self):
        self.parent.content_frame.forget()
    
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