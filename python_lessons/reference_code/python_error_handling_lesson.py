
# Python Error Handling Complete Guide

# Error handling in Python is an essential skill, as it ensures your program behaves well even when things go wrong.
# Python provides robust mechanisms to handle errors and exceptions using try, except, else, and finally. This guide
# will cover these basics, along with some advanced techniques.

# 1. What are Exceptions?

# In Python, exceptions are errors detected during execution that halt the program's normal flow. Python raises an 
# exception when an error occurs. For example, dividing by zero results in a ZeroDivisionError.

# result = 1 / 0  # This raises ZeroDivisionError

# 2. Basic Error Handling: try and except

# To handle exceptions, we use try and except. Code that may throw an exception goes inside the try block. If an 
# exception occurs, it is caught in the except block.

try:
    result = 1 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")

# 3. Handling Multiple Exceptions

# You can handle different exceptions separately or use a generic exception handler.

# Handling Multiple Specific Exceptions:
try:
    x = int("hello")
    result = 1 / 0
except ValueError:
    print("There was a value error!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catching All Exceptions:
try:
    result = 1 / 0
except Exception as e:
    print(f"An error occurred: {e}")

# 4. else Block

# The else block is executed if the try block does not raise an exception. It's useful for code that should run only
# if no errors occur.

try:
    result = 1 / 1
except ZeroDivisionError:
    print("You cannot divide by zero!")
else:
    print("Success! No errors.")

# 5. finally Block

# The finally block is always executed, whether an exception is raised or not. It’s commonly used for cleanup actions 
# like closing files or releasing resources.

try:
    result = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute.")

# 6. Raising Exceptions

# Sometimes, you might want to raise an exception yourself using the raise statement.

def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b

try:
    divide(5, 0)
except ValueError as e:
    print(e)

# 7. Custom Exceptions

# You can create your own exception classes for more specific error handling. Custom exceptions should inherit from 
# Python’s Exception class.

class CustomError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise CustomError("Negative number not allowed!")

try:
    check_positive(-5)
except CustomError as e:
    print(e)

# 8. Best Practices for Error Handling

# - Handle exceptions at the right level: Don't try to catch every possible error in one place. Handle them at appropriate levels in your code.
# - Be specific: Catch specific exceptions rather than using a generic except Exception.
# - Use logging: Instead of just printing the error, use the logging module for better traceability.
# - Avoid swallowing exceptions: If you catch an exception but don't handle it properly, it can hide bugs.
# - Don’t use exceptions for flow control: While exceptions are powerful, avoid using them for normal control flow as they can make the code hard to understand.

# 9. Exception Chaining (from keyword)

# Python supports chaining exceptions, meaning you can raise a new exception while preserving the original.

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Invalid input!") from e

try:
    divide(10, 0)
except ValueError as e:
    print(f"Caught an exception: {e}")

# 10. Using with for Resource Management

# The with statement is used to ensure that resources are properly cleaned up. It automatically handles exceptions and
# executes cleanup code (e.g., closing a file).

try:
    with open("non_existent_file.txt") as file:
        data = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")

