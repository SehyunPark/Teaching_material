try:
    a = [27,31,42,535,231]

    number = int(input('정수 입력(0~4까지 입력해주세요)>'))
    print(a[number])

except Exception as e: #exception 예외종류 as 변수로 사용할 이름
    if type(e) == ValueError:
        print('값에 문제가 있습니다.')

    elif type(e) == IndexError:
        print('0~4까지를 입력해주세요')