"""  
Primitive Data Types (or Basic Data Types)
    1. Integers (int): Whole numbers, positive or negative.
    2. Floats (float): Numbers with a decimal point.
    3. Booleans (bool): Represents True or False.
    4. Strings (str): A sequence of characters.
Complex Data Types
    1. Lists (list): An ordered, mutable collection of items.
    2. Tuples (tuple): An ordered, immutable collection of items.
    3. Sets (set): An unordered, mutable collection of unique items.
    4. Dictionaries (dict): A collection of key-value pairs.
    5. NoneType (None): Represents the absence of a value.

"""
# Primitive Data Types

# 1. Integer (int)
my_int = 10
print("Integer:", my_int)

# 2. Float (float)
my_float = 10.5
print("Float:", my_float)

# 3. Boolean (bool)
my_bool = True
print("Boolean:", my_bool)

# 4. String (str)
my_string = "Hello, World!"
print("String:", my_string)

# Complex Data Types

# 5. List (list): Ordered and mutable
my_list = [1, 2, 3, "apple", 4.5]
print("List:", my_list)
my_list[0] = 100  # Modifying an element in the list
my_list.append("banana")  # Adding to the list
print("List after modifications:", my_list)

# 6. Tuple (tuple): Ordered and immutable
my_tuple = (1, 2, 3, "orange")
print("Tuple:", my_tuple)
# Note: Tuples are immutable, so we cannot modify the elements like a list

# 7. Set (set): Unordered and mutable, no duplicates allowed
my_set = {1, 2, 3, "apple", 4.5}
print("Set:", my_set)
my_set.add("banana")  # Adding an element to the set
my_set.add(1)  # Adding a duplicate (won't appear twice)
print("Set after modifications:", my_set)

# 8. Dictionary (dict): Collection of key-value pairs
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Dictionary:", my_dict)
my_dict["email"] = "alice@example.com"  # Adding a new key-value pair
my_dict["age"] = 26  # Updating a value
print("Dictionary after modifications:", my_dict)

# 9. NoneType (None): Represents the absence of value
my_none = None
print("NoneType:", my_none)

# Operations on Primitive Types

# Arithmetic operations on integers and floats
sum_int = my_int + 5  # 10 + 5
sum_float = my_float + 3.5  # 10.5 + 3.5
print("Sum of integer and 5:", sum_int)
print("Sum of float and 3.5:", sum_float)

# String concatenation
greeting = my_string + " How are you?"
print("Concatenated string:", greeting)

# Boolean expressions
is_greater = 5 > 3
is_equal = (10 == my_int)  # Checking if my_int is equal to 10
print("Boolean expression (5 > 3):", is_greater)
print("Is my_int equal to 10:", is_equal)

# Accessing Elements in Complex Types

# Accessing list elements by index
first_list_element = my_list[0]
second_list_element = my_list[1]
print("First element of the list:", first_list_element)
print("Second element of the list:", second_list_element)

# Accessing tuple elements by index
first_tuple_element = my_tuple[0]
second_tuple_element = my_tuple[1]
print("First element of the tuple:", first_tuple_element)
print("Second element of the tuple:", second_tuple_element)

# Accessing dictionary values by key
name_from_dict = my_dict["name"]
age_from_dict = my_dict["age"]
print("Name from the dictionary:", name_from_dict)
print("Age from the dictionary:", age_from_dict)

# Checking membership in sets
is_apple_in_set = "apple" in my_set
is_banana_in_set = "banana" in my_set
print("Is 'apple' in the set:", is_apple_in_set)
print("Is 'banana' in the set:", is_banana_in_set)

# Checking length of complex types
list_length = len(my_list)
tuple_length = len(my_tuple)
set_length = len(my_set)
dict_length = len(my_dict)
print("Length of the list:", list_length)
print("Length of the tuple:", tuple_length)
print("Length of the set:", set_length)
print("Number of items in the dictionary:", dict_length)
