from functools import partial, reduce
import itertools




# Generator Examples

# Example 1: Simple generator function that yields numbers from 1 to 3
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print("Generated values:", list(gen))

# Example 2: Generator expression to yield squared numbers from 1 to 5
squared_gen = (x**2 for x in range(1, 6))
print("Squared numbers:", list(squared_gen))

# Example 3: Generator function for Fibonacci sequence
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_gen()
print("First 5 Fibonacci numbers:", [next(fib) for _ in range(5)])


# Decorator Examples

# Example 1: Simple decorator that prints a message before and after the function call
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@simple_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Example 2: Decorator that measures the execution time of a function
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Finished!"

print(slow_function())


# Using next and iter

# Example 1: Using `iter` and `next` to iterate over a range of numbers
numbers_iter = iter(range(5))
print("Using iter and next:")
for _ in range(5):
    print(next(numbers_iter), end=' ')
print()

# Example 2: Using `iter` with a sentinel value
def read_until_sentinel():
    while True:
        value = input("Enter a value (or 'done' to stop): ")
        if value == 'done':
            break
        yield value

sentinel_iter = read_until_sentinel()
print("Values entered:")
for value in sentinel_iter:
    print(value)
