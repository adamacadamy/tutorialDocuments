
# Python Lesson: Iterators, next(), yield, and underscore (_) usage

# 1. Iterators in Python
# An iterator is an object that allows you to traverse through a sequence of elements,
# like a list or tuple, without needing to access elements by index.
# It requires two methods:
# - __iter__() to return the iterator object itself.
# - __next__() to return the next item or raise StopIteration if there are no more items.

# Example of a Basic Iterator
my_list = [1, 2, 3]
my_iterator = iter(my_list)

print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3

# 2. The next() Function
# The next() function retrieves the next item from an iterator manually.
# It takes an iterator as an argument and raises a StopIteration exception if no more items are available.

# Example Using next()
my_list = [10, 20, 30]
my_iterator = iter(my_list)

print(next(my_iterator))  # Output: 10
print(next(my_iterator))  # Output: 20
print(next(my_iterator))  # Output: 30

# Avoiding StopIteration with a default value
print(next(my_iterator, 'End of list'))  # Output: End of list

# 3. Creating Custom Iterators
# Custom iterators allow you to control the iteration process by defining a class with __iter__ and __next__ methods.

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1

# Using the custom iterator
countdown = Countdown(3)
for number in countdown:
    print(number)  # Output: 3, 2, 1

# 4. The yield Keyword and Generators
# yield allows you to create generators, a special type of iterator that produces items one at a time.
# This approach is memory-efficient, as yield does not require storing all values at once.

def simple_generator():
    yield 1
    yield 2
    yield 3

for value in simple_generator():
    print(value)  # Output: 1, 2, 3

# 5. Using yield for Infinite Generators
# You can create infinite generators with yield, generating values on-demand.
def infinite_numbers(start=1):
    while True:
        yield start
        start += 1

infinite_gen = infinite_numbers()
print(next(infinite_gen))  # Output: 1
print(next(infinite_gen))  # Output: 2

# 6. Practical Example: Fibonacci Sequence Using yield
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for number in fibonacci(10):
    print(number)  # Output: 0, 1, 1, 2, 3, 5, 8

# 7. yield vs. return
# yield allows a function to return multiple values over time, whereas return only returns once.

def with_return():
    return [1, 2, 3]

def with_yield():
    yield 1
    yield 2
    yield 3

print(with_return())  # Output: [1, 2, 3]
print(list(with_yield()))  # Output: [1, 2, 3]

# 8. Using _ in Python

# _ as a throwaway variable
for _ in range(5):  
    print("Hello")

# Ignoring values in unpacking
x, _, y = (1, 2, 3)
print(x, y)  # Output: 1, 3

# _ as last expression result in REPL
# >>> 3 + 4  # Output: 7
# >>> print(_)  # Output: 7

# _ for readability in large numbers
large_number = 1_000_000
print(large_number)  # Output: 1000000

# Summary
# Iterator: An object implementing __iter__() and __next__().
# next(): Used to fetch the next item in an iterator manually.
# yield: Pauses a function and returns a value, allowing it to act as a generator.
# _: Used as a throwaway variable, a placeholder, for readability in large numbers.

# Practice Exercise
# Exercise: Write a generator function that yields prime numbers up to a specified limit.

def prime_numbers(limit):
    for num in range(2, limit + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            yield num

for prime in prime_numbers(20):
    print(prime)  # Expected Output: 2, 3, 5, 7, 11, 13, 17, 19
