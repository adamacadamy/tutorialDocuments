# Tuple operations in Python with examples

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)

# Accessing elements using indexing
first_element = my_tuple[0]
print("First element:", first_element)

# Accessing elements using negative indexing
last_element = my_tuple[-1]
print("Last element:", last_element)

# Slicing a tuple
slice_tuple = my_tuple[1:4]
print("Slice from index 1 to 4:", slice_tuple)

# count(): Returns the count of how many times an element appears in the tuple
count_of_3 = my_tuple.count(3)
print("Count of element 3:", count_of_3)

# index(): Returns the index of the first occurrence of an element
index_of_4 = my_tuple.index(4)
print("Index of element 4:", index_of_4)

# length of a tuple using len()
length_of_tuple = len(my_tuple)
print("Length of the tuple:", length_of_tuple)

# Concatenation of tuples
another_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + another_tuple
print("Concatenated tuple:", concatenated_tuple)

# Repeating elements in a tuple
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)

# Checking if an element exists in the tuple using 'in'
is_2_in_tuple = 2 in my_tuple
print("Is 2 in tuple:", is_2_in_tuple)

# Iterating through a tuple
print("Iterating through the tuple:")
for element in my_tuple:
    print(element)

# Unpacking a tuple
a, b, c, d, e = my_tuple
print(f"Unpacked values: a={a}, b={b}, c={c}, d={d}, e={e}")

# Nesting tuples
nested_tuple = (my_tuple, another_tuple)
print("Nested tuple:", nested_tuple)

# Tuples are immutable, so attempting to modify will raise an error
# Uncommenting the following line will raise a TypeError
# my_tuple[0] = 10

# Tuples can contain mutable objects like lists
tuple_with_list = (1, 2, [3, 4, 5])
print("Tuple with a list inside:", tuple_with_list)

# Modifying a list inside a tuple
tuple_with_list[2].append(6)
print("Modified tuple with list inside:", tuple_with_list)
