from database.DataObjects.DataObject import DataBaseObject
from sqlite3 import Connection
from dataclasses import dataclass
from datetime import datetime

class UserPackage:
    id: int
    name: str
    password: str
    cerated_at: datetime


class User(DataBaseObject):

    def __init__(self):
        super().__init__()

    def _package_factory(self, row: dict) -> UserPackage:
        return UserPackage(*row)

    def create(self, con: Connection) -> bool:
        con.cursor().execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

    def exists(self, con: Connection, id: int = None, username: str = None) -> int:
        """Gets user id if they exists, if they don't return -1"""
        where_statement = None
        
        if id is not None:
            where_statement = f"WHERE ID = {id}"

        if username is not None:
            where_statement = f"WHERE name = {username}"

        if where_statement is None:
            return -1 
        
        users = con.cursor().execute(f"SELECT id FROM User {where_statement}")
        
        if len(users) == 0:
            return -1

        return users[0]["id"]   

    def get_user(self, con: Connection, id: int) -> UserPackage:
        users = con.cursor().execute(f"SELECT * FROM User WHERE id = {id}")
        
        if len(users) == 0:
            return None

        return self._package_factory(users[0])

    def create_user(self, con: Connection, username: str, password: str) -> bool:
        return False