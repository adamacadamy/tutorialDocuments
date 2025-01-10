# Python Crash Course
![alt text](images/python_logo.png)
---

## **1. Hello World**

```python
# Your first Python program
print("Hello, World!")
```

---

## **2. Variables and Data Types**

```python
x = 5           # Integer
y = 3.14        # Float
name = "Python" # String
is_fun = True   # Boolean

# Variable Conversions
a = 5
b = "10"
c = 3.5

# Convert string to integer and add
print(a + int(b))  # Output: 15

# Convert integer to string and concatenate
print(str(a) + b)  # Output: "510"

# Convert float to integer
print(int(c))  # Output: 3

# Arithmetic Operations
x = 10
y = 3

print(x + y)  # Addition: Output 13
print(x - y)  # Subtraction: Output 7
print(x * y)  # Multiplication: Output 30
print(x / y)  # Division: Output 3.333...
print(x // y) # Floor Division: Output 3
print(x % y)  # Modulus: Output 1
print(x ** y) # Exponentiation: Output 1000

# Collections
fruits = ["apple", "banana", "cherry"]  # List
colors = ("red", "green", "blue")       # Tuple
person = {"name": "John", "age": 30}    # Dictionary
unique_numbers = {1, 2, 3, 4}           # Set

print(fruits, colors, person, unique_numbers)

# List Operations
print(len(fruits))  # Get the length of the list
fruits.append("date")  # Add an element to the list
print(fruits)
fruits.remove("banana")  # Remove an element from the list
print(fruits)

# Tuple Operations
print(len(colors))  # Get the length of the tuple
print(colors[0])  # Access the first element

# Dictionary Operations
print(len(person))  # Get the number of key-value pairs
person["city"] = "New York"  # Add a new key-value pair
print(person)
person.pop("age")  # Remove a key-value pair
print(person)

# Set Operations
print(len(unique_numbers))  # Get the number of elements in the set
unique_numbers.add(5)  # Add an element to the set
print(unique_numbers)
unique_numbers.discard(3)  # Remove an element from the set
print(unique_numbers)


```

---

## **3. Loops**

### **For Loop**

```python
# Loop through numbers from 0 to 4
for i in range(5):
    print(i)  # Print the current number
```

### **While Loop**

```python
# Initialize a counter variable
count = 0

# Loop while count is less than 5
while count < 5:
    print(count)  # Print the current value of count
    count += 1    # Increment count by 1
```

### **Looping Through Collections**

#### **Looping Through a List**

```python
# List of fruits
fruits = ["apple", "banana", "cherry"]

# Loop through each fruit in the list
for fruit in fruits:
    print(fruit)  # Print the current fruit
```

#### **Looping Through a Tuple**

```python
# Tuple of colors
colors = ("red", "green", "blue")

# Loop through each color in the tuple
for color in colors:
    print(color)  # Print the current color
```

#### **Looping Through a Dictionary**

```python
# Dictionary with key-value pairs
person = {"name": "Alice", "age": 25, "city": "New York"}

# Loop through each key-value pair in the dictionary
for key, value in person.items():
    print(f"{key}: {value}")  # Print the key and its corresponding value
```

#### **Looping Through a Set**

```python
# Set of unique numbers
unique_numbers = {1, 2, 3, 4}

# Loop through each number in the set
for number in unique_numbers:
    print(number)  # Print the current number
```

---

## **4. Zip Function**

The `zip()` function combines two or more iterables element-wise into tuples.

### **Basic Example**

```python
# Lists to be combined
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Combine names and ages using zip
zipped = zip(names, ages)

# Convert to a list of tuples
zipped_list = list(zipped)
print("Zipped List:", zipped_list)  # Output: [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

# Unzipping the zipped list
names_unzipped, ages_unzipped = zip(*zipped_list)
print("Names:", names_unzipped)  # Output: ("Alice", "Bob", "Charlie")
print("Ages:", ages_unzipped)    # Output: (25, 30, 35)
```

### **Creating a Dictionary with zip**

```python
# Keys and values for the dictionary
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

# Use zip and dict to create a dictionary
dictionary = dict(zip(keys, values))
print("Dictionary:", dictionary)  # Output: {"name": "Alice", "age": 25, "city": "New York"}
```

### **Iterating Through Dictionaries with zip**

```python
# Two dictionaries with related data
dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "country": "USA"}

# Use zip to combine keys and values from both dictionaries
for (key1, value1), (key2, value2) in zip(dict1.items(), dict2.items()):
    print(f"{key1}: {value1}, {key2}: {value2}")  # Output combined key-value pairs
```

### **Using zip with Multiple Iterables**

```python
# Multiple iterables to combine
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
symbols = ["@", "#", "$"]

# Combine all three iterables using zip
zipped = zip(letters, numbers, symbols)
print(list(zipped))  # Output: [("a", 1, "@"), ("b", 2, "#"), ("c", 3, "$")]
```

### **Handling Uneven Iterables with zip**

```python
# Iterables with different lengths
short_list = [1, 2]
long_list = ["a", "b", "c"]

# zip stops at the shortest iterable
zipped = zip(short_list, long_list)
print(list(zipped))  # Output: [(1, "a"), (2, "b")]
```

---

## **5. Functions**

### **Returnable Functions**

These functions return a value and include a return type in their type hint.

```python
# Function that returns a string
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Function that returns an integer
def add(a: int, b: int) -> int:
    return a + b

# Example usage
print(greet("Alice"))  # Output: Hello, Alice!
print(add(5, 3))        # Output: 8
```

### **Non-Returnable Functions**

These functions perform an operation but do not return a value (implicitly return `None`).

```python
# Function that prints a message (no return value)
def print_greeting(name: str) -> None:
    print(f"Hello, {name}!")

# Function that modifies a list in-place (no return value)
def append_to_list(items: list[int], value: int) -> None:
    items.append(value)

# Example usage
print_greeting("Alice")
my_list = [1, 2, 3]
append_to_list(my_list, 4)
print(my_list)  # Output: [1, 2, 3, 4]
```

---

## **6. Classes and Object-Oriented Programming**

### **Basic Class Example**

```python
class Person:
    def __init__(self, name: str, age: int):
        # Constructor: Initializes the Person instance with name and age
        self.name = name
        self.age = age

    def greet(self) -> str:
        # Method: Returns a greeting message
        return f"Hi, I'm {self.name} and I'm {self.age} years old!"

# Example usage
john = Person("John", 30)
print(john.greet())
```

### **Inheritance**

```python
class Animal:
    def __init__(self, name: str):
        # Constructor: Initializes the Animal with a name
        self.name = name

    def sound(self) -> str:
        # Method: Returns a generic sound
        return "Some generic sound"

class Dog(Animal):
    def sound(self) -> str:
        # Overridden Method: Returns a dog-specific sound
        return "Bark"

# Example usage
dog = Dog("Buddy")
print(f"{dog.name} says {dog.sound()}")
```

### **Magic Methods**

```python
class Point:
    def __init__(self, x: int, y: int):
        # Constructor: Initializes the Point with x and y coordinates
        self.x = x
        self.y = y

    def __str__(self) -> str:
        # Magic Method: Returns a user-friendly string representation of the Point
        return f"Point({self.x}, {self.y})"

    def __add__(self, other: "Point") -> "Point":
        # Magic Method: Enables the + operator for Point objects
        return Point(self.x + other.x, self.y + other.y)

# Example usage
p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2
print(p3)
```

### **Properties**

```python
class Rectangle:
    def __init__(self, width: float, height: float):
        # Constructor: Initializes the Rectangle with width and height
        self._width = width
        self._height = height

    @property
    def width(self) -> float:
        # Getter: Returns the width of the Rectangle
        return self._width

    @width.setter
    def width(self, value: float):
        # Setter: Validates and sets the width of the Rectangle
        if value <= 0:
            raise ValueError("Width must be positive.")
        self._width = value

    @property
    def area(self) -> float:
        # Property: Calculates and returns the area of the Rectangle
        return self._width * self._height

# Example usage
rect = Rectangle(4, 5)
print(rect.area)  # Output: 20
rect.width = 6
print(rect.area)  # Output: 30
```

### **Abstract Classes**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        # Abstract Method: Must be implemented by subclasses
        pass

    @abstractmethod
    def perimeter(self) -> float:
        # Abstract Method: Must be implemented by subclasses
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        # Constructor: Initializes the Circle with a radius
        self.radius = radius

    def area(self) -> float:
        # Implementation: Calculates and returns the area of the Circle
        from math import pi
        return pi * self.radius ** 2

    def perimeter(self) -> float:
        # Implementation: Calculates and returns the perimeter of the Circle
        from math import pi
        return 2 * pi * self.radius

# Example usage
circle = Circle(5)
print(f"Area: {circle.area()} - Perimeter: {circle.perimeter()}")  # Output: Area and Perimeter of the Circle
```

---

## **7. Managing Packages with pip**

### **Installing Packages**

```bash
# Install a package from PyPI (Python Package Index)
pip install requests
```

### **Exporting Installed Packages to `requirements.txt`**

```bash
# Export all installed packages and their versions to requirements.txt
pip freeze > requirements.txt
```

### **Installing Packages from `requirements.txt`**

```bash
# Install all packages listed in requirements.txt
pip install -r requirements.txt
```

### **Setting Up a Virtual Environment**

```bash
# Create a virtual environment named .venv
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate

# Install packages within the virtual environment
pip install requests

# Deactivate the virtual environment
# Exit the virtual environment
deactivate
```

### **Uninstalling Packages**

```bash
# Uninstall a package
pip uninstall requests
```

### **Upgrading Packages**

```bash
# Upgrade a package to the latest version
pip install --upgrade requests
```

### **Listing Installed Packages**

```bash
# List all installed packages
pip list
```

### **Using Requirements Files**

```bash
# Create a requirements.txt file with package dependencies
# Example contents of requirements.txt:
# requests==2.25.1
# numpy>=1.19.0

# Install all packages listed in the file
pip install -r requirements.txt
```

