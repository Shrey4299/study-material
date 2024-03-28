# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


# Creating a List
my_list = [1, 2, 3, 4, 5]

# Accessing Elements
first_element = my_list[0]

# Slicing
subset = my_list[1:4]

# Length of a List
length = len(my_list)

# Appending and Extending
my_list.append(6)
my_list.extend([7, 8])

# Inserting at a Specific Position
my_list.insert(2, 10)

# Removing Elements
my_list.remove(4)
popped_element = my_list.pop()

# Checking Membership
contains_3 = 3 in my_list

# Counting Occurrences
count_2 = my_list.count(2)

# List Comprehensions
squared_numbers = [x**2 for x in my_list]
even_numbers = [x for x in my_list if x % 2 == 0]

# Sorting and Reversing
my_list.sort()
sorted_list = sorted(my_list)
my_list.reverse()

# Copying Lists
copied_list = my_list.copy()

# Additional Functions
index_of_3 = my_list.index(3)
my_list.clear()

# Joining Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2

# Repeating a List
repeated_list = my_list * 3

# Filtering with a Function
def is_even(x):
    return x % 2 == 0

def square(x):
    return  x**2

filtered_list = list(filter(is_even, my_list))

# Using map function
map_list = list(map(square, my_list))

add_lambda = lambda x, y: x + y

result_lambda = add_lambda(3, 5)
print(result_lambda)  


# List Comprehension Example
squares_of_even_numbers = [x**2 for x in my_list if x % 2 == 0]

# Printing Results
print("Original List:", my_list)
print("First Element:", first_element)
print("Subset:", subset)
print("Length of List:", length)
print("Appended and Extended List:", my_list)
print("Popped Element:", popped_element)
print("Contains 3:", contains_3)
print("Occurrences of 2:", count_2)
print("Squared Numbers:", squared_numbers)
print("Even Numbers:", even_numbers)
print("Squares of Even Numbers (List Comprehension):", squares_of_even_numbers)
print("Sorted List:", sorted_list)
print("Reversed List:", my_list)
print("Copied List:", copied_list)
print("Index of 3:", index_of_3)
print("Cleared List:", my_list)
print("Combined List:", combined_list)
print("Repeated List:", repeated_list)
print("Filtered List (Even Numbers):", filtered_list)
print("Map List (square):", map_list)


nums = [1,2,3,4]
sub_nums = nums[2:3]
print(len(nums))
nums2 = [6,6,6]
mixed = nums+sub_nums
nums.pop()

for items in nums:
    print(items)

for x in range(len(nums)):
    print(nums[x])

for x in range(2,3):
    print(mixed[x])

[print(item) for item in nums]

# Using enumerate to get both index and value
for index, value in enumerate(nums):
    print(f"Index: {index}, Value: {value}")

