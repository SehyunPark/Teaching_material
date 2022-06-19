#Q. calculator class 만들기
# 1) cal 클래스는 생성자를 통해 두 수를 입력받는다.(input()을 통해 사용자 지정 두 수를 입력받음)
# 2) cal 클래스는 add, mul, div, sub 네 개 사칙연산 인스턴스 메서드를 구성한다.
# 3) 사용자 지정 1번을 입력하면 두 수의 덧셈 결과 출력, 2번을 입력하면 두 수의 뺄셈 결과 출력, 3번을 입력하면 두 수의 곱셈 결과 출력, 4번을 입력하면 두 수의 나눗셈 결과 출력, 0번을 입력하기 전까지 무한히 연산 결과를 출력할 수 있게 loop을 만든다., 0~4가 아닌 그 이외의 번호를 입력하면 잘못된 입력했다는 메시지를 출력한다.
# 4) 나눗셈은 소수 둘째자리까지 출력한다. (round() 이용)

class cal(): #class cal
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a+self.b
   
    def mul(self):
        return self.a*self.b
   
    def div(self):
        return self.a/self.b
   
    def sub(self):
        return self.a-self.b

a = int(input("첫번째 숫자 입력: "))
b = int(input("두번째 숫자 입력: "))

obj=cal(a,b) # 인스턴스 생성

choice=1

while choice!=0:
    
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division") #나눗셈 - 소수 둘째자리만 출력
    
    choice=int(input("Enter choice: "))
    
    if choice==1:
        print("Result: ",obj.add())
    
    elif choice==2:
        print("Result: ",obj.sub())
    
    elif choice==3:
        print("Result: ",obj.mul())
    
    elif choice==4:
        print("Result: ",round(obj.div(),2))
    
    elif choice==0:
        print("BYE-BYE")
    
    else:
        print("Invalid choice!!")