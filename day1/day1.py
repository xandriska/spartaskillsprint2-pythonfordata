import sys

print('I love bugs')
print('I love knitting')
print('I hate Hollow Knight')

# python basics

favourite_food = 'pasta'

birth_year = 1989

print(f'I was born in {birth_year} and my favourite food is {favourite_food}.')
#
# # primitive types
#
# # int --> whole nums
# # float --> decimal nums
# # str --> text 'blah blah'
# # bool --> true/false
#
# # types code-along
#
# # int
#
num1 = 1
print(num1)
print(type(num1))
print(sys.getsizeof(num1))
#
# #float
#
float1 = 1.0
print(type(float1))
print(sys.getsizeof(float1))
#
string1 = 'string'
print(type(string1))
print(sys.getsizeof(string1))

# casting (type conversion)

# between COMPATIBLE types: int --> float, bool --> int)
# NOT string --> int (works if str is numeric)

my_num = 5

my_float = float(my_num)

print(my_float)

my_str = '123'

my_int = int(my_str)

print(my_int)

my_num_input = int(input("Enter a number: ")) # will be str by default - cast to preferred type

print(my_num_input)

user_age = int(input("Enter your age: "))

print(f'You are {user_age} years old.')

get_float = float(input("Enter a decimal number: "))

print(type(get_float), get_float)

get_num1 = int(input("Enter a number: "))

get_num2 = int(input("Enter another number: "))

print('The sum of these numbers is:', get_num1 + get_num2)

print('Hi' * 3)

print(10 > 5)

#challenge 1
num_to_cast = float(input("Enter a number: "))

divided = int(num_to_cast) // 2

user_name = input("Enter your name: ")
print('Hello', user_name, '!')

#challenge 2

height = int(input("Enter the height: "))

width = int(input("Enter the width: "))

area = height * width

print('The area of the rectangle is', area)






