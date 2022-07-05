# number_input = int(input('input your integer> '))

# print('radius:', number_input)
# print('circumference of your circle is:', 2*3.14*number_input)
# print('area of your circle is:', 3.14*number_input*number_input)

#정수아니고 float이나 string입력하면 ValueError: invalid literal for int() with base 10: '1.2' - improper value 들어갔을 때
#try-except 필요성

def division(a,b):
    return a/b

print(division(3,0))

#ZeroDivisionError: division by zero (division(3,0))

#NameError(division(3,o))

#추가 ImportError, KeyError, IndentationError, typeError, attributeerror 더 많은 error 학습하고 넘어가기