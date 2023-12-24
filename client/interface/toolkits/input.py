from tkinter import *
from tkinter.font import Font

from client.interface.toolkits.typography.font import Characters

class InputBox(Characters):
    """Pythonic version of HTML tag <input> for Tkinter. """ 
    
    def __init__(self, interface, family="Arial", label_text="ENTRY_BOX: ", justify_text = CENTER, propagate=False, border_size = 1, x=0, y=0): 
        super().__init__(family) 
        subinterface = Frame(interface, padx=3, pady=3, )
        self.tkfont = Font(root=interface, **self.font_style)
        self.input_box_label = Label(master=subinterface, text=label_text, font=self.tkfont) 
        self.input_box = Entry(subinterface, font=self.tkfont, bd=border_size, relief=SOLID)
        self.input_box.propagate(flag=propagate)
        self.input_box_label.pack(side=LEFT)
        self.input_box.pack(side=RIGHT)
        subinterface.place(x=x, y=y)
        # Center the input box to the middle of the root display
        # subinterface.place(
        #     x=(interface.winfo_reqwidth()/2)-(subinterface.winfo_reqwidth()/2),
        #     y=(interface.winfo_reqheight()/2)-(subinterface.winfo_reqheight()/2)
        # )
        