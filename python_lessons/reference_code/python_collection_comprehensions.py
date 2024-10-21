
# Python Comprehensions: List, Dict, Tuple, and Set

# 1. List Comprehension

# A list comprehension is used to create a new list by applying an expression 
# to each element in an existing iterable (such as a list, range, etc.).

# Syntax:
# [expression for item in iterable if condition]

# Example:
squares = [i * i for i in range(10)]
print("List of squares:", squares)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example with condition:
even_numbers = [i for i in range(10) if i % 2 == 0]
print("List of even numbers:", even_numbers)
# Output: [0, 2, 4, 6, 8]


# 2. Dictionary Comprehension

# A dictionary comprehension is used to create a new dictionary by applying 
# an expression to each key-value pair from an iterable (like a list of tuples 
# or another dictionary).

# Syntax:
# {key_expression: value_expression for item in iterable if condition}

# Example:
squares_dict = {i: i * i for i in range(5)}
print("Dictionary of squares:", squares_dict)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Example with condition:
input_dict = {'apple': 1, 'banana': 5, 'orange': 3}
filtered_dict = {key: value for key, value in input_dict.items() if value > 1}
print("Filtered dictionary:", filtered_dict)
# Output: {'banana': 5, 'orange': 3}


# 3. Tuple Comprehension (using generator expression)

# Tuple comprehensions do not exist as a separate feature, but you can use 
# generator expressions that behave similarly. To get a tuple from a generator 
# expression, you need to pass it to the tuple() constructor.

# Syntax:
# tuple(expression for item in iterable if condition)

# Example:
squares_tuple = tuple(i * i for i in range(5))
print("Tuple of squares:", squares_tuple)
# Output: (0, 1, 4, 9, 16)

# Example with condition:
even_tuple = tuple(i for i in range(10) if i % 2 == 0)
print("Tuple of even numbers:", even_tuple)
# Output: (0, 2, 4, 6, 8)


# 4. Set Comprehension

# A set comprehension is used to create a new set by applying an expression 
# to each element in an existing iterable. Sets automatically remove duplicates.

# Syntax:
# {expression for item in iterable if condition}

# Example:
squares_set = {i * i for i in range(5)}
print("Set of squares:", squares_set)
# Output: {0, 1, 4, 9, 16}

# Example with condition:
even_set = {i for i in range(10) if i % 2 == 0}
print("Set of even numbers:", even_set)
# Output: {0, 2, 4, 6, 8}

