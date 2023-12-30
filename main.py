from client.interface import Interface
from client.interface.wm_screens import home, login
from client.settings import *
from client.interface.toolkits import headings
from typing import Optional

from server.sql.database import Database

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
    def __init__(self, parent):
        self.style = ttk.Style()
        self.stringVar = tk.StringVar()

        # Banner frame and widgets
        self.frame_banner_1 = ttk.Frame(parent, style="bannerFrame.TFrame")
        self.frame_banner_1.grid(row=0, column=0, sticky=tk.EW, columnspan=3, padx=3, pady=3)
        self.frame_banner_1.grid_rowconfigure(0, weight=1)
        self.frame_banner_1.grid_rowconfigure(2, weight=1)
        self.frame_banner_1.grid_columnconfigure(0, weight=1)
        self.frame_banner_1.grid_columnconfigure(2, weight=1)

        # Some spacing/other options
        self.frame_content_1 = ttk.Frame(parent, style="frame_content_1.TFrame", width=100 // MAIN_GRID_BOXES)
        self.frame_content_1.grid(row=1, column=0, sticky=tk.NSEW, padx=3, pady=3)
        self.frame_content_1.grid_rowconfigure(0, weight=1)
        self.frame_content_1.grid_columnconfigure(0, weight=1)
        
        # Number pad
        self.frame_content_2 = ttk.Frame(parent, style="frame_content_2.TFrame", width=100 // MAIN_GRID_BOXES)
        self.frame_content_2.grid(row=1, column=1, sticky=tk.NSEW, padx=3, pady=3)
        self.frame_content_2.grid_rowconfigure(0, weight=1)
        self.frame_content_2.grid_columnconfigure(0, weight=1)

        # Some spacing/other options
        self.frame_content_3 = ttk.Frame(parent, style="frame_content_3.TFrame", width=100 // MAIN_GRID_BOXES)
        self.frame_content_3.grid(row=1, column=2, sticky=tk.NSEW, padx=3, pady=3)
        self.frame_content_3.grid_rowconfigure(0, weight=1)
        self.frame_content_3.grid_columnconfigure(0, weight=1)
        
        self.containers = [self.frame_content_1, self.frame_content_2, self.frame_content_3]

        # Frame banner content
        self.lbl_title = headings.Heading6(self.frame_banner_1, text="Horizon Restaurants")
        self.lbl_title.label.grid(row=0, column=0, sticky=tk.W)
        
        self.lbl_branch_id = headings.TextLabel(self.frame_banner_1, text="Branch ID: 123677")
        self.lbl_branch_id.label.grid(row=1, column=0, sticky=tk.W)


        # Configure columns and rows to expand horizontally and vertically
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_columnconfigure(2, weight=1)
        
        # Update vertical expansion due to row 0 elements not requiring it.
        # Make the next row expandable.
        parent.grid_rowconfigure(0, weight=0)
        parent.grid_rowconfigure(1, weight=1)

        # Style all elements
        self.style.configure("bannerFrame.TFrame", background=BACKGROUND_COLOR)
        self.lbl_title.label.configure(background=BACKGROUND_COLOR, fg='#FFFFFF')
        self.lbl_branch_id.label.configure(background=BACKGROUND_COLOR, fg='#FFFFFF')
        self.style.configure("frame_content_1.TFrame", background=BACKGROUND_COLOR)
        self.style.configure("frame_content_2.TFrame", background='yellow')
        self.style.configure("frame_content_3.TFrame", background=BACKGROUND_COLOR)
        
        print(self.frame_banner_1.winfo_children())
        
        
    def display_navbar(self, staff_role):
        OFFSET_LOGOUT_BTN = -1
        
        self.lbl_title.label.grid(row=0, column=0, columnspan=2, rowspan=1,sticky=tk.W)
        self.lbl_branch_id.label.grid(row=1, column=0, columnspan=2, rowspan=1,sticky=tk.W)
        
        # # Create a child frame inside the banner, give it a grid row/col then update.
        btn_frame = tk.Frame(self.frame_banner_1, background=BACKGROUND_COLOR)
        btn_frame.grid(row=0, column=2, rowspan=2, columnspan=2, sticky=tk.NSEW, padx=16, pady=16)
        
        # Create a button and place it on the child frame.
        buttons = []
        btn_dict = {}
        
        if staff_role >= 5:
            buttons = ["Reports", "Inventory", "Events"]
            
        
        # Insert a prefix button Home and a suffix button logout.
        buttons.insert(0, "Home")
        buttons.insert(len(buttons), "Logout")
        
        # Configure rows and columns for the navbar so that it considers all new buttons
        btn_frame.grid_rowconfigure(0, weight=1)
        btn_frame.grid_rowconfigure(2, weight=1)
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(len(buttons)+OFFSET_LOGOUT_BTN, weight=1)
            
        # Navigation Bar buttons
        for i in range(len(buttons)):
            btn = tk.Button(btn_frame, text=buttons[i], width=100 // len(buttons))
            btn.grid(row=0, column=i, sticky=tk.NE, padx=3)
            btn_dict[buttons[i]] = btn
            
        # Logout button. Make it obvious.
        btn_dict['Logout'].configure(background='#d9534f', command=lambda: exit())
        
            
        # Seperately destroy children containers rather than main_window.containers to prevent it removing top level sub frames.
        # Using this function will destory any elements that were previously binded to these container frames.
        self.destroy_window_children(self.containers[0]),
        self.destroy_window_children(self.containers[1]),
        self.destroy_window_children(self.containers[2]),
        
        return btn_dict
        
    def destroy_window_children(self, window:list | tk.Frame | ttk.Frame):
        """Destroy all child elements of a main tkinter Frame. """
        
        if isinstance(window, list):
            for i in range(len(window)):
                child = window[i].winfo_children()
                if len(child) != 0:
                    for j in range(len(child)):
                        child[j].destroy()
                        
                ## Not quite sure about this one therefore its temporary.
                # if len(child) == 0:
                #     child[j].destroy()
            return
        window.destroy()
        
    def display_window_children(self, window):
        return window.display()

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
        main_frame = ttk.Frame(self.main.master, style='main_frame.TFrame', width=self.main.master.winfo_reqwidth(), height=self.main.master.winfo_reqheight())
        main_frame.grid(row=0, column=0, sticky=tk.NSEW)        
        # style.configure("main_frame.TFrame", background=BACKGROUND_COLOR, bd=1, relief=tk.SOLID)
        
        # The first screen and fall back screen when all gets destroyed
        main_window = Main(main_frame)
        
        # Login (Logged in to system)
        login_interface = login.Login(main_window)
        login_interface.display()
        
        # Login (Not logged in to system)
        buttons = login_interface.main_frame.winfo_children()[2].winfo_children()
        login_button = len(buttons)-3
        backspace_button = len(buttons)-1
        
        # Login number keys
        for row in range(len(login_interface.main_frame.winfo_children())):
            for col in range(len(login_interface.main_frame.winfo_children()[row].winfo_children())):
                btn = login_interface.main_frame.winfo_children()[row].winfo_children()[col]
                if '!button' in btn.winfo_name():
                    if (btn.cget("text") != "Login") and (btn.cget("text") != "<<"):
                        btn.configure(command=lambda x=str(btn.cget("text")): login_interface.on_tbx_insert(login_interface.input_box.input_box, x))

        # Login commands
        buttons[login_button].configure(command=lambda: (login_interface.login(login_interface.input_box.input_box.get()), main_window.display_navbar(login_interface.staff_role)))     
        buttons[backspace_button].configure(command=lambda: login_interface.on_tbx_delete(login_interface.input_box.input_box))
          
        # Menu        
        
        # Orders
        
        # Payments
        
        # Kitchen/Inventory
        
        # Reports

if __name__ == '__main__':
    
    # Initialise the entire application and mapped settings
    app = Application(**app_settings)
    
    # Add any new settings after initialisation like below:
    # main_window.settings['SETTING_NAME'] = SETTING_VALUE
    
    # Run the tkinter event loop to control continuity
    app.main.master.mainloop()