from database.DataObjects.DataObject import DataBaseObject
from sqlite3 import Connection
from dataclasses import dataclass
from datetime import datetime
from sqlite3 import IntegrityError
from typing import Optional

from werkzeug.security import check_password_hash, generate_password_hash

@dataclass(frozen=True, slots=True)
class UserPackage:
    id: int
    name: str
    created_at: datetime


class User(DataBaseObject):

    def __init__(self):
        super().__init__()

    def _package_factory(self, row: tuple) -> UserPackage:
        return UserPackage(
            id=row[0],
            name=row[1],
            created_at=datetime.fromisoformat(row[2]),
        )

    def create(self, con: Connection) -> bool:
        con.cursor().execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)
        return True

    def exists(self, con: Connection, id: int = None, username: str = None) -> int:
        """Gets user id if they exists, if they don't return -1"""
        if id is not None:
            row = con.execute(
                "SELECT id FROM users WHERE id = ?", (id,)
            ).fetchone()
        elif username is not None:
            username = username.strip().lower()
            row = con.execute(
                "SELECT id FROM users WHERE name = ?", (username,)
            ).fetchone()
        else:
            return -1

        return row[0] if row is not None else -1

    def get_user(self, con: Connection, id: int) -> Optional[UserPackage]:
        row = con.execute(
            "SELECT id, name, created_at FROM users WHERE id = ?", (id,)
        ).fetchone()

        if row is None:
            return None

        return self._package_factory(row)

    def create_user(self, con: Connection, username: str, password: str) -> bool:
        username = username.strip().lower()
        if not username or len(username) > 64 or not 12 <= len(password) <= 1024:
            return False

        password_hash = generate_password_hash(password)
        try:
            con.execute(
                "INSERT INTO users (name, password) VALUES (?, ?)",
                (username, password_hash),
            )
        except IntegrityError:
            return False

        con.commit()
        return True

    def verify_password(self, con: Connection, username: str, password: str) -> bool:
        username = username.strip().lower()
        row = con.execute(
            "SELECT password FROM users WHERE name = ?", (username,)
        ).fetchone()
        return row is not None and check_password_hash(row[0], password)