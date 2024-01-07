from client.interface import Interface
from client.interface.wm_screens import login, menu, payments, reports, reservations, kitchen, user_management
from client.settings import *
from client.interface.toolkits import headings
from client.errors import InvalidCredentialsError
from typing import Optional
from functools import partial
from server.sql.database import database
from tkinter import messagebox

import tkinter as tk
import tkinter.ttk as ttk

app_settings = {
    "title" : TITLE,
    "wm_resizable" : {
        "width": True,
        "height": True
    },
    "bg":'red'
}

class Main(object):
    def __init__(self, main_frame:ttk.Frame, xy_padding:bool = False):
        self.style = ttk.Style()
        
        # Toggle Relative Padding
        match (xy_padding):
            case True:
                self.padx = 3
                self.pady = 3
            case False:
                self.padx = 0
                self.pady = 0
        
        # Main Frame
        self.main_frame = main_frame
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        
        # Banner Frame
        self.banner_frame = ttk.Frame(self.main_frame, style="bannerframe.TFrame", name="bannerframe")
        self.banner_frame.grid_rowconfigure(0, weight=1)
        self.banner_frame.grid_rowconfigure(2, weight=1)
        self.banner_frame.grid_columnconfigure(0, weight=1)
        self.banner_frame.grid_columnconfigure(1, weight=1)
        self.banner_frame.grid_columnconfigure(2, weight=1)
        
        # Banner Nav Frame
        self.navigation_frame = ttk.Frame(self.banner_frame, style="navigation.TFrame", name="navigation")
        
        # Frame banner content
        self.lbl_title = headings.Heading6(self.banner_frame, text="Horizon Restaurants")
        self.lbl_branch_id = headings.TextLabel(self.banner_frame, text="")
        
        # Content frame to contain all navigation result elements
        self.content_frame = ttk.Frame(self.main_frame, style="content_frame.TFrame", name="content_frame")
        
        # Content frame grid
        self.content_frame.grid_rowconfigure(0, weight=0) # Title row
        self.content_frame.grid_rowconfigure(1, weight=1)
        self.content_frame.grid_rowconfigure(2, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=1)
        self.content_frame.grid_columnconfigure(2, weight=1)
        
        # Prevent the content frame from wrapping.
        self.content_frame.grid_propagate(False)
        
        # self.style.configure("main_frame.TFrame", background=BACKGROUND_COLOR)
        self.style.configure("bannerframe.TFrame", background=BACKGROUND_COLOR)
        self.style.configure("navigation.TFrame", background=BACKGROUND_COLOR)
        self.style.configure("content_frame.TFrame", background=BACKGROUND_COLOR)
        self.lbl_title.label.configure(background=BACKGROUND_COLOR, fg='#FFFFFF')
        self.lbl_branch_id.label.configure(background=BACKGROUND_COLOR, fg='#FFFFFF')
        
        # Display Main() frames with tkinter's grid manager
        self._display_frames()
    
    def destroy_frames(self, window: ttk.Frame | tk.Frame | tk.Widget | ttk.Widget):
        if type(window) == list:
            for item in window:
                if item != self.navigation_frame:  # Exclude navigation frame from destruction
                    item.destroy()
        else:
            if window != self.navigation_frame:  # Exclude navigation frame from destruction
                window.destroy()
            
    def forget_frames(self, window:ttk.Frame | tk.Frame | tk.Widget | ttk.Widget):
        # Check if the window is the banner_frame and skip removal
        # try:
        #     if window.winfo_name() == "bannerframe":
        #         return
        # except AttributeError:
        #     pass

        if type(window) == list:
            for item in window:
                item.grid_forget()
        else:
            window.grid_forget()
            
    def _display_frames(self):
        """ Displays the top level frame for any children to be displayed on. """
        
        # Display Banner Frame
        self.banner_frame.grid(row=0, column=0, columnspan=3, padx=self.padx, pady=self.pady, sticky=tk.EW)
        
        # Display Banner Content
        self.lbl_title.label.grid(row=0, column=0, sticky=tk.W)
        self.lbl_branch_id.label.grid(row=1, column=0, sticky=tk.W)
        
        # Display Navigation
        self.navigation_frame.grid(row=0, column=1, columnspan=2, rowspan=2, padx=3, pady=12, sticky=tk.NSEW)
        
        # Display Main Content Frame
        self.content_frame.grid(row=1, column=0, columnspan=3, padx=self.padx, pady=self.pady, sticky=tk.NSEW)
    
    def create_navbar(self, branch_role):
        """Creates a navbar from a list of button names. """
        nav_buttons = []
        nav_button_obj_list = []
        
        match(branch_role):
            case 1: # Staff
                nav_buttons = ["Menu", "Logout"]
            case 2: # Chef
                nav_buttons = ["Menu", "Kitchen", "Logout"]
            case 3: # Manager
                nav_buttons = ["Menu", "Reservations", "Kitchen", "Reports", "Logout"]
            case 4: # Admin
                nav_buttons = ["Menu", "Reservations", "Kitchen", "Reports", "User Management", "Logout"]
            case 5: # HR Director
                nav_buttons = ["Reports", "Logout"]
            case _: # Unknown
                nav_buttons = ["Menu", "Logout"]
                
        # Remove navbar buttons if there is only logout and the existing page/frame.
        # nav_buttons_length = len(nav_buttons)    
        # if nav_buttons_length == 2:
        #     del nav_buttons[nav_buttons_length-2]
        
        # Create the button objects using the configured navbar list
        for i in range(len(nav_buttons)):
            button_name = nav_buttons[i].lower()
            button = tk.Button(
                self.navigation_frame,
                text=nav_buttons[i],
                # width=100 // nav_buttons_length,
                width=100 // len(nav_buttons),
                name=button_name,
                padx=self.padx,
                pady=self.pady
            )
            nav_button_obj_list.append(button)
            
        # Check if the logout button is in button name and make it a 'danger' color
        # This gives UX a peace of mind.
        if "logout" == nav_buttons[i].lower():
            button.configure(background='#FF5252', activebackground='#FF5252')

        return nav_button_obj_list
        
    def del_navbar_button(self, nav_button:str):
        """ Deletes a navigation button from a button set via string type. """
        return
    
    def add_navbar_button(self, nav_button:dict):
        """Add a new or previously existing navigation button via hashmap."""
        return
    
    def display_navbar_buttons(self, nav_buttons:list):
        """ Display the top level frame navigation bar based on the hierarchical priority of the user. """
                
        self.destroy_frames(self.navigation_frame)
        # Get the child of the main frame
        content_frame_name = self.content_frame.winfo_name()
        content_frame_children = self.content_frame.winfo_children()
        
        self.navigation_frame.grid_rowconfigure(0, weight=1)
        self.navigation_frame.grid_columnconfigure(0, weight=1)
        
        # If 0, then frame is empty, resort to default nav.
        # The other option is to get next content frame children as a baseline
        # so we know which navigation items to display.
        # for i in range(len(nav_buttons)):
            
        #         # If empty, create default navbar based on user access.
        #         if len(content_frame_children) == 0:
        #             self.style.configure(nav_buttons[i].winfo_name())
        #             nav_buttons[i].grid(row=0, column=i, sticky=tk.NS+tk.E)
        
        
        # ---------------------------------------------------------------------------------#
        # Remove later. This is a test to see if the navbar displays after updating a frame.
        for i in range(len(nav_buttons)):
            self.style.configure(nav_buttons[i].winfo_name())
            nav_buttons[i].grid(row=0, column=i, sticky=tk.NS+tk.E)
        # ---------------------------------------------------------------------------------#

        
    def get_current_frames(self):
        """Gets all the current active frames of a paginated section. """
        
        return self.content_frame.winfo_children()

    
class Application(object):
    def __init__(self, **args):
        
        # Configure the master interface
        self.main = Interface(**args)
        self.main.master.propagate(False)
        self.main.master.configure(width=INITIAL_WIDTH, height=INITIAL_HEIGHT, bg=BACKGROUND_COLOR)
        self.main.master.minsize(width=INITIAL_WIDTH, height=INITIAL_HEIGHT)
        
        # Allow the application to become expandable on the top level.
        self.main.master.grid_rowconfigure(0, weight=1)
        self.main.master.grid_columnconfigure(0, weight=1)
        
        # Add styling
        self.style = ttk.Style()
        
        # Add a main frame to master
        main_frame = ttk.Frame(self.main.master, style='main_frame.TFrame', name="main_frame", width=self.main.master.winfo_reqwidth(), height=self.main.master.winfo_reqheight())
        main_frame.grid(row=0, column=0, sticky=tk.NSEW)      
        
        # Main Window
        self.main_window = Main(main_frame)
        
        # Sub Windows
        self.login_interface = login.Login(self.main_window)
        self.menu_interface = menu.Menu(self.main_window)
        self.home_frame = ttk.Frame(self.main_window.content_frame, style="home_frame.TFrame", name="home_frame")
        self.home_welcome = headings.Heading1(self.home_frame)
        self.home_info = headings.TextLabel(self.home_frame)
        self.kitchen_interface = kitchen.Kitchen(self.main_window)
        self.user_management = user_management.UserManagement(self.main_window)
        self.reservations = reservations.Reservations(self.main_window)
        
        # Lowest level of staff
        self.staff = login.Staff()
        
        self.login_buttons = self.login_interface.create_login_buttons_2d_list()
        self.display_login()
        
    def display_home(self):
        """Display a template home page for the user after login. """
        
        self.style.configure("home_frame.TFrame", background=BACKGROUND_COLOR)
        self.home_frame.grid_rowconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(1, weight=1)
        self.home_frame.grid_columnconfigure(0, weight=1)
        # self.home_frame.grid_columnconfigure(1, weight=1)
        self.home_frame.grid(row=0, column=1, rowspan=3, sticky=tk.NSEW)
        
        # Home label heading
        self.home_welcome.label.configure(bg=BACKGROUND_COLOR, fg='#FFFFFF', text=f"Welcome {self.staff.first_name.get()}!")
        self.home_welcome.label.grid(row=0, column=0, sticky=tk.S)

        # Home label staff id
        self.home_info.label.configure(bg=BACKGROUND_COLOR, fg='#FFFFFF', text=f"POS Management System. \nYour Personal Staff ID: {self.staff.staff_id.get()}.")
        self.home_info.label.grid(row=1, column=0, sticky=tk.N)
        
    def display_navbar(self):
        # Create and display navbar
        self.navbar = self.main_window.create_navbar(branch_role=self.staff.branch_role.get())
        self.main_window.display_navbar_buttons(nav_buttons=self.navbar)
        
        # Logout button
        logout_button_int = -1
        self.navbar[logout_button_int].bind("<Button>", func=lambda _: (
            # Forget (all) previous frames to display a new frame object.
            self.main_window.forget_frames(self.main_window.content_frame.winfo_children()),
            self.main_window.forget_frames(self.main_window.navigation_frame.winfo_children()),
            
            # Empty branch ID on logout
            self.main_window.lbl_branch_id.label.configure(text = ""),
            
            # Display the login page
            self.display_login()
            )
        )
        
        # Bind every navbar button to their respective display function.
        for button in range(len(self.navbar)+logout_button_int):
            button_name = self.navbar[button].cget('text').lower().replace(' ', '_')            
            display_page = getattr(self, f"display_{button_name}")
            self.navbar[button].bind("<Button>", func=lambda _, page=display_page: ( 
                self.main_window.forget_frames(self.main_window.content_frame.winfo_children()),
                page(),
                
                # Show which frames are currently active on the screen
                # print("\n***ACTIVE FRAMES ***"),
                # print(frame.winfo_ismapped() for frame in self.main_window.main_frame.winfo_children()),
            ))
        
    def display_login(self):
        """Top most level function to display the login page. """
        
        def _create_btn_callbacks():
            """Internal nested callback function. """
            for row in range(len(self.login_buttons)):
                for col in range(len(self.login_buttons[row])):
                    if self.login_interface.buttons[row][col].cget('text') != "Login":
                        if self.login_interface.buttons[row][col].cget('text') == "<<":
                            self.login_interface.buttons[row][col].configure(
                                command=lambda: self.login_interface._input_box.on_tbx_delete(self.login_interface._input_box.input_box)
                            )
                        else:
                            self.login_interface.buttons[row][col].configure(
                                command=lambda x=str(self.login_interface.buttons[row][col].cget("text")): self.login_interface._input_box.on_tbx_insert(self.login_interface._input_box.input_box, x)
                            )
                        
                    elif self.login_interface.buttons[row][col].cget('text') == "Login":
                        self.login_interface.buttons[row][col].configure(
                            command=lambda: (
                                # Configure staff object and update branch id.
                                self.staff.init_staff(staff_id = self.login_interface._input_box.input_box.get()),
                                self.main_window.lbl_branch_id.label.configure(text=f"HR Branch ID: {self.staff.branch_id.get()}"),
                                self.login_interface._input_box.on_tbx_delete(self.login_interface._input_box.input_box),
                                
                                # Display the home page + navbar if accessed is granted other return to login page.
                                ((self.display_navbar(),self.display_home()) 
                                if self.login_interface.check_access_rights(branch_role=self.staff.branch_role.get(), staff_id=self.staff.staff_id.get()) == True else self.display_login())
                            )
                            if self.login_interface.login(staff_id=self.login_interface._input_box.input_box.get()) == True else False
                        )

            self.login_interface.display_frames()  
            self.login_interface.display_login_buttons(self.login_buttons)
    
        try:
            _create_btn_callbacks()
            
        except AttributeError:
            # If this error is raised it means the program cannot find the created button objects
            # therefore it resorted back to the default buttons names list causing tkinter attribute error.
            # This is easily fixed by catching the error and re-intialising self.login_buttons to its original state.
            self.login_buttons = self.login_interface.create_login_buttons_2d_list()
            _create_btn_callbacks()
            
    def display_menu(self):
        """Top most level function to display the menu page. """
        
        
        # Create a new Login instance in the case that the previous has been destroyed, forgotten, or removed by tkinter.
        self.login_interface = login.Login(self.main_window)
        # Display the menu frames
        self.menu_interface.display_frames()
        
    def display_reservations(self):
        # self.reservations.display_frames()
        self.reservations.display_frames()
    
    def display_kitchen(self):
        """Top most level function to display the kitchen/order overview page. """
        
        # Delete pre-existing orders
        self.kitchen_interface.unpopulate_orders_display()
        
        # Create a new kitchen interface.
        order_management_buttons = self.kitchen_interface.create_management_buttons()
        self.kitchen_interface.display_management_buttons(order_management_buttons)
        self.kitchen_interface.create_dynamic_headings()
        self.kitchen_interface.display_frames()
        
        
        return
    
    def display_reports(self):
        # self.reports_interface.btn_dict.get("KEY").bind("<Button>", func=lambda _: ((cmd1), (cmd2), if x == y else ""))
        return
    
    def display_user_management(self):
        """Top most level function to display the user management overview page. """
        
        self.user_management.btn_create_account.bind("<Button>", func=lambda _: (
            self.user_management.create_user_account()
        ))
        
        self.user_management.btn_delete_account.configure(command=lambda: self.user_management.delete_user_account())
        
        self.user_management.display_frames()


if __name__ == '__main__':
    
    # Initialise the entire application and mapped settings
    app = Application(**app_settings)
    
    # Add any new settings after initialisation like below:
    # main_window.settings['SETTING_NAME'] = SETTING_VALUE
    
    # Run the tkinter event loop to control continuity
    app.main.master.mainloop()