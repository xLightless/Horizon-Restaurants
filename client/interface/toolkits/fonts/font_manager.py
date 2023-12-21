from tkinter.font import Font
from tkinter import Label

# CSS-like tkinter window styling. self.root equivalent to :root {};   
root = {
    "font_size":    16, # px
    "margin":       0,
    "padding":      0,
}

class BaseFont(object):
    """ Base class for Tkinter Font modulation."""
    
    def __init__(self, family="Arial", size:int = root["font_size"], weight="bold", slant:str="roman"):
        self.font_size = size
        self.custom_font_file = ""
        self.font_family = family
        self.font_weight_type = weight
        self.font_slant = slant
        self.underline = 0
        self.overstrike = 0
        
        # If a custom font path + file is entered into family then use this instead of a built-in.
        if self.font_family.endswith(".tff"):
            self.custom_font_file = self.font_family.split("\\")[-1]
            self.font_family = self.custom_font_file[:-4]
            
        # Create a set mapping of the BaseFont for child classes
        self.font_style = {
            "family": self.font_family,
            "size": self.font_size,
            "weight": self.font_weight_type,
            "slant": self.font_slant,
            "underline": self.underline,
            "overstrike": self.overstrike
        }

class Heading6(BaseFont):
    """Pythonic version of HTML tag <h6></h6> for Tkinter. """
    
    def __init__(self, interface, family="Arial", text="LBL_TEXT"):
        super().__init__(family)
        self.tkfont = Font(root=interface, **self.font_style)
        self.label = Label(master=interface, text=text, font=self.tkfont)
        
class Heading5(BaseFont):
    """Pythonic version of HTML tag <h5></h5> for Tkinter. """
    
    def __init__(self, interface, family="Arial", text="LBL_TEXT"):
        super().__init__(family)
        self.font_style["size"] = int(self.font_style["size"] * 1.25) # rem
        self.tkfont = Font(root=interface, **self.font_style)
        self.label = Label(master=interface, text=text, font=self.tkfont)
        
class Heading4(BaseFont):
    """Pythonic version of HTML tag <h4></h4> for Tkinter. """
    
    def __init__(self, interface, family="Arial", text="LBL_TEXT"):
        super().__init__(family)
        self.font_style["size"] = int(self.font_style["size"] * 1.5) # rem
        self.tkfont = Font(root=interface, **self.font_style)
        self.label = Label(master=interface, text=text, font=self.tkfont)

class Heading3(BaseFont):
    """Pythonic version of HTML tag <h3></h3> for Tkinter. """
    
    def __init__(self, interface, family="Arial", text="LBL_TEXT"):
        super().__init__(family)
        self.font_style["size"] = int(self.font_style["size"] * 1.75) # rem
        self.tkfont = Font(root=interface, **self.font_style)
        self.label = Label(master=interface, text=text, font=self.tkfont)
        
class Heading2(BaseFont):
    """Pythonic version of HTML tag <h2></h2> for Tkinter. """
    
    def __init__(self, interface, family="Arial", text="LBL_TEXT"):
        super().__init__(family)
        self.font_style["size"] = int(self.font_style["size"] * 2) # rem
        self.tkfont = Font(root=interface, **self.font_style)
        self.label = Label(master=interface, text=text, font=self.tkfont)
        
class Heading1(BaseFont):
    """Pythonic version of HTML tag <h1></h1> for Tkinter. """
    
    def __init__(self, interface, family="Arial", text="LBL_TEXT"):
        super().__init__(family)
        self.font_style["size"] = int(self.font_style["size"] * 2.5) # rem
        self.tkfont = Font(root=interface, **self.font_style)
        self.label = Label(master=interface, text=text, font=self.tkfont)
        
        
        
# class Text
        
        