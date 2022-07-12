try:
    a = [27,31,42,535,231]

    number = int(input('정수 입력(0~4까지 입력해주세요)>'))
    print(a[number])

except ValueError as exception:
    print('값에 문제가 있습니다.')
except IndexError as exception:
    print('0~4까지 입력해주세요.')
except Exception as exception: #마지막 기타 에러는 이렇게 처리! 거의 모두 사용
    print('알 수 없는 예외가 발생했습니다. 개발자에게 메일을 보내보세용~')