#<class variables vs. instance variables>

#두 variable의 차이 그림으로 설명하기

class Employee:

    raise_amount = 1.04 #class variable
    num_of_emps = 0

    def __init__(self, first, last, pay): 
        self.first = first #instance vairable
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com' 

        Employee.num_of_emps += 1

    def fullname(self): 
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)

emp_1 = Employee('Ryan', 'Kim', 500000)
emp_2 = Employee('Sam', 'Lim', 600000)

#------------------------------
#method를 이용해 instance variable 바꾸기

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

#------------------------------
#class variable 바꾸기

#(1)
Employee.raise_amount = 1.05 #결과 모두 동일
print(Employee.raise_amount) #1.05
print(emp_1.raise_amount) #1.05
print(emp_2.raise_amount) #1.05

#(2)
print(Employee.num_of_emps) #객체가 2로 바뀜

#------------------------------
print(emp_1.__dict__) #class variable 없음 확인 가능 - raise_amount & num_of_emps 없음
print(Employee.__dict__)