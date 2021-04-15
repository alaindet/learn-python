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
        try:
            return sqlite3.connect(self.path)
        except Exception:
            print('Could not establish database connection')

    # TODO: Move to Database management class
    def execute(self, sql, boundValues):
        cursor = self.connection.cursor()
        cursor.execute(sql, boundValues)
        self.connection.commit()
        return cursor.lastrowid

    def select(self, sql):
        # TODO
        pass
