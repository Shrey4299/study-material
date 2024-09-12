from collections import defaultdict

def defaultdict_examples():
    print("Defaultdict Examples:\n")
    
    # Example 1: Defaultdict with int
    # Defaultdict initialized with int will provide a default value of 0 for any new key
    int_dict = defaultdict(int)
    int_dict['apple'] += 1
    int_dict['banana'] += 2
    print("Example 1 - defaultdict with int:")
    print(int_dict)  # Output: defaultdict(<class 'int'>, {'apple': 1, 'banana': 2})
    print()

    # Example 2: Defaultdict with list
    # Defaultdict initialized with list will provide an empty list for any new key
    list_dict = defaultdict(list)
    list_dict['fruits'].append('apple')
    list_dict['fruits'].append('banana')
    list_dict['vegetables'].append('carrot')
    print("Example 2 - defaultdict with list:")
    print(list_dict)  # Output: defaultdict(<class 'list'>, {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']})
    print()

    # Example 3: Defaultdict with set
    # Defaultdict initialized with set will provide an empty set for any new key
    set_dict = defaultdict(set)
    set_dict['fruits'].add('apple')
    set_dict['fruits'].add('banana')
    set_dict['vegetables'].add('carrot')
    set_dict['fruits'].add('apple')

    print("Example 3 - defaultdict with set:")
    print(set_dict)  # Output: defaultdict(<class 'set'>, {'fruits': {'apple', 'banana'}, 'vegetables': {'carrot'}})
    print()

    # Example 4: Using defaultdict with custom factory function
    # Defaultdict initialized with a custom factory function
    def default_value():
        return "default_value"

    custom_dict = defaultdict(default_value)
    custom_dict['key1'] = 'value1'
    print("Example 4 - defaultdict with custom factory function:")
    print(custom_dict['key1'])  # Output: value1
    print(custom_dict['key2'])  # Output: default_value
    print()

    # Example 5: Counting items using defaultdict
    # Defaultdict with int to count occurrences
    items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    count_dict = defaultdict(int)
    for item in items:
        count_dict[item] += 1
    print("Example 5 - Counting items using defaultdict:")
    print(count_dict)  # Output: defaultdict(<class 'int'>, {'apple': 2, 'banana': 3, 'orange': 1})

if __name__ == "__main__":
    defaultdict_examples()
