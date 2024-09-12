# Creating a Dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}

# Accessing Values
name = my_dict['name']

# Adding or Modifying Elements
my_dict['occupation'] = 'Engineer'
my_dict['age'] = 26

# Removing Elements
del my_dict['city']
popped_value = my_dict.pop('age')

# Checking Membership
key_exists = 'name' in my_dict

# Dictionary Methods
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()
default_value = my_dict.get('nonexistent_key', 'default')

# Additional Dictionary Functions
# my_dict.clear()
copied_dict = my_dict.copy()

# Using fromkeys()
keys_to_create = ['name', 'age', 'occupation']
default_value_for_keys = 'Unknown'
created_dict = dict.fromkeys(keys_to_create, default_value_for_keys)

# Using popitem() with check for an empty dictionary
last_inserted_pair = my_dict.popitem() if my_dict else None

# Using setdefault()
age = my_dict.setdefault('age', 30)

# Using update()
my_dict.update({'location': 'Unknown', 'occupation': 'Data Scientist'})

# Looping Through a Dictionary
print("Looping Through Keys:")
for key in my_dict:
    print(key, my_dict[key])

print("\nLooping Through Items:")
for key, value in my_dict.items():
    print(key, value)

print("\nLooping Through Values:")
for value in my_dict.values():
    print(value)



# Printing Results
print("\nOriginal Dictionary:", my_dict)
print("Name:", name)
print("Updated Dictionary:", my_dict)
print("Key 'name' exists:", key_exists)
print("Keys:", keys)
print("Values:", values)
print("Items:", items)
print("Default Value:", default_value)
print("Popped Value:", popped_value)
print("Cleared Dictionary:", my_dict)
print("Copied Dictionary:", copied_dict)
print("Created Dictionary with fromkeys():", created_dict)
print("Last Inserted Pair using popitem():", last_inserted_pair)
print("Age using setdefault():", age)
print("Updated Dictionary using update():", my_dict)

# sorted_dict = dict(sorted(map.items(), key=lambda item: (-item[1], item[0]))) sort by value then , alphabetically


words = ["i","love","leetcode","i","love","coding"]

map = {}

for word in words:
    map[word] = map.get(word, 0) + 1


from collections import defaultdict

# Example data
data = {
    "cherry": 3,
    "apple": 3,
    "elderberry": 2,
    "banana": 2,
    "date": 1,   
}

# Create a defaultdict of lists to hold arrays of strings for each frequency
frequency_dict = defaultdict(list)

# Populate the dictionary
for string, freq in data.items():
    frequency_dict[freq].append(string)
    frequency_dict[freq].sort()

# Convert defaultdict to a regular dict if needed
# frequency_dict = dict(frequency_dict)

print("Frequency Dictionary:")
print(frequency_dict)


# Flatten the frequency_dict values into a single sorted list of strings
sorted_strings = []
for freq in (frequency_dict.keys()):
    sorted_strings.extend(frequency_dict[freq])

print("Flat Sorted List of Strings:")
print(sorted_strings)