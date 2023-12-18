# --------------------------------------------------------------------------------------- #
# 
#   This is the LOGIN page window manager screen module.
#   Any functions related to this particular interface should
#   specifically be programmed in this environment.
# 
# --------------------------------------------------------------------------------------- #

from client.interface import Interface
from client.interface.authentication import AuthenticateUser
from client.settings import INITIAL_HEIGHT, INITIAL_WIDTH

import tkinter as tk


class LoginInterface(object):
    def __init__(self, master:Interface):
        self.__master = master
        self.__tk = master.interface
        
        navbar = tk.Frame(self.__master.main_frame, bg='red', width=INITIAL_WIDTH, height=(INITIAL_HEIGHT*0.12))
        content = tk.Frame(self.__master.main_frame, bg='blue', width=INITIAL_WIDTH, height=(INITIAL_HEIGHT-(INITIAL_HEIGHT*0.12)))
        # navbar.grid()
        content.grid()
        navbar.grid()

        
        # interface_items = {
        #     "lbl_login" : tk.Label(login_frame, text="Enter Staff ID:"),
        #     "tbx_login" : tk.Entry(login_frame)
        # }
        
        # self.__master.show_interface({
            
        # })
        
                
    def login(self) -> AuthenticateUser:
        pass
    
    def logout(self):
        pass