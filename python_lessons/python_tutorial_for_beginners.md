
# Python Tutorial for Beginners

## 1. Introduction to Python
Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. It's widely used in web development, data science, automation, and more.

**Why Python?**
- Easy to learn and use
- Extensive standard libraries
- Large community support
- Versatile (can be used in many fields)

## 2. Installing Python
- Download Python from [python.org](https://www.python.org/downloads/).
- Install the latest version (Python 3.x).
- Verify installation:
  ```bash
  python --version
  ```
  
## 3. Setting Up Your First Python Program
1. Open a text editor or IDE (e.g., Visual Studio Code, PyCharm).
2. Create a file named `hello.py`.
3. Add the following code:
   ```python
   print("Hello, World!")
   ```
4. Run the script:
   ```bash
   python hello.py
   ```

## 4. Basic Syntax and Concepts
### Comments
- Single-line comment: `# This is a comment`
- Multi-line comment:
  ```python
  '''
  This is a
  multi-line comment
  '''
  ```

### Variables and Data Types
- Variables store data values.
  ```python
  name = "Alice"  # String
  age = 25        # Integer
  height = 5.7    # Float
  is_student = True  # Boolean
  ```

### Basic Data Types
- **Integer**: Whole numbers (e.g., `10`, `-5`)
- **Float**: Decimal numbers (e.g., `3.14`, `-0.5`)
- **String**: Text data enclosed in quotes (e.g., `"Hello"`)
- **Boolean**: `True` or `False`

### Type Conversion
Convert between data types:
```python
x = int("10")  # Converts string to integer
y = float("5.5")  # Converts string to float
z = str(123)  # Converts integer to string
```

## 5. Basic Operations
### Arithmetic Operations
```python
a = 10 + 5  # Addition
b = 10 - 5  # Subtraction
c = 10 * 5  # Multiplication
d = 10 / 5  # Division
e = 10 % 3  # Modulus (remainder)
f = 2 ** 3  # Exponentiation (2 raised to power 3)
```

### Comparison Operators
Used to compare values, returning `True` or `False`.
```python
x == y  # Equals
x != y  # Not equals
x > y   # Greater than
x < y   # Less than
x >= y  # Greater than or equal to
x <= y  # Less than or equal to
```

## 6. Control Flow
### If Statements
```python
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```
### Switch case or match case
```python
  day = 1
  match day:
      case 1:
          return "Monday"
      case 2:
          return "Tuesday"
      case 3:
          return "Wednesday"
      case 4:
          return "Thursday"
      case 5:
          return "Friday"
      case 6:
          return "Saturday"
      case 7:
          return "Sunday"
      case _:
          return "Invalid day"
```
### Loops
- **For Loop**: Iterates over a sequence.
  ```python
  for i in range(5):
      print(i)  # Prints numbers from 0 to 4
  ```
- **While Loop**: Repeats while a condition is `True`.
  ```python
  count = 0
  while count < 5:
      print(count)
      count += 1  # Increment count
  ```

## 7. Functions
Functions are reusable blocks of code.
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Calls the function with "Alice"
```

### Return Values
Functions can return values.
```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # Outputs: 7
```

## 8. Basic Data Structures
### Lists
- Ordered and mutable collection of items.
  ```python
  fruits = ["apple", "banana", "cherry"]
  fruits.append("orange")  # Adds an item
  print(fruits[0])  # Accesses first item
  ```

### Tuples
- Ordered but immutable collection.
  ```python
  coordinates = (10, 20)
  ```

### Dictionaries
- Collection of key-value pairs.
  ```python
  person = {
      "name": "Alice",
      "age": 25
  }
  print(person["name"])  # Outputs: Alice
  ```

## 9. Error Handling
Catch and handle exceptions using `try-except`.
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## 10. Conclusion
You’ve covered the basics! You can now explore more advanced topics like object-oriented programming, working with libraries, file handling, and more.

---

Let me know if you want more details on any specific section or advanced topics!
