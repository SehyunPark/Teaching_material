
# import re

# hand = open('C:/Users/harry/OneDrive/Desktop/mbox-short.txt')

# for line in hand:
#     line = line.rstrip()

#     if re.search('$edu. ', line): #edu.으로 끝나는 line
#         print(line)

#----------------------------------------------------------
# for line in hand:
#     line = line.rstrip()

#     if re.search('^F..m:', line): #F로 시작하고 두 문자가 들어가고 m:으로 시작하는 line
#         print(line)

# for line in hand:
#     line = line.rstrip()

#     if re.search('^From: .+@', line): #From:으로 시작하고 한 개 이상의 문자로 이루어지고 @
#         print(line)

# for line in hand:
#     line = line.rstrip()

#     if re.search('^From: .+@', line): #From:으로 시작하고 한 개 이상의 문자로 이루어지고 @
#         print(line)

# s = 'hello, this is ryan@from another universe.'
# lst = re.findall('\S+@\S+', s) #findall()로 regular expression 문법 적용, list로 반환
# #@을 포함한 한 단어를 출력할 때 씀
# print(lst)

# import re
# hand = open('C:/Users/harry/OneDrive/Desktop/mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('\S+@\S+', line)
#     if len(x) > 0:
#         print(x) #@을포함한 모든 단어가 출력됨

# import re
# hand = open('C:/Users/harry/OneDrive/Desktop/mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
#     if len(x) > 0:
#         print(x) #@을포함한 모든 단어가 출력됨

# import re #quiz 문제
# hand = open('C:/Users/harry/OneDrive/Desktop/mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
#     if len(x) > 0:
#         print(x)


# import re 
# hand = open('C:/Users/harry/OneDrive/Desktop/mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('^From .* ([0-9][0-9]):', line)
#     if len(x) > 0: print(x)



