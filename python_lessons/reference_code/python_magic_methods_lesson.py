
# Python Lesson: Magic Methods (Dunder Methods) in Classes

# Magic methods, also known as "dunder" (double underscore) methods, are special methods in Python classes.
# These methods are surrounded by double underscores (__) and are called automatically based on object interactions.
# Common dunder methods include __init__, __str__, __repr__, __len__, __getitem__, and many others.

# 1. __init__ Method
# __init__ is the constructor method called automatically when an instance of the class is created.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Example usage of __init__
person = Person("Alice", 30)
print(person.name)  # Output: Alice
print(person.age)   # Output: 30

# 2. __str__ and __repr__ Methods
# __str__ provides a user-friendly string representation of an object.
# __repr__ provides an "official" string representation of an object, mainly for debugging.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person({self.name}, {self.age})"

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

# Example usage of __str__ and __repr__
person = Person("Bob", 25)
print(person)       # Output: Person(Bob, 25)
print(repr(person)) # Output: Person(name=Bob, age=25)

# 3. __len__ Method
# __len__ is called when you use the len() function on an instance. It should return the "length" of the object.

class MyCollection:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

# Example usage of __len__
collection = MyCollection([1, 2, 3, 4])
print(len(collection))  # Output: 4

# 4. __getitem__ and __setitem__ Methods
# __getitem__ is called to retrieve an item using the indexing operator [].
# __setitem__ is called to set an item using the indexing operator [].

class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

# Example usage of __getitem__ and __setitem__
my_list = MyList([10, 20, 30])
print(my_list[1])  # Output: 20
my_list[1] = 25
print(my_list[1])  # Output: 25

# 5. __call__ Method
# __call__ allows an instance of a class to be called as a function.

class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        return f"Hello, {self.name}!"

# Example usage of __call__
greeter = Greeter("Charlie")
print(greeter())  # Output: Hello, Charlie!

# 6. __add__, __sub__, __mul__, etc. (Operator Overloading)
# Magic methods such as __add__, __sub__, __mul__, etc., allow objects to support operators like +, -, *, etc.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Example of operator overloading with __add__
v1 = Vector(2, 3)
v2 = Vector(5, 6)
v3 = v1 + v2
print(v3)  # Output: Vector(7, 9)

# 7. __enter__ and __exit__ Methods (Context Managers)
# __enter__ and __exit__ allow an object to be used in a with statement, automatically handling setup and teardown.

class MyResource:
    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Resource released")

# Example of using __enter__ and __exit__
with MyResource() as resource:
    print("Using resource")
# Output:
# Resource acquired
# Using resource
# Resource released

# Summary
# Magic methods (dunder methods) allow objects to define behavior for built-in functions and operators.
# Common dunder methods include __init__, __str__, __repr__, __len__, __getitem__, __setitem__, __call__,
# operator overloads like __add__, and context manager methods __enter__ and __exit__.

# Practice Exercise
# Implement a class representing a 2D point with dunder methods __init__, __str__, __add__, and __eq__.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Example usage of Point class
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)  # Output: Point(4, 6)
print(p1 == p2)  # Output: False
