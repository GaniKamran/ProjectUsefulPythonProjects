import pyodbc


def checklogin():
    connection = pyodbc.connect('Driver={SQL Server};' 'Server=QENI\FG;'
                                'Database=Consulting;' 'Trusted_connection=yes;')

    cursor = connection.cursor()
    print('Write')
    FirstName = input('First Name: ')
    LastName = input('Password ')

    cursor.execute('select *From LoginC where Username=? and password=?', (FirstName,LastName))


    ren=cursor.fetchall()
    if(len(ren)==1):
      cursor.execute('select *From PersonalityInformation where UserName=?',FirstName)
      for i in cursor:
       print(i)
    else:
        print("alimadi")
    connection.commit()



checklogin()