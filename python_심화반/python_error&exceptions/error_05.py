# try:

# except:

# finally: 
#option (필요에 따라서 사용) - 예외와 상관없이 무조건적으로 실행하는 코드
#주로 함수 내부 return, 반복문 내부 break 사용할 때 많이 씀
#주로 뒷처리할 때 많이 사용 - 무얼 하든 뒷처리, 마무리를 꼭 해야할 때
#예) file.close()로 주로 많이 사용

# 1) 함수 내부 return과 상관없이 finally 무조건 실행

#defining test() function

# def test():
#     print('A')

#     try:
#         print('B')
#         return
#         print('C')
    
#     except:
#         print('D')
    
#     finally:
#         print('E')
    
#     print('F')

# test() #A, B, E


def test():
    print('A')

    try:
        print('B')
        dkwhgkw
        print('C')
    
    except:
        print('D')
        return
    
    finally:
        print('E')
    
    print('F')

test() #A, B, D, E

#2) while True에서 break와도 상관없이 finally는 무조건 실행 - 문제 출제


#finally github에 검색하면서 확인해보기