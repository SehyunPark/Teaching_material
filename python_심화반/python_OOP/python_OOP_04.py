#<class inheritance>

class School: #학교 class

    power = 1.5 #학교 평판지수
    num = 0 #학교 수

    def __init__(self, name, area, location, level):
        self.name = name
        self.area = area
        self.location = location
        self.level = level

        School.num += 1
    
    #regular method
    def add_power(self):
        self.power = self.power * self.level

    @classmethod
    def change_power(cls, pwr):
        cls.power = pwr
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
sch_1 = School('munhwa', 300, 'ilsan', 1)
sch_2 = School('balsan', 400, 'ilsan', 2)

#---------------------------------------------
#1) regular method
#각 객체 내의 변수 바꾸기

sch_1.add_power()
print(sch_1.power)

sch_2.add_power()
print(sch_2.power)

print(School.power)

#--------------------------------------------
#2) class method
#class 변수 바꾸기

School.change_power(4)
print(School.power)

#----------------------------------------------
#3) static method
#class, 객체와 상관 x

import datetime
my_date = datetime.date(2022, 6, 28)

print(School.is_workday(my_date))
#----------------------------------------------

#inheritance - 중학교 class 상속하기
class Middle_School(School):
    
    power = 5.0 #상위 class의 attribute는 안 바뀐 상태에서 상속된 class만 바뀜

    def __init__(self, name, area, location, level, uniform):
        super().__init__(name, area, location, level) #super() 사용
        self.uniform = uniform

    #상속하면 위 상위 class의 모든 attribute, method 활용 가능

ms_1 = Middle_School('balsan', 400, 'ilsan', 2, 10)

print(ms_1.uniform)
#한 개 더 상속된 class 출력해보기 (상속된 두 class 간의 관계)
#-----------------------------------
print(isinstance(ms_1, Middle_School))
print(isinstance(sch_1, Middle_School))

#------------------------------------
print(issubclass(Middle_School, School))
print(issubclass(School, Middle_School))
