import pyodbc
class Person():



    def __init__(self,name,fullname,fathername,Age,location,WorkId,PhoneNumber,CaseofLife,Education):
        self.name=name
        self.fullname=fullname
        self.fathername=fathername
        self.Age=Age
        self.location=location
        self.workId=WorkId
        self.PhoneNumber=PhoneNumber
        self.Education=Education
        self.CaseOfLife=CaseofLife
        self.connect=pyodbc.connect('Driver={SQL Server};' 'Server=QENI\FG;'
                          'Database=DataPersonal;' 'Trusted_connection=yes;')

    def read(self):
        cursor=self.connect.cursor()
        print("read")
        cursor.execute('Select * From PersonTable')
        for i in cursor:
           print(i)
        cursor.commit()
    def write(self):
        cursor = self.connect.cursor()
        cursor.execute('Insert into PersonTable(Name, Surname, FatherName, Age, Location, Education, Workd, PhoneNumber, CaseofLife) values(?,?,?,?,?,?,?,?,?);',(self.name,self.fullname,self.fathername,self.Age,self.location,self.Education,self.PhoneNumber,self.workId,self.CaseOfLife))
        self.connect.commit()
ep1=Person("Rauf","dwdsa","jwqjdiqw",23,"dwdsa","jwqjdiqw","jwqjdiqw","123243","gsdfg")
ep1.write()
ep1.read()









