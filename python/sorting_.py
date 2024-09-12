# - (-) means bigger will come first
# - (reversed) means sorting reverse
# - -ord(item[1]) for sorting string using unicode
# - for bolean false will come first becasue false is 0 and true is 1
# - (sort and sorted ) Both will sort the list of strings alphabetically, but the key difference is that strs.sort() modifies the list in place, while sorted() returns a new sorted list without modifying the original list.


# Example 1: Sorting a list of tuples by the second element in descending order
from datetime import datetime


tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
sorted_tuples = sorted(tuples, key=lambda item: item[1], reverse=True)
print("Sorted tuples by second element (descending):", sorted_tuples)

# Example 2: Sorting a list of dictionaries by a specific key (age) first by descending age then accesnding name
list_of_dicts = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 30}, {'name': 'Anni', 'age': 30} ]
sorted_list = sorted(list_of_dicts, key=lambda item: (-item['age'], item['name']))
print("Sorted list of dictionaries by age:", sorted_list)

# Example 3: Sorting a dictionary by values in ascending order
map = {'apple': 10, 'banana': 5, 'cherry': 7}
sorted_dict = dict(sorted(map.items(), key=lambda item: item[1]))
print("Sorted dictionary by values (ascending):", sorted_dict)

# Example 4: Sorting a list of strings by length
strings = ['apple', 'banana', 'cherry', 'date']
sorted_strings = sorted(strings, key=len)
sorted_strings2 = sorted(strings, key= lambda x: x)
print("Sorted strings by length:", sorted_strings)
print("Sorted strings by lexogirally:", sorted_strings2)


strs = ['banana', 'apple', 'cherry', 'date']
strs.sort()
print("Sorted list using strs.sort():", strs)

strs = ['banana', 'apple', 'cherry', 'date']
sorted_strs = sorted(strs)
print("Sorted list using sorted():", sorted_strs)


# # Example 5: Sorting a list of numbers with custom sorting (even numbers first, then odds)
# numbers = [1, 4, 3, 2, 5, 6]
# sorted_numbers = sorted(numbers, key=lambda x: (x % 2, x))
# print("Sorted numbers (evens first):", sorted_numbers)

# # Example 6: Primary, secondary, and tertiary sorting
# # Sorting a list of tuples by the first element in ascending order (primary),
# # second element in descending order (secondary), and third element (if exists) in ascending order (tertiary)
# complex_tuples = [(1, 'c', 7), (2, 'b', 9), (1, 'a', 5), (2, 'b', 3)]
# sorted_complex_tuples = sorted(complex_tuples, key=lambda item: (item[0], -ord(item[1]), item[2]))
# print("Sorted by primary (first element), secondary (second element descending), tertiary (third element ascending):", sorted_complex_tuples)


# employees = [
#     {'bad_actor': True, 'emp_id': 103, 'temp_emp': False},
#     {'bad_actor': True, 'emp_id': 113, 'temp_emp': False},
#     {'bad_actor': False, 'emp_id': 101, 'temp_emp': True},
#     {'bad_actor': True, 'emp_id': 105, 'temp_emp': True},
#     {'bad_actor': False, 'emp_id': 102, 'temp_emp': False},
#     {'bad_actor': False, 'emp_id': 104, 'temp_emp': True},
# ]

# # Sort by bad_actor (False first), then temp_emp (True first), and finally emp_id (ascending)
# sorted_employees = sorted(employees, key=lambda item: (item['bad_actor'], -item['temp_emp'], item['emp_id']))
# print("Sorted employees by 'bad_actor', 'temp_emp', and 'emp_id':", sorted_employees)

# # Example 8: Sorting by date
# events = [
#     {'event': 'Event 1', 'date': '2024-09-10'},
#     {'event': 'Event 2', 'date': '2023-12-25'},
#     {'event': 'Event 3', 'date': '2024-01-01'},
#     {'event': 'Event 4', 'date': '2023-11-15'},
# ]

# # Convert the date strings to datetime objects for sorting
# sorted_events = sorted(events, key=lambda item: datetime.strptime(item['date'], '%Y-%m-%d'))
# print("Sorted events by date:", sorted_events)