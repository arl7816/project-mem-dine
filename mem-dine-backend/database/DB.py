import sqlite3
from typing import Final
from database.DataObjects.User import User

class _DatabaseConnection:

    con: Final

    
    def __init__(self):
        self.con = sqlite3.connect("app.db")

        # make sure all needed tables are created
        User().create(self.con)


database_connection = _DatabaseConnection()
