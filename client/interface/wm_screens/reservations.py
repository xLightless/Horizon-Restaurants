# from client.interface.wm_screens.tables import Table


class Reservation(object):
    def __init__(self, parent):
        self.parent = parent
        
        # Create any objects
    
    def create(self, table_number: int, occupants:int, date:str, branch_id:int):
        return
    
    # def get(self) -> Table:
    #     return Table().get_table_number()
    
    def update(self, table_number:int, **args:dict):
        return
    
    def cancel(self, table_number:int, date:str):
        return
    
    def get_reservation_availability(self):
        return