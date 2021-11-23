import pyodbc
import json
from typing import *
from collections import *
connection = pyodbc.connect('Driver={SQL Server};' 'Server=QENI\FG;'
                          'Database=DataPersonal;' 'Trusted_connection=yes;')

def Read(connection):
  cursor=connection.cursor()
  print('Read')
  cursor.execute('Select * From PersonTable')
  delta=[]
  ticket=defaultdict(delta)
  count=0
  for zenit in cursor:
      for kert in zenit:
            json.dumps(delta.append(kert))
            ticket=cursor.
      count=+1
  return  delta
def Write(connection):
    cursor = connection.cursor()
    print('Write')
    FirstName=input('First Name: ')
    LastName=input('Enter Last Name: ')
    cursor.execute('Insert into PersonTable(Name, Surname) values(?,?);', (FirstName, LastName ) )
    connection.commit()
    Read(connection)
def Delete(connection):
    cursor = connection.cursor()
    print('Delete')
    Idm=input("Id:")
    cursor.execute('Delete from PersonTable where Id=?',(Idm))
    connection.commit()
    Read(connection)
def DeleteBetwwenId(connection):
    cursor = connection.cursor()
    print('Delete between id')
    Idm2=input("Id1: ")
    Idm3=input("Id2: ")
    cursor.execute('Delete from PersonTable where Id between ? and ? ',(Idm2,Idm3))
    connection.commit()
    Read(connection)
def DeleteName(connection):
    cursor = connection.cursor()
    print('Delete between id')
    NAME=input("Select Name:")
    cursor.execute('Delete from PersonTable where Name=? ',(NAME))
    connection.commit()
    Read(connection)
print(Read(connection))