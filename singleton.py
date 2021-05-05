import sqlite3


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.connection = None

    def connect(self):
        print(self.connection)
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


a = Singleton()
b = Singleton()
c = Singleton()
a.connect()
b.connect()
c.connect()
