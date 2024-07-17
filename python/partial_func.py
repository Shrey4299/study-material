from functools import partial


# Original function
def power(base, exponent):
    return base**exponent


# Creating a partial function with base fixed to 2
square = partial(power, base=2)

# Using the partial function to calculate squares
print(square(exponent=2))  # Output: 4
print(square(exponent=3))  # Output: 8
print(square(exponent=4))  # Output: 16
