# python lists & arrays
import array as arr

# list to array

numlist = [1, 2, 3, 4, 5]

num_array = arr.array('i', numlist)

print(type(num_array))

#challenge

multiply_five = []

multiply_five.append(5 * 0)
multiply_five.append(5 * 1)
multiply_five.append(5 * 2)
multiply_five.append(5 * 3)
multiply_five.append(5 * 4)
multiply_five.append(5 * 5)
multiply_five.append(5 * 6)
multiply_five.append(5 * 7)
multiply_five.append(5 * 8)
multiply_five.append(5 * 9)
multiply_five.append(5 * 10)
multiply_five.append(5 * 11)
multiply_five.append(5 * 12)

print(multiply_five)

multiply_five.pop(5)

print(multiply_five)

multiply_five.insert(5, 25)

print(multiply_five)

multiply_five.pop()

print(multiply_five)

print(multiply_five[5])

print(multiply_five.index(40))

print(multiply_five.count(5))

