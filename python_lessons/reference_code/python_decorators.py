
# Lesson: Python Decorators

# 1. Introduction to Decorators
# Decorators in Python are a way to modify or enhance functions or methods without changing their definition.
# They are typically used to add functionality to functions, such as logging, access control, timing execution, etc.

# A decorator is a function that takes another function as an argument and extends or alters its behavior.

# Basic decorator example:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator  # This is how we apply the decorator to the function
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()

# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# 2. Functions as First-Class Citizens
# In Python, functions are first-class citizens, meaning you can pass them as arguments to other functions, 
# return them from functions, and assign them to variables. This feature allows decorators to work.

def greet():
    return "Hello!"

# Assign the function to a variable
greeting = greet
print(greeting())  # Outputs: Hello!

# 3. Applying Decorators
# To apply a decorator, you can use the @decorator_name syntax above a function, or you can manually wrap a function.

# Manual application of a decorator
def say_goodbye():
    print("Goodbye!")

decorated_func = my_decorator(say_goodbye)
decorated_func()

# 4. Decorators with Arguments
# If the function being decorated accepts arguments, the decorator function needs to handle those as well.

def my_decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)  # Call the original function with arguments
        print("After the function call")
        return result
    return wrapper

@my_decorator_with_args
def greet_person(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet_person("John", 30)

# 5. Returning Values from Decorated Functions
# The decorator can also return values by calling the original function and returning its result.

@my_decorator_with_args
def add(a, b):
    return a + b

result = add(5, 10)
print(f"Result: {result}")  # Output: Before the function call, After the function call, Result: 15

# 6. Decorating Methods in Classes
# Decorators can also be used to modify methods in classes.

class MyClass:
    @my_decorator_with_args
    def method(self, name):
        print(f"Method called with {name}")

obj = MyClass()
obj.method("decorator example")

# 7. Using functools.wraps
# When creating decorators, it's a good practice to use `functools.wraps` to preserve the original function's name, docstring, and metadata.

import functools

def my_decorator_with_wraps(func):
    @functools.wraps(func)  # This preserves the original function's information
    def wrapper(*args, **kwargs):
        print("Before the function call")
        return func(*args, **kwargs)
    return wrapper

@my_decorator_with_wraps
def another_function():
    print("Another function here!")

another_function()

# 8. Practical Example: Timing Function Execution
# Here's a decorator that measures the time a function takes to execute.

import time

def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)
        end_time = time.time()  # Record end time
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@timer_decorator
def long_running_task():
    time.sleep(2)  # Simulate a long-running task
    print("Task complete.")

long_running_task()

# This lesson provides a comprehensive overview of decorators in Python, from basic usage to more advanced scenarios.
