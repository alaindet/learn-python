import sqlite3
from pathlib import Path

class DatabaseConnection():

    def __init__(self):
        self.path = self.init_path()
        self.connection = self.init_connection()

    def __del__(self):
        self.connection.close()

    def init_path(self):
        root_dir = Path(__file__).parent.parent
        return Path(root_dir, 'data', 'data.db').absolute()

    def init_connection(self):
        return sqlite3.connect(self.path)
