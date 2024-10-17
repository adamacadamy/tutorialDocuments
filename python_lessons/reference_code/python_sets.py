# Set operations in Python with examples

# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# add(): Adds a single element to the set
my_set.add(6)
print("After add(6):", my_set)

# update(): Adds multiple elements to the set
my_set.update([7, 8, 9])
print("After update([7, 8, 9]):", my_set)

# remove(): Removes an element from the set (raises KeyError if not found)
my_set.remove(9)
print("After remove(9):", my_set)

# discard(): Removes an element from the set (does not raise an error if not found)
my_set.discard(10)  # No error even if 10 is not in the set
print("After discard(10):", my_set)

# pop(): Removes and returns an arbitrary element from the set
popped_element = my_set.pop()
print(f"After pop(), popped element: {popped_element}, Set now:", my_set)

# clear(): Removes all elements from the set
my_set.clear()
print("After clear(), set:", my_set)

# Re-creating a new set for more examples
my_set = {1, 2, 3, 4, 5}
another_set = {4, 5, 6, 7}

# union(): Returns a new set with all elements from both sets
union_set = my_set.union(another_set)
print("Union of my_set and another_set:", union_set)

# intersection(): Returns a new set with only the common elements
intersection_set = my_set.intersection(another_set)
print("Intersection of my_set and another_set:", intersection_set)

# difference(): Returns a new set with elements in the first set but not in the second
difference_set = my_set.difference(another_set)
print("Difference of my_set and another_set:", difference_set)

# symmetric_difference(): Returns a new set with elements in either set but not both
symmetric_difference_set = my_set.symmetric_difference(another_set)
print("Symmetric difference of my_set and another_set:", symmetric_difference_set)

# issubset(): Checks if the set is a subset of another set
is_subset = {1, 2}.issubset(my_set)
print("{1, 2} is a subset of my_set:", is_subset)

# issuperset(): Checks if the set is a superset of another set
is_superset = my_set.issuperset({1, 2})
print("my_set is a superset of {1, 2}:", is_superset)

# isdisjoint(): Checks if the sets have no elements in common
is_disjoint = my_set.isdisjoint({6, 7, 8})
print("my_set is disjoint with {6, 7, 8}:", is_disjoint)

# copy(): Returns a shallow copy of the set
copied_set = my_set.copy()
print("Copied set:", copied_set)

# Checking set membership using 'in'
is_3_in_set = 3 in my_set
print("Is 3 in my_set:", is_3_in_set)

# Iterating through a set
print("Iterating through my_set:")
for element in my_set:
    print(element)
