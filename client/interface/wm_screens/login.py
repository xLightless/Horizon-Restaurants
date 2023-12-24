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
from client.interface.toolkits import inputs, headings
from client.settings import INITIAL_HEIGHT, INITIAL_WIDTH
from client.errors import InvalidCredentialsError

from tkinter import messagebox
import tkinter as tk

widget_options = {
    "bd" : 1,
    "relief" : tk.SOLID,
    # "padx" : 5,
    # "pady" : 5
}

NAVBAR_HEIGHT = 64


class Login(AuthenticateUser):
    """ Login Interface component for the HRMS System. """
    
    def __init__(self, interface:Interface):
        # Initialise a Login Interface Frame
        i = tk.Frame(interface.master, width=INITIAL_WIDTH, height=INITIAL_HEIGHT)
        i.pack(fill="both", expand=True)
        
        # Create a subframe for the UI
        i_top = tk.Frame(i, width=INITIAL_WIDTH, height=NAVBAR_HEIGHT)
        i_top.pack_propagate(False)
        i_top.pack(side=tk.TOP)
        
        # Pack a heading for the subframe
        lbl_restaurants = headings.Heading6(i_top, text="Horizon Restaurants Ltd.")
        lbl_restaurants.label.configure(bg="#1e1e1e", fg='white') # Add dark theme
        lbl_restaurants.label.pack(side="top", fill="both", expand=True)
        
        # Create a new subframe for the UI
        i_bottom = tk.Frame(i, width=INITIAL_WIDTH, height=(INITIAL_HEIGHT - NAVBAR_HEIGHT), padx=3, pady=3)
        i_bottom.configure(bg="#1e1e1e")
        i_bottom.pack_propagate(False)
        
        # Enter login pin
        lbl_frame = tk.LabelFrame(i_bottom, text="", width=i_bottom.winfo_reqwidth()/2, height=i_bottom.winfo_reqheight())
        lbl_frame.configure(bg="#1e1e1e", fg='white', padx=3, pady=3)
        
        # Create frame seperation for the PIN Entry
        lbl_frame_top = tk.Frame(lbl_frame, width=lbl_frame.winfo_reqwidth(), height=NAVBAR_HEIGHT)
        lbl_frame_top.configure(bg="#1e1e1e")
        
        lbl_frame_bottom = tk.Frame(lbl_frame, width=lbl_frame.winfo_reqwidth(), height=lbl_frame_top.winfo_reqwidth()-NAVBAR_HEIGHT)
        lbl_frame_bottom.configure(bg="#1e1e1e")
        lbl_frame_bottom.grid_propagate(False)
        lbl_frame_bottom.pack_propagate(False)
        lbl_frame_bottom.propagate(False)
        
        # Disabled Input box for displaying staff id
        lbl_frame_top_heading = headings.TextLabel(lbl_frame_top, text="Enter your Staff ID:")
        lbl_frame_top_heading.label.configure(bg="#1e1e1e", fg='white')
        lbl_frame_top_heading.label.grid(row=0, column=0)
        tbx_input_disabled = inputs.InputBox(lbl_frame_top, label_text="", tbx_width=20, tbx_border_size=0, state='readonly')
        tbx_input_disabled.input_box.configure(fg='red')
        # tbx_input_disabled.set_input_state(state=tk.DISABLED)
        tbx_input_disabled.x += (lbl_frame.winfo_reqwidth()/2) - (tbx_input_disabled.input_box.winfo_reqwidth()/2) - (tbx_input_disabled.input_box_label.winfo_reqwidth()/2)
        # tbx_input_disabled.y += (lbl_frame.winfo_reqheight()/2) - (tbx_input_disabled.input_box.winfo_reqheight()/2)
        tbx_input_disabled.display(grid=[1, 0])
        
        # Input to entry box via Buttons
        input_btn_box = inputs.ButtonBox(
            lbl_frame_bottom, 
            buttons=[
                [1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9], 
                ["Login", 0, "<<"]
                ]
            )
        

        for btn in input_btn_box.btn_list:
            idx = input_btn_box.btn_list.index(btn)
            if (idx != 9) or (idx != 11):
                btn.configure(command = lambda x = str(btn.cget('text')): self.on_tbx_insert(tbx_input_disabled.input_box, x))
            if idx == 11:
                btn.configure(command = lambda: self.on_tbx_delete(tbx_input_disabled.input_box))
            if idx == 9:
                btn.configure(command = lambda: print("Getting database details, logging in...") if self.get_tbx_length(tbx_input_disabled.input_box)>0 else messagebox.showwarning("Authentication Error!", InvalidCredentialsError()))
            
        # tbx_input_disabled.input_box.configure(textvariable=disabled_btn_text.set(disabled_btn_text + btn_text))



        i_bottom.pack(side=tk.BOTTOM)
        lbl_frame_top.pack(side=tk.TOP)
        lbl_frame_bottom.pack(side=tk.BOTTOM)
        lbl_frame.pack()
        lbl_frame.pack()
    

    def login(self):
        """Attempts to login the user with the requested access method."""
        return


    def on_tbx_insert(self, tbx_input, args):
        tbx_input.configure(state="normal")
        tbx_input.insert(tk.END, args)
        tbx_input.configure(state="readonly")
        
    def on_tbx_delete(self, tbx_input):
        tbx_input.configure(state="normal")
        tbx_input.delete(0, tk.END)
        tbx_input.configure(state="readonly")
        
    def get_tbx_length(self, tbx_input):
        return len(tbx_input.get())
        





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