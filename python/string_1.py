# Creating Strings
my_string = "Hello, World!"

# String Concatenation
str1 = "Hello"
str2 = " World"
result_concatenation = str1 + str2

# String Repetition
my_string_repeated = "abc" * 3

# Length of a String
length = len(my_string)

# String Formatting
name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)

# String Indexing and Slicing
char = my_string[0]
substring = my_string[1:4]

# Changing Case
upper_case = my_string.upper()
lower_case = my_string.lower()
reversed_string = my_string[::-1] 

# Checking Substrings
contains_hello = "Hello" in my_string

# Replacing Substrings
new_string = my_string.replace("Hello", "Hi")

# Splitting and Joining
my_string_to_split = "apple,orange,banana"
fruits_list = my_string_to_split.split(',')
joined_string = '-'.join(fruits_list)

# Stripping Whitespace
my_string_with_whitespace = "   Hello, World!   "
stripped_string = my_string_with_whitespace.strip()

# Escape Characters
escaped_string = "This is a line\nwith a newline character."

# Raw Strings
raw_string = r"This is a raw string\nIt treats \n as text, not a newline."

# More Useful String Methods

# Counting Occurrences
my_string_to_count = "banana"
count_b = my_string_to_count.count("b")

# Finding Substrings
index_of_n = my_string_to_count.find("n")
last_index_of_n = my_string_to_count.rfind("n")

# Check if String is Alphanumeric
is_alphanumeric = my_string.isalnum()

# Check if String is Numeric
is_numeric = my_string.isdigit()

# Check if String is in Title Case
is_title_case = my_string.istitle()

# Check if String is Upper or Lower Case
is_upper_case = my_string.isupper()
is_lower_case = my_string.islower()

# Capitalize the First Letter
capitalized_string = my_string.capitalize()

# Swap Case
swapped_case_string = my_string.swapcase()

# Centering a String
centered_string = my_string.center(20, "*")

# Zfill (Zero-fill) a Number
zfilled_number = "42".zfill(5)

# String Formatting (f-strings, Python 3.6+)
name = "Bob"
age = 25
formatted_string_f = f"Hello, my name is {name} and I am {age} years old."

# Printing Results
print("Original String:", my_string)
print("Result of Concatenation:", result_concatenation)
print("Repeated String:", my_string_repeated)
print("Length of String:", length)
print("Formatted String:", formatted_string)
print("Indexed Character:", char)
print("Substring:", substring)
print("Uppercase:", upper_case)
print("Lowercase:", lower_case)
print("Contains 'Hello':", contains_hello)
print("String after Replacement:", new_string)
print("List of Fruits:", fruits_list)
print("Joined String:", joined_string)
print("Stripped String:", stripped_string)
print("String with Escape Characters:", escaped_string)
print("Raw String:", raw_string)

# Additional Useful String Methods
print("Occurrences of 'b':", count_b)
print("Index of 'n':", index_of_n)
print("Last Index of 'n':", last_index_of_n)
print("Is Alphanumeric:", is_alphanumeric)
print("Is Numeric:", is_numeric)
print("Is Title Case:", is_title_case)
print("Is Upper Case:", is_upper_case)
print("Is Lower Case:", is_lower_case)
print("Capitalized String:", capitalized_string)
print("Swapped Case String:", swapped_case_string)
print("Centered String:", centered_string)
print("Zfilled Number:", zfilled_number)
print("Formatted String (f-string):", formatted_string_f)
my_string = "Hello, World!"
for char in my_string:
    print(char)


my_string = "Hello, World!"
for i in range(len(my_string)):
    print(my_string[i])

my_string = "Hello, World!"
for index, char in enumerate(my_string):
    print(f"Index {index}: {char}")


