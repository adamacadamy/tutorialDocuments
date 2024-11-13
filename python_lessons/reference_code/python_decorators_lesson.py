
# Python Lesson: Decorators
# =========================
# In Python, decorators are a way to modify the behavior of a function or a class.
# They are a powerful tool for extending functionality without modifying the original code directly.

# 1. Basic Decorator
# ------------------
# A basic decorator is a function that takes another function as an argument, adds some behavior,
# and returns a new function.

def simple_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

# Applying the decorator using the @ syntax
@simple_decorator
def say_hello():
    print("Hello, world!")

# When we call `say_hello()`, it will execute the wrapper function:
say_hello()

# Output:
# Before the function call
# Hello, world!
# After the function call

# 2. Function Decorators with Arguments
# -------------------------------------
# Decorators can also accept arguments. To create such decorators, we need an extra level of nested functions.

def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_decorator(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!

# 3. Preserving Metadata with `functools.wraps`
# ---------------------------------------------
# When using decorators, the original function's metadata (like its name and docstring) can be lost.
# To preserve this metadata, we can use `functools.wraps`.

import functools

def logging_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logging_decorator
def add(a, b):
    '''Adds two numbers'''
    return a + b

result = add(3, 5)
print(f"Result: {result}")
print(f"Function Name: {add.__name__}")
print(f"Docstring: {add.__doc__}")

# Output:
# Calling function: add
# Result: 8
# Function Name: add
# Docstring: Adds two numbers

# 4. Class Decorators
# -------------------
# Decorators can also be implemented using classes. A class decorator defines a class that has a `__call__` method,
# making the class instance callable like a function.

class UpperCaseDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result.upper()

@UpperCaseDecorator
def get_message():
    return "Hello from class decorator!"

print(get_message())

# Output:
# HELLO FROM CLASS DECORATOR!

# 5. Chaining Multiple Decorators
# -------------------------------
# You can apply multiple decorators to a single function by stacking them.

def bold_decorator(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic_decorator(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold_decorator
@italic_decorator
def text():
    return "Decorated Text"

print(text())

# Output:
# <b><i>Decorated Text</i></b>

# Summary:
# - Decorators are used to modify the behavior of functions or methods.
# - They can be used with the `@decorator` syntax.
# - Use `functools.wraps` to preserve the original function's metadata.
# - Decorators can be functions or classes.
# - You can chain multiple decorators to apply several modifications.

# This lesson covers the basics of Python decorators and provides examples for common use cases.
