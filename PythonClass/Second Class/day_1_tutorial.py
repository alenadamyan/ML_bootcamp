import time
import sys

# from math import pi
# """Basic types and variables"""
# x = 5
# y = True
# s = 'S'
# f = 5.0
#
# print('Type of x is: ', type(x))
# print('Type of y is: ', type(y))
# print('Type of s is: ', type(s))
# print('Type of f is: ', type(f))
#
# print(1, 2, 3, 4, 5, 6, 7, 8)
#
# # print('f is of type', type(int(f)))
# # print('x is of type', type(float(x)))
#
# """Strings"""
#
# s_1 = 'This is a string'
# s_2 = "This is another string"
#
# print(s_1)
# print(s_2)
#
# s_1 = "My name's Hrach"
# s_2 = 'My name\'s Hrach'
#
# s_3 = "Name of this var is \"s_3\""
# print(s_3)
#
# s_4 = """This is the first line
# this is the second line
# and the third is here"""
#
# s_5 = 'This is the first line\n\
# this is the second line\n\
# and the third is here'
# print(s_5)
#
# """Escape characters"""
#
# # \n - new line
# # \t - tab
# # \b - backspace
# # \s - space
#
# print(r'This\t should be\b \n separated')
# s_1 = 'One'
# s_2 = 2
#
# print(s_1 + str(s_2))
# print('=' * 100)
#
# """Arithmetic operators"""
#
# # +, -, /, *, %, //, **
#
# x = 6
# y = 4
# print('x + y: ', x + y)
# print('x - y: ', x - y)
# print('x / y: ', x / y)
# print('x * y: ', x * y)
# print('x % y: ', x % y)
# print('x // y: ', x // y)
# print('x ** y: ', x ** y)
# int()
# print(dir(x))
#
# """Logical operators"""
#
# # ==   - True if equal, False otherwise
# # !=   - False if equal, True otherwise
# # >    - True if left operand > right operand
# # >=   - True if left operand >= right operand
# # <    - True if left operand < right operand
# # <=   - True if left operand <= right operand
# # not  - negates the value after
# # is   - True if the objects are the same, False otherwise
# # x in y  - True if y contains x
#
# y = [2, 3]
# u = [2, 3]
# print(hex(id(y[0])))
# print(hex(id(u[0])))
#
# y = 2
# u = 2
# print(hex(id(y)))
# print(hex(id(u)))
# # print(hex(id('s')))
# # 0x1cf46dd2530
# # 0x20e0d0e2530
# print(y is u)
#
# x = 6
# y = 7
# print('x == y: ', x == y)
# print('x != y: ', x != y)
# print('x > y: ', x > y)
# print('x < y: ', x < y)
# print('x <= y: ', x <= y)
# print('x >= y: ', x >= y)
#
# string = 'This is a string'
# string_1 = ''
# print('s in string: ', 's' in string)
# print('s not in string: ', 's' not in string)
# print(not string)
#
# """Truthy and Falsy values"""
# print('=' * 50)
# print(bool(string))
# print(bool(string_1))
#
# # Falsy values - 0, None, '', False, [], ()...
# lst = [None, None,]
# print(4 is 4.0)
# print(len(lst))
#
# """String methods"""
#
# string = 'This is a string'
# print(string.replace('s', 'p'))
# print('After replace: ', string)
# lst = string.split(' ')
# print(f'{lst=}')
# print(string.split(' '))
# print(string.count('is'))
# print(' '.join(lst))
# print(string.upper())
# print(string.lower())
#
# # isdecimal, isnumeric ... difference:
# # https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-python/44891278
#
# # More on str methods:
# # https://www.w3schools.com/python/python_ref_string.asp
#
# """String formatting"""
#
# x = 5
# y = 4214
# print('The value of x is', x)
# print('The value of x is ' + str(x))
#
# print('The value of x is {0}, {1}, {2}'.format(x, y, string))
# #
# print('The value of x is {0}, y is {1}, and again x is {0}'.format(x, y))
#
# print('=' * 50)
# print('The value of x is {0:<10}, y is {1:>10}, and again x is {0:^10}'.format(x, y))
#
# print('The value of x is {0:<10}, y is {1:>10}, and again x is {0:^10}'.format(x, y))
#
# print(pi)
# print('Value of pi is {:.4f}'.format(pi))
#
# # More on .format(): https://www.w3schools.com/python/ref_string_format.asp
#
# print(f'x is {x}')
# print(f'x is {x=}')
#
# # Python 2 style
# print('x is %d %d' % (x, y))
# print(len([1, 2, 3, 4]))
# ls = [1, 2, 3, 4]
#
# counter = 0
# for item in ls:
#     counter += 1
#
# print(counter)

"""Control flow"""
"""Conditional statements"""

# condition = False
# lst = []
# other_condition = False
#
# if condition:
#     print('Condition is true')
# elif other_condition:
#     print('Other condition is true')
# elif not other_condition:
#     print('Other condition is False')
# elif not condition:
#     print('Other condition is False')
# # else:
# #     print('Else is running')
#
# print('Rest of the code')
# if condition:
#     print('Condition is true')
# if other_condition:
#     print('Other condition is true')
# if not other_condition:
#     print('Other condition is False')
# if not condition:
#     print('Condition is False')
#
# # and, or
# print(True and False)
# # if False and True:
# #     print('Both conditions are true')
#
# # if True or False:
# #     print('One of the conditions is true')
#
# if (True or False) and (True or False):
#     print('One of the conditions is true')
#
# # Operator precedence: https://www.programiz.com/python-programming/precedence-associativity
#
# c = True
#
# if c:
#     x = 6
# else:
#     x = 7
# print(x)
#
# # Ternary operator
# x = 6 if c else 7
#
# print(x)
#
# x = 5
# y = 3
#
# if y > x:
#     if y % 2 == 0:
#         print('y > 0 and y is even')
#     else:
#         print('y > 0 and y is odd')
# else:
#     print('x < y')

"""Loops"""

# for i in range(0, 11, 1):
#     print(i)
#
# for i in range(10, -1, -1):
#     if i > 0:
#         print(i, end=" - ")
#     else:
#         print(i)
#
# print(1, 2, 3, 4, 5, 6, sep=" - ", end="s")
#
# x = 0
#
# while x < 11:
#     print(x)
#     # x = x + 1
#     x += 1

start_for = time.perf_counter()
x = 0
for i in range(100000):
    pass
end_for = time.perf_counter()
start_while = time.perf_counter()
x = 0
while x < 100000:
    x += 1

end_while = time.perf_counter()

print('For timer: ', end_for - start_for)
print('While timer: ', end_while - start_while)

lst = [i for i in range(100)]
gen = (i for i in range(0, 100, 2))
print(type(gen))
print(next(gen))
print(next(gen))

# for i in lst:
#     print(i)
#
# for i in gen:
#     print(i)

# for i in range(10):
#     print(i)
# else:
#     print('We\'re in the else clause')

# for i in range(10):
#     if i == 5:
#         break
#     print(i)
# else:
#     print('We\'re in the else clause')

x =0

while x < 11:
    if x == 5:
        x += 1
        continue
    print(x)
    x += 1
else:
    print('While else clause')

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

for i in range(10):
    for j in range(10):
        print(f'{j=}')
        break
    print(i)


"""Data structures: Lists, Tuples, Dictionaries, Sets"""

lst = [1, 3, 5, 3, 3, 4, 10]

# print(type(lst))
# print(lst[0])
# print(lst[4])
# print(lst[-2])
# print(lst[len(lst)])

# Slicing

# print(id(lst[:]))
# print(id(lst))
# print(list(reversed(lst)))
# print(lst[::-1])
#
# lst[1] = 5
# print(lst)
# string = 'Abc'
# string = string[0:1] + 's' + string[2:]
# print(string)
#
# # lst[0] = 1, 2, 3
# lst[1:] = [1, 2, 3, 5, 1, 2, 3, 4]
# print(lst)
#
# """List methods"""
#
# bad_list = [[], (), 'sdhasd', 5.4, 1, False]
# print(bad_list)
# lst.append([5])
# print(lst)
# x = lst.pop()
# print(lst, f'Popped element {x}')
# lst.remove(1)
# print(lst)
# lst.insert(2, True)
# print(lst)
print('This is a string'.count(' is '))

string = '      rrrrrrjasdkrasjrrrrr    '
print(string)
print(string.strip())
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))

a.pop()
print(a)
print(b)

b = a.copy()
b = a[:]
b = list(a)

# More on lists: https://www.w3schools.com/python/python_ref_list.asp

"""Tuples"""
print(True or True)
