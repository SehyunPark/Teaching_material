#try-except 예시 (1)

while True:
    try:
        #예외가 발생할 수 있는 가능성 있는 코드
        print(float(input('> input an integer:')) ** 2)
        break
    except:
        #예외가 발생했을 때 실행할 코드
        print('please input an integer')