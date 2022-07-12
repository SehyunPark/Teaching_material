names = ['Ryan', 'Sam', 'Mickey', 'Lacey', 'Nyle', 'Dustin']

index = 0
for name in names:
    print(index,name)
    index+=1


#---------------------------------------------------------------
for index, name in enumerate(names, start=1):
    print(index, name)

#enumerate - index까지 같이 이용할 때 사용

#--------------------------------------------------------------

names = ['Ryan', 'Sam', 'Mickey', 'Lacey', 'Nyle', 'Dustin']
countries = ['Korea', 'Switzerland', 'USA', 'Canada', 'Brazil', 'China']

for index, name in enumerate(names):
    country = countries[index]
    print(f'{name} is from {country}')

#--------------------------------------------------------------

names = ['Ryan', 'Sam', 'Mickey', 'Lacey', 'Nyle', 'Dustin']
countries = ['Korea', 'Switzerland', 'USA', 'Canada', 'Brazil', 'China']

for name, country in zip(names, countries):
    print(f'{name} is from {country}')

for value in zip(names, countries):
    print(value) #print tuple
    
#다중 list 같이 묶을 때 한번에 사용가능 - 순서대로 (3개이상 list도 한번에 가능)
