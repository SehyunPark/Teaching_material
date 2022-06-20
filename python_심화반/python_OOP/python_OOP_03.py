#<regular instance methods vs. class methods(+alternative constructor) vs. static methods>

class Employee:

    raise_amount = 1.04 
    num_of_emps = 0

    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com' 

        Employee.num_of_emps += 1

    def fullname(self): 
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self): #regular method는 instance 변수 self를 받아들이는데
        self.pay = int(self.pay * self.raise_amount)

    @classmethod #class method는 class를 받아들임
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount #위 method와 다르게, instance 변수가 아니라 class 변수를 바꿈

    @classmethod #class constructor(class 생성자) 생성
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day): #위 두 method와 다르게 self, cls를 안받는다
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    #class와 regular method와 다르게 static method는 instace, class 필요 없이 아무때나 사용 가능    
    #즉, self나 cls를 사용안할 경우 static method

emp_1 = Employee('Ryan', 'Kim', 500000)
emp_2 = Employee('Sam', 'Lim', 600000)

#------------------------------------

#1) class_method) set_raise_amt

# Employee.set_raise_amt(1.05) #class 변수 raise_amt를 바꿈

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_1.set_raise_amt(1.06) #emp_1을 이용해서 바꿔도 class 전체 변수 raise_amount가 바뀜

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

#------------------------------------

#2) class_method) from_string

#emp_str_1 = 'John-Doe-700000'
#first, last, pay = emp_str_1.split('-')
#new_emp_1 = Employee(first, last, pay) #문자열에서 split을 이용해 새로운 객체 생성
#print(new_emp_1.email)

#위와 같이 직접 split으로 일일이 하지말고 class method를 class constructor의 역할로 만들 수 있다.
#new_emp_1 = Employee.from_string(emp_str_1)

#print(new_emp_1.email)

#-------------------------------------

#3) static method) regular, class와 다르게 첫 인자로 self, cls가 안들어감

import datetime
my_date = datetime.date(2022, 6, 21)

print(Employee.is_workday(my_date))

#-------------------------------------

# Q. 앞에서 만들었던 calculator class에 적절한 class method & static method 만들어보기