# Basic Variable Assignments
# Assigning integers
x = 10

# Assigning floating-point numbers
y = 3.14

# Assigning strings
name = "Alice"

# Assigning boolean values
is_valid = True


# Multiple Variable Assignments
a, b, c = 1, 2, 3


# Assigning the Same Value to Multiple Variables
p = q = r = 5


# Assigning Lists, Tuples, and Dictionaries

# List
my_list = [1, 2, 3]

# Tuple
my_tuple = (4, 5, 6)

# Dictionary
my_dict = {"key": "value", "age": 30}


# Dynamic Typing
var = 100  # Initially an integer
var = "Now a string"  # Reassigned as a string

# Assigning Variables to Other Variables
x = 10
y = x  # y is now assigned the value of x, so y = 10

# Changing one variable does not affect the other
x = 20  # Now x is 20, but y is still 10

# Copying Lists (Shallow Copy)
list1 = [1, 2, 3]
list2 = list1  # list2 references the same list as list1

# Modifying list1 affects list2 because both reference the same list
list1.append(4)  # list1 is now [1, 2, 3, 4], and list2 is also [1, 2, 3, 4]

# To create a new copy of the list, use slicing or copy method (Shallow Copy)
list3 = list1[:]  # Creates a new list, so modifying list1 won't affect list3
list1.append(5)   # list1 is now [1, 2, 3, 4, 5], but list3 remains [1, 2, 3, 4]

# Copying Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = dict1  # dict2 references the same dictionary as dict1

# Modifying dict1 affects dict2 because they reference the same dictionary
dict1["c"] = 3  # dict1 is now {"a": 1, "b": 2, "c": 3}, dict2 also {"a": 1, "b": 2, "c": 3}

# To create a new copy of the dictionary, use the copy method
dict3 = dict1.copy()  # Creates a shallow copy of dict1
dict1["d"] = 4  # dict1 is now {"a": 1, "b": 2, "c": 3, "d": 4}, but dict3 is still {"a": 1, "b": 2, "c": 3}

# Assigning None
x = None  # x now has no value (NoneType)
y = None  # y is also assigned None
