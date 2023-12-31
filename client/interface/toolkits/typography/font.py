from tkinter.font import Font
from tkinter import Label, Entry
from tkinter import LEFT, RIGHT, CENTER

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
        
class Characters(BaseFont):
    """
    Base class for Tkinter Characters modification.
    Its purpose is to improve the user experience of an application by using a preset base design.
    """
    
    def __init__(self, family="Arial", propagate=False):
        super().__init__(family)
        # tbx_width = tbx_width if tbx_width != 0 else interface.winfo_reqwidth()
        self.font_style["size"] = int(self.font_style["size"] * 0.875) # rem
        self.font_style["weight"] = "normal"