from dataclasses import dataclass

@dataclass
class Root:
    screenName: str = None
    baseName: str = None
    className: str = None
    useTk: bool = True
    sync: bool = False
    use: str = None
        

# tk.Frame()

# @dataclass
class FrameMap:
    def __init__(
        self,
        background_color = None,
        border = None,
        border_width = None,
        border_type = None,
        cursor = None,
        height = None,
        width = None
        
    ):
        self.bd = border
        
        
        
def is_subset(subset, superset):
    return all(item in superset.items() for item in subset.items())