class Employee:
    no_of_emps=0
    raise_amt= 0.5
    
    def __init__(self, first_name, last_name, pay):
        self.first_name=first_name
        self.last_name=last_name
        self.email= first_name +'.'+last_name +'.com'
        self.pay= pay
        Employee.no_of_emps+=1
        
    def apply_raise(self):
        self.pay = int(self.pay* self.raise_amt)
        return self.pay
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt=amount
    @classmethod
    def from_string(cls,emp_str):
        first_name , last_name ,pay=emp_str.split('-')
        return cls(first_name , last_name ,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
            
    
Employee.set_raise_amt(0.7)  
# emp_1=Employee("Kp","Singh", 5000)
# emp_2=Employee("Kp","Singh", 10000)
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

emp_1='Kp-singh-5000'
emp_2 ='abc-xyz-2000'
newEmp_1=Employee.from_string(emp_1)
newEmp_2=Employee.from_string(emp_2)
print(newEmp_1.email)
print(newEmp_2.email)
print(newEmp_1.raise_amt)

import datetime
mydate= datetime.date(2017,2, 18)
print(Employee.is_workday(mydate))