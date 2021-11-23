class Employee:
    num_of_emps=0
    raise_amt=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@email.com'

        Employee.num_of_emps+=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)
    @staticmethod
    def is_workday(day):
        if day==5 or day.weekday()==6:
            return False
        return True
emp1=Employee('Corey','Schafer',50000)
emp2=Employee('Test','Employee',60000)
print(emp1.fullname())
print(emp2.fullname())
import datetime
my_data=datetime.date(2016, 7, 10)
print(Employee.is_workday(my_data))
class SubClass(Employee):
    raise_amt = 1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang


class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first, last, pay)
        if employees is None:
             self.employees = []
        else:
            self.employees=employees
