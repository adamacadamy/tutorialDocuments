# Python Functions, Lambda Expressions, *args, and **kwargs

# 1. Regular Function Example
def add_numbers(x, y):
    """Returns the sum of two numbers."""
    return x + y

result = add_numbers(5, 10)
print(f"add_numbers(5, 10) -> {result}")  # Output: 15


# 2. Function with Default Arguments
def greet(name, greeting="Hello"):
    """Greets a person with a specified greeting."""
    return f"{greeting}, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", greeting="Hi"))  # Output: Hi, Bob!


# 3. Function with Positional and Keyword Arguments
def introduce(name, age, city="Unknown"):
    """Introduces a person."""
    return f"My name is {name}, I am {age} years old, from {city}."

print(introduce("Alice", 25, city="New York"))
# Output: My name is Alice, I am 25 years old, from New York.

print(introduce("Bob", 30))
# Output: My name is Bob, I am 30 years old, from Unknown.


# 4. Recursive Function Example
def factorial(n):
    """Returns the factorial of n."""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"factorial(5) -> {factorial(5)}")  # Output: 120


# 5. Lambda Expression Example
# A lambda function to add two numbers
add_lambda = lambda x, y: x + y
print(f"add_lambda(5, 10) -> {add_lambda(5, 10)}")  # Output: 15

# Using lambda with map() function to square each number in a list
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(f"Squared numbers using map -> {list(squared)}")  # Output: [1, 4, 9, 16]

# Using lambda with filter() to filter even numbers from a list
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(f"Even numbers using filter -> {list(even_numbers)}")  # Output: [2, 4]

# Using lambda with sorted() to sort a list of tuples by the second item
points = [(1, 2), (4, 1), (5, -2)]
sorted_points = sorted(points, key=lambda point: point[1])
print(f"Points sorted by second item using sorted -> {sorted_points}")
# Output: [(5, -2), (4, 1), (1, 2)]


# 6. *args Example
def sum_all(*args):
    """Sums all positional arguments."""
    return sum(args)

print(f"sum_all(1, 2, 3, 4) -> {sum_all(1, 2, 3, 4)}")  # Output: 10
print(f"sum_all(10, 20) -> {sum_all(10, 20)}")  # Output: 30


# 7. **kwargs Example
def print_details(**kwargs):
    """Prints details provided as keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, job="Engineer")
# Output:
# name: Alice
# age: 25
# job: Engineer


# 8. *args and **kwargs Together
def mixed_function(*args, **kwargs):
    """Handles both positional and keyword arguments."""
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

mixed_function(1, 2, 3, name="Alice", age=30)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 30}
