# Creating a Set
my_set = {1, 2, 3, 4, 5}

# add()
my_set.add(6)

# copy()
copied_set = my_set.copy()

# difference()
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
difference_set = set1.difference(set2)

# difference_update()
set1.difference_update(set2)

# discard()
my_set.discard(3)

# intersection()
intersection_set = set1.intersection(set2)

# intersection_update()
set1.intersection_update(set2)

# isdisjoint()
are_disjoint = set1.isdisjoint(set2)

# issubset()
is_subset = set1.issubset(set2)

# issuperset()
is_superset = set1.issuperset(set2)

# pop()
popped_element = my_set.pop()

# remove()
my_set.remove(4)

# symmetric_difference()
symmetric_difference_set = set1.symmetric_difference(set2)

# symmetric_difference_update()
set1.symmetric_difference_update(set2)

# union()
union_set = set1.union(set2)

# update()
my_set.update({7, 8, 9})

# clear()
my_set.clear()

# Printing Results
print("Original Set:", my_set)
print("Copied Set:", copied_set)
print("Difference Set:", difference_set)
print("Updated Set after Difference:", set1)
print("Intersection Set:", intersection_set)
print("Updated Set after Intersection:", set1)
print("Are Sets Disjoint:", are_disjoint)
print("Is set1 a Subset of set2:", is_subset)
print("Is set1 a Superset of set2:", is_superset)
print("Popped Element:", popped_element)
print("Symmetric Difference Set:", symmetric_difference_set)
print("Updated Set after Symmetric Difference:", set1)
print("Union Set:", union_set)


