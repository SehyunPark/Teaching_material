#list comprehension

array = []

for i in range(0,20,2):
    array.append(i*i)

print(array)

#-------------------------------

array = [i*i for i in range(0,20,2)]
print(array)

array = [i*i for i in range(0,20,2) if i%4 == 0]
print(array)