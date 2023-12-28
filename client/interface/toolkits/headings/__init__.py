from tkinter.font import Font
from tkinter.ttk import Label, Entry
from tkinter import LEFT, RIGHT, CENTER
from client.interface.toolkits.typography.font import *

class Heading6(BaseFont):
    """Pythonic version of HTML tag <h6></h6> for Tkinter. """
    
    def __init__(self, interface, family="Arial", text="HEADING"):
        super().__init__(family)
        self.tkfont = Font(root=interface, **self.font_style)
        self.label = Label(master=interface, text=text, font=self.tkfont)
        
class Heading5(BaseFont):
    """Pythonic version of HTML tag <h5></h5> for Tkinter. """
    
    def __init__(self, interface, family="Arial", text="HEADING"):
        super().__init__(family)
        self.font_style["size"] = int(self.font_style["size"] * 1.25) # rem
        self.tkfont = Font(root=interface, **self.font_style)
        self.label = Label(master=interface, text=text, font=self.tkfont)
        
class Heading4(BaseFont):
    """Pythonic version of HTML tag <h4></h4> for Tkinter. """
    
    def __init__(self, interface, family="Arial", text="HEADING"):
        super().__init__(family)
        self.font_style["size"] = int(self.font_style["size"] * 1.5) # rem
        self.tkfont = Font(root=interface, **self.font_style)
        self.label = Label(master=interface, text=text, font=self.tkfont)

class Heading3(BaseFont):
    """Pythonic version of HTML tag <h3></h3> for Tkinter. """
    
    def __init__(self, interface, family="Arial", text="HEADING"):
        super().__init__(family)
        self.font_style["size"] = int(self.font_style["size"] * 1.75) # rem
        self.tkfont = Font(root=interface, **self.font_style)
        self.label = Label(master=interface, text=text, font=self.tkfont)
        
class Heading2(BaseFont):
    """Pythonic version of HTML tag <h2></h2> for Tkinter. """
    
    def __init__(self, interface, family="Arial", text="HEADING"):
        super().__init__(family)
        self.font_style["size"] = int(self.font_style["size"] * 2) # rem
        self.tkfont = Font(root=interface, **self.font_style)
        self.label = Label(master=interface, text=text, font=self.tkfont)
        
class Heading1(BaseFont):
    """Pythonic version of HTML tag <h1></h1> for Tkinter. """
    
    def __init__(self, interface, family="Arial", text="HEADING"):
        super().__init__(family)
        self.font_style["size"] = int(self.font_style["size"] * 2.5) # rem
        self.tkfont = Font(root=interface, **self.font_style)
        self.label = Label(master=interface, text=text, font=self.tkfont)
        
        
class TextLabel(Characters):
     def __init__(self, interface, family="Arial", text="LABEL_TEXT", propagate=False):
        super().__init__(family, propagate)
        self.tkfont = Font(root=interface, **self.font_style)
        self.label = Label(interface, text=text, font=self.tkfont)
        