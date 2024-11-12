# Exercise 3: Advanced Python Challenges  

# 1. Define a function `calculate_statistics` that takes a list of numbers and returns a dictionary containing:
#    a) The mean of the numbers.
#    b) The median of the numbers.
#    c) The mode of the numbers.
#    Use the `statistics` module for these calculations.



# 2. Create a class `Rectangle` that has attributes for `width` and `height`.
#    a) Define a method to calculate the area of the rectangle.
#    b) Define a method to calculate the perimeter of the rectangle.
#    c) Instantiate two rectangles and compare their areas.

# 3. Define a function `is_prime` that takes an integer and returns `True` if the number is prime, and `False` otherwise.
#    a) Use this function to filter a list of numbers (from 1 to 100) and return only the prime numbers.

# 4. Define a function `merge_dictionaries` that accepts two dictionaries and merges them.
#    a) If both dictionaries have the same key, sum the values of that key.
#    b) Otherwise, combine the keys and values into the resulting dictionary.

# 5. Create a generator function `fibonacci` that yields an infinite sequence of Fibonacci numbers.
#    a) Use a `for` loop to print the first 20 Fibonacci numbers.

# 6. Define a function `matrix_transpose` that takes a 2D list (matrix) and returns its transpose.
#    a) The function should work for any matrix size.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
 
# for row in zip(*matrix): #      [1, 2, 3], [4, 5, 6],  [7, 8, 9]
#     pass
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# 7. Write a function `analyze_text` that takes a string and returns:
#    a) The number of words in the string.
#    b) The number of unique words.
#    c) A dictionary of word frequencies.
#    d) The longest word in the string.

# 8. Define a function `group_by_length` that takes a list of strings and returns a dictionary where:
#    a) The keys are string lengths.
#    b) The values are lists of strings with that length.

# 9. Define a recursive function `factorial` that calculates the factorial of a given number.
#    a) Use it to calculate the factorial of numbers from 1 to 10.

# 10. Define a function `flatten_list` that takes a nested list and returns a flat list.
#     a) Use recursion to handle arbitrarily nested lists.
#     Example: flatten_list([1, [2, [3, 4], 5]]) -> [1, 2, 3, 4, 5]

# 11. Write a function `reverse_string_recursive` that reverses a given string using recursion.
#     Example: reverse_string_recursive("hello") -> "olleh"
 

# 12. Define a higher-order function `apply_twice` that takes another function `f` as input and applies it twice to a given argument.
#     Example: apply_twice(lambda x: x * 2, 5) -> 20
# from typing import Generator, Callable


# def apply_twice(f: Generator | Callable, x: int)-> int:
#      f(f(x))
     
     
# apply_twice(?, x=5)

#  13. Define a function `read_file_lines` that reads the contents of a file line by line and returns a list of the lines.
#     a) Handle file not found errors gracefully by printing a message.

# 14. Define a function `write_even_numbers` that writes only the even numbers from a list into a text file.
#     a) Ensure that the file is created and written to safely.

# 15. Define a function `memoized_fibonacci` that returns the nth Fibonacci number, using memoization to optimize the computation.
#     a) Ensure the function computes the nth Fibonacci efficiently by storing already computed values.

# 16. Create a decorator `time_execution` that measures and prints the execution time of any function it decorates.
#     a) Use it on the `fibonacci` function to measure how long it takes to compute the 30th Fibonacci number.

# 17. Define a function `unique_permutations` that takes a list and returns all unique permutations of the elements in the list.
#     a) Use the `itertools` module to simplify the task.

# 18. Define a function `safe_division` that performs division but catches division by zero errors.
#     a) If an error occurs, return "Undefined" instead of raising an exception.

# 19. Create a class `BankAccount` with attributes for `balance` and methods `deposit` and `withdraw`.
#     a) Ensure `withdraw` raises an error if there are insufficient funds.
#     b) Create a method `transfer` to transfer money between two bank accounts.

# 20. **New Challenge: Complex Data Manipulation**
#     Define a function `merge_sort` that implements the merge sort algorithm recursively.
#     a) The function should take a list of numbers and return a sorted list.
#     b) Ensure the function is efficient and works on lists of large size.
#     c) Use this function to sort a list of 1000 random numbers.

# 21. Define a function `json_to_yaml` that converts a JSON object to a YAML file.
#     a) The JSON object should contain key-value pairs.
#     b) Use the `yaml` module to write the data to a YAML file.

# 22. Define a function `yaml_to_json` that converts a YAML file to a JSON object.
#     a) Ensure the function reads the YAML file and outputs the equivalent JSON structure.

# 23. Define a function `yaml_to_csv` that converts a YAML file to a CSV file.
#     a) The YAML file should contain structured data (e.g., dictionaries or lists).
#     b) Use the `csv` module to write the data to a CSV file.

# 24. Define a function `csv_to_yaml` that converts a CSV file to a YAML file.
#     a) The CSV file should contain rows of data.
#     b) Ensure the function reads the CSV and outputs the equivalent YAML structure.
