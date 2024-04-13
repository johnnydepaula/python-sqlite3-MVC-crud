import sqlite3

# Create a class that instantiate a SQLite connection object
# with PRAGMA foreign_keys support, since it's disable by
# default on SQLite.


class Connection:
    def __init__(self):
        self.conn = sqlite3.connect('/home/johnny/temp/python-mvc-crud/models/agenda_db.db')
        self.conn.execute("PRAGMA foreign_keys=ON")
        self.cur = self.conn.cursor()
