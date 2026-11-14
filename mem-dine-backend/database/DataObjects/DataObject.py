from abc import ABC, abstractmethod
from sqlite3 import Connection


class DataBaseObject(ABC):

    @abstractmethod
    def create(self, con: Connection) -> bool:
        pass