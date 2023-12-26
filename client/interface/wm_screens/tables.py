# --------------------------------------------------------------------------------------- #
# 
#   Manages the interaction of table occupancy and number.
# 
# --------------------------------------------------------------------------------------- #




class Table(object):
    def __init__(self):
        self.__table_number:int = 0
        self.__occupants:int = 0
    
    def get_table_occupants(self) -> int:
        return
    
    def get_table_size(self) -> int:
        return
    
    def is_occupied(self) -> bool:
        return
    
    def get_table_number(self) -> int:
        return self.__table_number
    
    def set_table(self, table_number:int):
        return