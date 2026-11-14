import sqlite3
from typing import Final
from database.DataObjects.User import User

class _DatabaseConnection:

    database_path: Final[str]

    
    def __init__(self):
        self.database_path = "app.db"
        con = self.connect()
        try:
            User().create(con)
        finally:
            con.close()

    def connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.database_path)


database_connection = _DatabaseConnection()
