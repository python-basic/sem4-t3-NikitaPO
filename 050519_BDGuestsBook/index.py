import sqlite3
from datetime import datetime, date, time

conn = sqlite3.connect('guestsBook.sqlite')
cursor = conn.cursor()

def createTable():
    cursor.execute(f'CREATE TABLE Guests( Author varchar(50) NOT NULL, Comment varchar(255) NOT NULL, Date varchar(100) NOT NULL, ID INTEGER PRIMARY KEY AUTOINCREMENT)')

def deleteTable():
    cursor.execute(f'DROP TABLE Guests')

def clearTable(ID:int=None, Author:str=None):
    if ID:
        cursor.execute(f'DELETE FROM Guests WHERE ID={ID};')
    elif Author:
        cursor.execute(f'DELETE FROM Guests WHERE Author=\'{Author}\';')
    else:
        cursor.execute(f'DELETE FROM Guests;')
    conn.commit()

def printTable():
    cursor.execute('SELECT * FROM Guests;')
    print(cursor.fetchall())

class Guest(object):
    def __init__(self, name):
        self.name = name
        self._comment = None

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, com):
        self._comment = com

    def addComment(self):
        Date = str(datetime.now())
        cursor.execute(f'INSERT INTO Guests (Author, Comment, Date) VALUES (\'{self.name}\', \'{self._comment}\', \'{Date}\')')
        conn.commit()

    @comment.deleter
    def comment(self):
        cursor.execute(f'DELETE FROM Guests WHERE Author=\'{self.name}\' AND Comment=\'{self._comment}\';')
        conn.commit()
        del self._comment

mike = Guest('Майк')
mike.comment = 'Провел тут классный отдых'
del mike.comment

printTable()

conn.close()
