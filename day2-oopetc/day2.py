import math
import csv

# functions - reusable blocks of code

# def hello(name):
#     return 'Hello' + ' ' + name
#
# hello('Michael')
# hello('Bob')
# hello('Minnie')
#
# name1 = hello('Michael')
# name2 = hello('Bob')
# name3 = hello('Minnie')
#
# print(name1, name2, name3)


# def add_three_nums(num1, num2, num3):
#     return num1 + num2 + num3
#
# print(add_three_nums(4, 5, 6))
# print(add_three_nums(5, 6, 7))
# print(add_three_nums(24, 78, 83))
#
# def num_squared(num1):
#     return num1 * num1
#
# print(num_squared(4))
# print(num_squared(57))
# print(num_squared(5400))

# def my_first_function(string):
#     return 'I love ' + string
#
# print(my_first_function('cats'))
#
# def tripler(num):
#     return num * 3
#
# print(tripler(5))
#
# def greet(name):
#     return 'Hello ' + name + '!'
#
#
# def is_even(num):
#     return num % 2 == 0
#
# print(is_even(5))
#
# """
# Write a function repeat_word(word, times)
#
#     It should return the word repeated times number of times.
#
# """
#
# def repeat_word(word, times):
#     return word * times
#
#
# print(repeat_word('cats', 3))
# print(repeat_word('dogs', 3))
#
#
# """
#
#  Write a function factorial(n) that calculates the factorial of n.
#
#     Example: factorial(5) → 5 * 4 * 3 * 2 * 1 = 120.
# """


## lambda functions

"""
Convert the following functions to lambda expressions:

import math

def circle_perimeter(radius):

    return 2 * math.pi * radius

 
def circle_area(radius):

    return math.pi * radius ** 2

"""

circle_perimeter_lambda = lambda radius: 2 * math.pi * radius

print(circle_perimeter_lambda(25))


circle_area_lambda = lambda radius: math.pi * radius ** 2

print(circle_area_lambda(57))

"""
def triangle_area(a, b, c):

    s = (a + b + c) / 2

    return math.sqrt(s * (s - a) * (s - b) * (s - c))

"""

#lambda inside function
def multiplier(n):
    return lambda x: x * n

doubler = multiplier(10)
tripler = multiplier(10)

print(doubler(3))
print(tripler(7))


# map with lambda

numbers = [2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(numbers)
print(doubled)

# filter with lambda

numbers = range(1, 10)
evens = list(filter(lambda x: x % 2 == 0, numbers))
odds = list(filter(lambda x: x % 2 != 0, numbers))

print(evens)
print(odds)


# sort()

## sorts items in a list in ascending order, either in value if integer or alphabetical if strings.

# reduce()

## used in combination with a function (eg. lambda) on an iterable, reduces a collection of elements into
## a singular value. it does this by performing a function on item a & b, then result & c, then result & d,
## and so on until all elements have been used and a final value is returned.


## working with .csv files

# comma separated

## reading
#
# rows = []
#
# with open('employees.csv', newline='') as csvfile:
#
#     csvreader = csv.reader(csvfile)
#     header = next(csvreader)
#     for row in csvreader:
#         rows.append(row)
#
#
#     print(rows)

## writing

# header = ['name', 'age']
#
# data = [['minnie', '12'], ['elaine', '78'], ['will', '50']]
#
# with open('ppl.csv', 'w', newline='') as csvfile:
#
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(header)
#     csvwriter.writerows(data)


# csv.DictReader()

with open('employees.csv', 'r', newline='') as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:
        print(row['Name'], row['email'])
        print(row)


# csv.DictWriter

headers = ['name', 'age']

data = [['minnie', '12'], ['elaine', '78'], ['will', '50']]

with open('ppl.csv', 'w', newline='') as csvfile:

    writer = csv.DictWriter(csvfile, fieldnames=headers)

    writer.writeheader()
    for person in data:
        writer.writerow({'name': person[0], 'age': person[1]})







