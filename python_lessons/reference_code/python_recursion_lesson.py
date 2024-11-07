
# Lesson on Recursion in Python

# What is Recursion?
# Recursion is a method of solving problems where a function calls itself as a subroutine.
# This enables the function to repeat its behavior multiple times until it reaches a base condition,
# simplifying complex problems by breaking them down into smaller, more manageable sub-problems.

# Basic Structure of a Recursive Function
# A recursive function typically has two main parts:
# 1. Base Case: This is the condition that stops the recursion. Without it, the function would call itself indefinitely,
#    leading to a stack overflow error.
# 2. Recursive Case: This is where the function calls itself with a smaller version of the original problem,
#    moving closer to the base case.

# Syntax Example:
# def recursive_function(parameters):
#     if base_condition:  # Base Case
#         return result
#     else:
#         # Recursive Case
#         return recursive_function(modified_parameters)

# Example: Factorial of a Number
# Factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
# It is denoted as n!, and defined as:
# - n! = n * (n-1)!
# - Base case: 0! = 1

# Recursive Solution:
def factorial(n):
    if n == 0:  # Base Case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive Case

# Test the function
print(factorial(5))  # Output: 120

# Understanding the Execution Flow
# When factorial(5) is called, Python performs the following calls:
# 1. factorial(5) -> 5 * factorial(4)
# 2. factorial(4) -> 4 * factorial(3)
# 3. factorial(3) -> 3 * factorial(2)
# 4. factorial(2) -> 2 * factorial(1)
# 5. factorial(1) -> 1 * factorial(0)
# Finally, factorial(0) returns 1, and the functions start returning their results in reverse order,
# eventually giving factorial(5) = 120.

# Types of Recursion
# 1. Direct Recursion: A function calls itself directly, as in the factorial example.
# 2. Indirect Recursion: A function calls another function, which eventually leads to a call to the first function.

# Example of Indirect Recursion:
def function_a(x):
    if x > 0:
        print(x)
        function_b(x - 1)

def function_b(x):
    if x > 0:
        print(x)
        function_a(x - 1)

# Test the functions
function_a(5)

# Fibonacci Sequence Using Recursion
# The Fibonacci sequence is defined as:
# - F(0) = 0
# - F(1) = 1
# - F(n) = F(n-1) + F(n-2)

# Recursive Solution:
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
print(fibonacci(6))  # Output: 8

# Pros and Cons of Recursion
# Pros:
# - Simplifies Code: Recursive solutions can be more elegant and easier to understand for problems that naturally fit recursive structures (e.g., tree traversal).
# - Reduces Code Complexity: Certain algorithms can be implemented more concisely.
#
# Cons:
# - High Memory Usage: Each recursive call adds a new frame to the call stack, which may lead to high memory usage for deep recursions.
# - Slower Execution: Recursive functions tend to be slower than their iterative counterparts due to the overhead of multiple function calls.

# Recursive Solution vs Iterative Solution
# Sometimes, recursion can be replaced by iteration for a more memory-efficient approach.

# Example: Factorial Using Iteration
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test the function
print(factorial_iterative(5))  # Output: 120

# Practical Applications of Recursion
# 1. Tree and Graph Traversal: Recursive functions are particularly useful for traversing hierarchical data structures like trees.
# 2. Divide and Conquer Algorithms: Many algorithms (e.g., merge sort, quick sort) use recursion.
# 3. Backtracking: Problems like solving a maze, Sudoku, or the N-Queens problem can be elegantly solved with recursion.

# Advanced Example: Tower of Hanoi
# The Tower of Hanoi is a classic problem involving moving disks from one rod to another,
# with the constraint that only one disk can be moved at a time and no disk can be placed on top of a smaller disk.

# Recursive Solution:
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        hanoi(n - 1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        hanoi(n - 1, auxiliary, target, source)

# Test the function
hanoi(3, 'A', 'C', 'B')
