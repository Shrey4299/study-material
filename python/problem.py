from functools import reduce


numbers = [1,2,3,4,5,6,7,8,9]

squared_num = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_num)

even_num = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_num)

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_of_numbers)