import sqlite3


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        print(self.connection)
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursor = self.connection.cursor()
        return self.cursor


a = Singleton()
b = Singleton()
c = Singleton()
a.connect()
b.connect()
c.connect()
