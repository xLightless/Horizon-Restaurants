from tkinter import *
from tkinter.font import Font

from client.interface.toolkits.typography.font import Characters

class InputBox(Characters):
    """Pythonic version of HTML tag <input> for Tkinter. """ 
    
    def __init__(self, interface, family="Arial", label_text="ENTRY_BOX: ", x=0, y=0, tbx_border_size = 1, tbx_relief=SOLID, tbx_width=20, propagate=False, padx=3, pady=3, state='normal'): 
        super().__init__(family)
        
        self.padx = padx
        self.pady = pady
        self.__subinterface = Frame(interface, padx=self.padx, pady=self.pady)
        
        self.x = x + (self.padx*2)
        self.y = y + (self.pady*2)
        
        self.tkfont = Font(root=interface, **self.font_style)
        self.input_box_label = Label(master=self.__subinterface, text=label_text, font=self.tkfont) 
        self.input_box = Entry(self.__subinterface, font=self.tkfont, bd=tbx_border_size, relief=tbx_relief, width=tbx_width, justify=LEFT, state=state)
        # self.input_box.propagate(flag=propagate)
        
        # Check if the label is empty. No need to display an empty label.
        if len(label_text) != 0:
            self.input_box_label.pack(side=LEFT)
        self.input_box.pack(side=RIGHT)
        
    def get_frame(self):
        return self.__subinterface
        
    def display(self, relx=0, rely=0, grid:list=[], sticky=None):
        """Display the input box on the interface via place(). If no args are given then reverts to using (x,y).

        Args:
            relx (int, optional): relative X of the interface. Defaults to 0.
            rely (int, optional): relative Y of the interface. Defaults to 0.
            grid (list): position the object by [row, column] on a grid with other objects.
        """
        if self.x != (self.padx*2):
            self.__subinterface.place(x=self.x, y=self.y)
        if self.y != (self.pady*2):
            self.__subinterface.place(x=self.x, y=self.y)
            return
        
        if len(grid) == 0:
            return self.__subinterface.place(relx=relx, rely=rely)
        
        if len(grid)>0:
            return self.__subinterface.grid(row=grid[0], column=grid[1]) if sticky == None else self.__subinterface.grid(row=grid[0], column=grid[1], stick=sticky)
        
    def get_size(self):
        """Returns the width and height of an input box. """
        
        return (self.__subinterface.winfo_reqwidth(), self.__subinterface.winfo_reqheight())
    
    def get_width(self):
        """Returns only the width of an input box. """
        
        return self.__subinterface.winfo_reqwidth()
    
    def get_height(self):
        """Returns only the height of an input box. """

        return self.__subinterface.winfo_reqheight()
        
    def set_input_state(self, state):
        """Change the input state of the focused object. """
        
        if state == DISABLED:
            return self.input_box.config(state=state, disabledbackground="#dddddd") 
        return self.input_box.config(state=NORMAL)
    
    def on_tbx_insert(self, tbx_input, args):
        tbx_input.configure(state="normal")
        tbx_input.insert(END, args)
        tbx_input.configure(state="readonly")
        
    def on_tbx_delete(self, tbx_input):
        tbx_input.configure(state="normal")
        tbx_input.delete(0, END)
        tbx_input.configure(state="readonly")
        
    def get_tbx_length(self, tbx_input):
        return len(tbx_input.get())

        

class ButtonBox(Characters):
    def __init__(self, interface, buttons:list = [list], button_size_multiplier:int = 4):
        """ Creates a set of button objects based on a 2D array of pre-determined button names.

        Args:
            buttons (list[list]): Pass a list of buttons to create automatically in a grid of X*Y. Defaults to [].
        """
        
        self.__subinterface = Frame(interface)
        self.btn_list = []
                
        for row in range(len(buttons)):
            for col in range(len(buttons[row])):
                
                btn = Button(self.__subinterface, text=buttons[row][col])
                btn.configure(
                    width=int(len(buttons[row])*len(buttons)/interface.winfo_reqwidth()*100)*button_size_multiplier,
                    height=int(len(buttons[row])*len(buttons)/interface.winfo_reqheight()*100)*int(button_size_multiplier/2)
                )
                self.btn_list.append(btn)
                btn.grid(row=row, column=col)
                
        self.__subinterface.place(relx=0.5, rely=0.5, anchor=CENTER)
        # btn_list = [(Button(interface, text=buttons[row][col]), (row,col)) for row in range(len(buttons)) for col in range(len(buttons[row]))]