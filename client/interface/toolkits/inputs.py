from tkinter import *
from tkinter.font import Font

from client.interface.toolkits.typography.font import Characters

class InputBox(Characters):
    """Pythonic version of HTML tag <input> for Tkinter. """ 
    
    def __init__(self, interface, family="Arial", label_text="ENTRY_BOX: ", x=0, y=0, tbx_border_size = 1, tbx_relief=SOLID, tbx_width=20, propagate=False): 
        super().__init__(family) 
        self.__subinterface = Frame(interface, padx=3, pady=3)
        self.width = self.get_width()
        self.height = self.get_height()
        
        self.x = x
        self.y = y
        
        self.tkfont = Font(root=interface, **self.font_style)
        self.input_box_label = Label(master=self.__subinterface, text=label_text, font=self.tkfont) 
        self.input_box = Entry(self.__subinterface, font=self.tkfont, bd=tbx_border_size, relief=tbx_relief, width=tbx_width, justify=LEFT)
        self.input_box.propagate(flag=propagate)
        
        self.input_box_label.pack(side=LEFT)
        self.input_box.pack(side=RIGHT)
        # self.__subinterface.place(x=x, y=y)
        
    def display(self, relx=0, rely=0):
        """Display the input box on the interface via place(). If no args are given then reverts to using (x,y).

        Args:
            relx (int, optional): relative X of the interface. Defaults to 0.
            rely (int, optional): relative Y of the interface. Defaults to 0.
        """
        if self.x != 0:
            self.__subinterface.place(x=self.x, y=self.y)
        if self.y != 0:
            self.__subinterface.place(x=self.x, y=self.y)
        
        self.__subinterface.place(relx=relx, rely=rely)
        
    def get_size(self):
        """Returns the width and height of an input box. """
        
        return (self.__subinterface.winfo_reqwidth(), self.__subinterface.winfo_height())
    
    def get_width(self):
        """Returns only the width of an input box. """
        
        return self.__subinterface.winfo_reqwidth()
    
    def get_height(self):
        """Returns only the height of an input box. """

        return self.__subinterface.winfo_height()
        
    def set_input_state(self, state):
        """Change the input state of the focused object. """
        
        if state == DISABLED:
            self.input_box.config(state=state, disabledbackground="#dddddd")
            return
            
        return self.input_box.config(state=NORMAL)

        

class ButtonBox(Characters):
    def __init__(self, buttons:list = [list]):
        """ Creates a set of button objects based on a 2D array of pre-determined button names.

        Args:
            buttons (list[list]): Pass a list of buttons to create automatically in a grid of X*Y. Defaults to [].
        """
        
        # for 