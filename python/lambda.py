# Example 1: Simple lambda function for addition
add = lambda x, y: x + y
print("Addition (5 + 3):", add(5, 3))

# Example 2: Lambda function for squaring a number
square = lambda x: x ** 2
print("Square of 4:", square(4))

# Example 3: Lambda function for filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Filtered even numbers:", even_numbers)


# Example 5: Lambda function for applying a transformation to a list (doubling the numbers)
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print("Doubled numbers:", doubled_numbers)

# Example 6: Lambda function for finding the maximum of two numbers
max_value = lambda a, b: a if a > b else b
print("Maximum of 10 and 20:", max_value(10, 20))

# Example 7: Lambda function with default arguments
multiply = lambda x, y=2: x * y
print("Multiply 5 by 2 (default):", multiply(5))  # Uses default y=2
print("Multiply 5 by 3:", multiply(5, 3))         # Overrides default value of y


# Example 9: Using lambda in reducing a list to a single value (sum of all elements)
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total_sum = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", total_sum)

# Example 10: Lambda function for conditional statements (checking if a number is even or odd)
even_or_odd = lambda x: 'Even' if x % 2 == 0 else 'Odd'
print("5 is:", even_or_odd(5))
print("10 is:", even_or_odd(10))
