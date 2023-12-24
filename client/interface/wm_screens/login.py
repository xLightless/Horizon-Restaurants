# --------------------------------------------------------------------------------------- #
# 
#   This is the LOGIN page window manager screen module.
#   Any functions related to this particular interface should
#   specifically be programmed in this environment.
# 
# --------------------------------------------------------------------------------------- #

from client.interface import Interface
from client.interface.authentication import AuthenticateUser
from client.interface.toolkits.typography.font import *
from client.interface.toolkits.headings import *
from client.interface.toolkits.input import InputBox
from client.settings import INITIAL_HEIGHT, INITIAL_WIDTH

import tkinter as tk

widget_options = {
    "bd" : 1,
    "relief" : tk.SOLID,
    # "padx" : 5,
    # "pady" : 5
}

NAVBAR_HEIGHT = 64


class Login():
    """ Login Interface component for the HRMS System. """
    
    def __init__(self, interface:Interface):
        # Initialise a Login Interface Frame
        i = tk.Frame(interface.master, width=INITIAL_WIDTH, height=INITIAL_HEIGHT)
        i.pack(fill="both", expand=True)
        
        # Create a subframe for the UI
        i_top = tk.Frame(i, width=INITIAL_WIDTH, height=NAVBAR_HEIGHT, bd=1, relief=tk.SOLID)
        i_top.pack_propagate(False)
        i_top.pack(side=tk.TOP)
        
        # Pack a heading for the subframe
        lbl_restaurants = Heading6(i_top, text="Horizon Restaurants Ltd.")
        lbl_restaurants.label.pack(side="top", fill="both", expand=True)
        
        # Create a new subframe for the UI
        i_bottom = tk.Frame(i, width=INITIAL_WIDTH, height=(INITIAL_HEIGHT - NAVBAR_HEIGHT))
        i_bottom.pack_propagate(False)
        i_bottom.pack(side=tk.BOTTOM)
        
        # Pack an input box onto the subframe
        i_bottom_input = InputBox(i_bottom)
        # i_bottom_input.entry.place(relx=0.5, rely=0.5)
        
        
        
        
        
        
        
        
        
        











# class LoginInterface(Interface):
#     def __init__(self, master):
#         self.login_frame = tk.Frame(self.main_frame)
#         self.login_frame.configure(bg='red')
#         self.login_frame.pack()
        
        
        
        
        
        # interface_items = {
        #     "lbl_login" : tk.Label(login_frame, text="Enter Staff ID:"),
        #     "tbx_login" : tk.Entry(login_frame)
        # }
        
        # self.__master.show_interface()
        
                
    # def login(self) -> AuthenticateUser:
    #     pass
    
    # def logout(self):
    #     pass