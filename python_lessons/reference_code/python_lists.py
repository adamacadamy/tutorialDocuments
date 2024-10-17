# List functions in Python with examples

# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# append(): Adds an element at the end of the list
my_list.append(6)
print("After append(6):", my_list)

# extend(): Adds multiple elements to the end of the list
my_list.extend([7, 8, 9])
print("After extend([7, 8, 9]):", my_list)

# insert(): Inserts an element at a given index
my_list.insert(1, 10)  # Insert 10 at index 1
print("After insert(1, 10):", my_list)

# remove(): Removes the first occurrence of the element
my_list.remove(10)
print("After remove(10):", my_list)

# pop(): Removes and returns the element at the specified index
popped_element = my_list.pop(2)  # Removes element at index 2
print(f"After pop(2), popped element: {popped_element}, List now:", my_list)

# index(): Returns the index of the first occurrence of the element
index_of_4 = my_list.index(4)
print("Index of element 4:", index_of_4)

# count(): Returns the count of how many times an element appears in the list
count_of_3 = my_list.count(3)
print("Count of element 3:", count_of_3)

# sort(): Sorts the list in ascending order
my_list.sort()
print("After sort():", my_list)

# reverse(): Reverses the list
my_list.reverse()
print("After reverse():", my_list)

# copy(): Creates a shallow copy of the list
list_copy = my_list.copy()
print("Copy of the list:", list_copy)

# clear(): Removes all elements from the list
my_list.clear()
print("After clear(), list:", my_list)
