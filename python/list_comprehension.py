# list_comprehension_examples.py

print("List Comprehension Examples:\n")

# Example 1: Basic List Comprehension
# Creating a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print("Example 1 - Basic List Comprehension:")
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print()

# Example 2: List Comprehension with Conditional
# Creating a list of even squares of numbers from 0 to 9
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Example 2 - List Comprehension with Conditional:")
print(even_squares)  # Output: [0, 4, 16, 36, 64]
print()

# Example 3: Nested List Comprehension
# Flattening a matrix (list of lists) into a single list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [elem for row in matrix for elem in row]
print("Example 3 - Nested List Comprehension:")
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print()

# Example 4: List Comprehension with Function Application
# Applying a function to each element in a list
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print("Example 4 - List Comprehension with Function Application:")
print(doubled)  # Output: [2, 4, 6, 8, 10]
print()

# Example 5: List Comprehension with Multiple Iterators
# Generating pairs (i, j) where i is from 0 to 2 and j is from 0 to 2
pairs = [(i, j) for i in range(3) for j in range(3)]
print("Example 5 - List Comprehension with Multiple Iterators:")
print(pairs)  # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
print()

# Example 6: List Comprehension with String Manipulation
# Converting a list of strings to uppercase
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print("Example 6 - List Comprehension with String Manipulation:")
print(uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']
print()

# Example 7: Flattening a List of Lists
# Flattening a list of lists into a single list
list_of_lists = [[1, 2, 3], [4, 5], [6]]
flattened_list = [item for sublist in list_of_lists for item in sublist]
print("Example 7 - Flattening a List of Lists:")
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]
print()

# Example 8: List Comprehension with Conditional Expression
# Creating a list with 'even' or 'odd' based on the number
numbers = [1, 2, 3, 4, 5]
even_odd = ['even' if x % 2 == 0 else 'odd' for x in numbers]
print("Example 8 - List Comprehension with Conditional Expression:")
print(even_odd)  # Output: ['odd', 'even', 'odd', 'even', 'odd']
print()

# Example 9: List Comprehension with Dictionary Values
# Extracting the values from a dictionary
data = {'a': 1, 'b': 2, 'c': 3}
values = [value for key, value in data.items()]
print("Example 9 - List Comprehension with Dictionary Values:")
print(values)  # Output: [1, 2, 3]
print()

# Example 10: List Comprehension with Enumeration
# Getting indices and values from a list
items = ['apple', 'banana', 'cherry']
indexed_items = [f"{index}: {item}" for index, item in enumerate(items)]
print("Example 10 - List Comprehension with Enumeration:")
print(indexed_items)  # Output: ['0: apple', '1: banana', '2: cherry']


# Example 11 - List Comprehension with set
query = 'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'

result = [set(x for x in query if x.lower() not in ("a", "e", "i", "o", "u", " ") )]


# Example 12 - List Comprehension with set and two loops
result = list(set(x for x in range(1,1001) for y in range (2,10) if x % y == 0))
