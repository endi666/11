# print("hey sosun")
# a=2
# n=7
# j=14
# print(a+n+j)
# if a%6:
#     print(1)
# else:
#     print(3)

# a='Abrakadabra'
# print(n[0:5])
# print(n[::-1])
# print(n[0:9])
# print(n[::2])
# print(n[1::2])
# print(n[::-2])


# print(a)
# c='a' in a
# d='e' in a
#
# print(c, d)
#
# print('a'.isupper())
# print('A'.isupper())
#
# data=input()
# if data.isupper():
#  print('DA BLYAT')
# else:
#  print('hell nah')

# data=input()
# if len(data)>3:
#  if '*' in data:
#    if data.isupper():
#     print('YUH WELCUM TO THE CLUB BUDDY')
#    else:
#     print('NAH BUDDY')
#
# for i in range(2,10,2):
#     print(i)
# a = [1,2,3,4,5]
# print(a[2])
# for i in range(len(a)):
#     print(a[i],i)
# a=[1,2,5,4,2,3]
# for i in range(2,10,2):
#     a.append(i)
# print(a)
# b = 0
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         b = b + a[i]
# print(b)


    # b=b*a[i]
# print(b)
# n=0
# c='Abrakadabra'
# for i in range(len(c)):
#     if c[i]=='a':
#         n=n+1
#print(n)

# a=[1,12,4,7,37,27,95,2,8,14,26]
# for i in range(len(a)):
#     print(a[i])
    # print(a)
# import random
#
# marks=[random.randint(4,5) for i in range(10)]
# print(marks)
# b=0
# for i in range(len(marks)):
#     b=marks[i]+b
# average=b/len(marks)
# if average >=4:
#     print('pozdravlyau')
# else:
#     print('nah youre a fool')

# i=5
#
# while i<10:
#     print(i)
#     i+=1

# while True:
#     print('yah')

# import random
# a= random.randint(-12,11)
# print(a)
#
# action=input('tvoye deystviye:')
# myscore=0
# kazinichscore=0
# while action=='ONE MORE CARD AH' and myscore<21 and kazinichscore<21:
#     myscore+=random.randint(3,11)
#     kazinichscore+= random.randint(3, 11)
#     print(myscore)
#     action=input('tvoye deystviye:')
'# if myscore or kazinichscore'
from os.path import split
from turtledemo.sorting_animate import instructions1

from pyexpat.errors import XML_ERROR_UNCLOSED_CDATA_SECTION

# a = input()
# i = 1
# print(a)
# while i < len(a):
#     print(a[0:-i])
#     i += 1

# def build_box(width, height):
#     roof = '*' * width
#     roof = list(roof)
#     roof = ''.join(roof)
#     print(roof)
#     for i in range(height - 2):
#         middle = '*' + ' ' * (width - 2) + '*'
#         middle = list(middle)
#         middle[1] = ' '
#         middle = ''.join(middle)
#         print(middle)
#     print(roof)
#
# build_box(4, 4)


# a = 'zepa'
# a = list(a)
# a[1] = '*'
# a = ''.join(a)
# print(a)

# coordinates = [5,3]
# instructions = ['left','left','left','up']
#
# def change_coordinates(cords, instr):
#     for instruction in instr:
#         if 'left' == instruction:
#             coordinates[0] -= -1
#         elif 'down' == instruction:
#             coordinates[1] -= -1
#         elif 'up' == instruction:
#             coordinates[1] -= 1
#         elif 'down' == instruction:
#             coordinates[0] -= 1
# print()

# a = [4, 1, 2, 3, 5]
# # print(a[2])
# for i in range(len(a)):  # 0 - len(a)
#     print(a[i])


#
# txt = "mama,papa,cat"
#
# x = txt.split("")
#
# print(x)

# words = input()
# words = words.split()
#
# for word in words:
#     # print(word, '-', word.count('a'))
#     counter = 0
#     counter2 = 0
#     for symbol in word:
#         if symbol == 'a' or symbol == 'm':
#             counter += 1
#
#
# # for symbol in word:
# #         if symbol == 'm':
# #             counter2 += 1
#     print(word, counter)


with open("scores") as file:
    file = file.readlines()
    print(file)
    lines = [line.split() for line in file]
    print(lines)
    for i in range(len(lines)):
        lines[i][2] = int(lines[i][2])
    # print(lines)
a = sorted(lines, key=lambda x:x[-1])
b = sorted(a, key=lambda x:x[0])
c = sorted(b, key=lambda x:x[1])
d = sorted(c, key=lambda x:x[2])
# print(d)
#
# for i in range(len(lines)):              # daldvniaqnhsefvqfrvqorgfqrg
#     lines[i][1]
# e = sorted(d, key=lambda x:x[1])
# print(e)