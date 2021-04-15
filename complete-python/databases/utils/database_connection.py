import sqlite3
from pathlib import Path

class DatabaseConnection():

    def __init__(self):
        self.init_path()
        self.open_connection()

    def __del__(self):
        self.close_connection()

    def init_path(self):
        root_dir = Path(__file__).parent.parent
        self.path = Path(root_dir, 'data', 'data.db').absolute()

    def open_connection(self):
        try:
            self.connection = sqlite3.connect(self.path)
        except Exception:
            print('Could not establish database connection')

    def close_connection(self):
        self.connection.close()
