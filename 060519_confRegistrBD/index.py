import sqlite3
from datetime import datetime

conn = sqlite3.connect('registr.sqlite')
cursor = conn.cursor()

def createTable():
    cursor.execute('CREATE TABLE Members(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name varchar(50) NOT NULL, Surname varchar(50) NOT NULL, Age INTEGER, Phone varchar(15) UNIQUE NOT NULL, Date varchar(100) NOT NULL)')

def deleteTable():
    cursor.execute('DROP TABLE Members')

def clearTable():
    cursor.execute('DELETE FROM Members;')
    conn.commit()

def printTable():
    cursor.execute('SELECT * FROM Members')
    print(cursor.fetchall())

class Member(object):

    def __init__(self, name, sname, phone, age):
        self.name = name
        self.sname = sname
        self.age = age
        self.phone = phone

    def singUp(self):
        Date = datetime.now()
        cursor.execute(f'INSERT INTO Members(Name, Surname, Age, Phone, Date) VALUES(\'{self.name}\', \'{self.sname}\', {self.age}, \'{self.phone}\', \'{Date}\')')
        conn.commit()

    def delete(self):
        cursor.execute(f'DELETE FROM Members WHERE Name = \'{self.name}\' AND Phone = \'{self.phone}\'')
        conn.commit()
"""
mary = Member('Mary', 'Bukofsky', '22', '+73004010323')
mary.singUp()
jack = Member('Jack', 'Wulf', '42', '+741234123423')
jack.singUp()
linda = Member('Linda', 'Craz', '26', '+32512351235')
linda.singUp()
jamie = Member('Jamie', 'Lannister', '37', '+245243623462')
jamie.singUp()
"""

printTable()
conn.close()
