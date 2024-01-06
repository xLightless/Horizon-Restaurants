from server.sql.database import database
from client.interface.toolkits import inputs, headings

class Reservations(object):
    def __init__(self, parent):
        self.parent = parent
        

    def get_reservations(self):
        return database.get_table("reservations", True)