#try-except 예시(2)

list_input_a = ['2', '23', '552', '125', 'hello', '124']

list_number = []

for item in list_input_a:

    try:
        float(item) #exception occurred, jump into except clause
        list_number.append(item)
    
    except:
        pass

print(list_number)