#<Classes and Instances>

#class 필요성 - 데이터와 함수의 묶음
#class의 데이터를 attribute, 함수를 method
#class를 본 뜬 각 객체를 instance

class Employee:
    #pass
    #pass 만들었을 때 아래 비효율적 소개 먼저 - __init__등등 class 내의 여러 method, variable 소개 

    def __init__(self, first, last, pay): #객체가 생성될 때 자동으로 생성되는 method (객체별 variable = instance variable의 초기화)
        self.first = first #instance vairable
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com' #만드는 법 물어보기

    def fullname(self): #self 없을 때 takes 0 positional arguments but 1 was given
        #자동적으로 instance가 method내에 무조건 들어감 - 무조건 self 필수
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Ryan', 'Kim', 500000) #class를 사용해 instance 객체 만들기
emp_2 = Employee('Sam', 'Lim', 600000)


print(emp_1, emp_2) #프린트 결과 다른 메모리 주소 - 다른 위치에 객체가 저장됨

#위 pass한 채로 각각 emp_1.email, fisrt, last 등등 만들고 비효율적
#print(emp_1.email)
#print(emp_2.email) #__init__ 소개
#print('{} {}'.format(emp_1.first, emp_1.last)) #8) 직접 하기보다는 위 fullname() 사용
#print(emp_1.fullname())

#즉, 위 method와 __init__으로 정한 각 instance 별 instance variable 소개