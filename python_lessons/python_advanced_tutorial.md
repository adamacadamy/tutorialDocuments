
# Python Advanced Tutorial

## 1. Object-Oriented Programming (OOP)

### Classes and Objects
- **Classes** are blueprints for creating objects, which are instances of classes.
- **Objects** are instances of classes, containing attributes (variables) and methods (functions).

#### Defining a Class
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name  # Attribute
        self.breed = breed  # Attribute

    def bark(self):  # Method
        return f"{self.name} says woof!"
```

#### Creating an Object
```python
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())  # Outputs: Buddy says woof!
```

### Inheritance
- **Inheritance** allows a class to inherit attributes and methods from another class.

#### Example
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Cat(Animal):  # Inherits from Animal
    def speak(self):
        return f"{self.name} says meow!"

my_cat = Cat("Whiskers")
print(my_cat.speak())  # Outputs: Whiskers says meow!
```

### Encapsulation
- **Encapsulation** restricts access to certain attributes and methods, using underscores to indicate "private" elements.

#### Example
```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected attribute

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Outputs: 1500
```

### Polymorphism
- **Polymorphism** allows methods to be used interchangeably across different classes.

#### Example
```python
class Bird:
    def speak(self):
        return "Chirp"

class Fish:
    def speak(self):
        return "Blub"

animals = [Bird(), Fish()]

for animal in animals:
    print(animal.speak())  # Outputs: Chirp, Blub
```

### Abstract Classes
- **Abstract classes** are classes that cannot be instantiated directly and must be inherited.
- They are created using the `abc` module.

#### Example
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())  # Outputs: 78.5
```

## 2. Working with the `requests` Library

### Making HTTP Requests
- The `requests` library allows you to send HTTP requests easily.

#### Installing `requests`
```bash
pip install requests
```

#### GET Request
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # Outputs: 200
print(response.json())  # Outputs: JSON response
```

#### POST Request
```python
data = {"name": "test", "description": "some test repository"}
response = requests.post("https://api.github.com/user/repos", json=data, auth=("username", "password"))
print(response.status_code)
```

### Handling Errors
- Handle HTTP errors using `raise_for_status()` or checking `status_code`.

#### Example
```python
try:
    response = requests.get("https://api.github.com/invalid-endpoint")
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
```

## 3. Advanced Topics in Python

### Generators
- **Generators** are special functions that return an iterator with `yield`.

#### Example
```python
def countdown(num):
    while num > 0:
        yield num
        num -= 1

for number in countdown(5):
    print(number)  # Outputs: 5, 4, 3, 2, 1
```

### Decorators
- **Decorators** are functions that modify the behavior of other functions.

#### Example
```python
def decorator_function(func):
    def wrapper():
        print("Function is being called")
        func()
        print("Function call finished")
    return wrapper

@decorator_function
def greet():
    print("Hello!")

greet()
```

### Context Managers
- **Context managers** use `with` to handle resource management.

#### Example
```python
with open("example.txt", "w") as file:
    file.write("Hello, World!")
```

### Multithreading and Multiprocessing
- **Multithreading** allows multiple threads to run concurrently.
- **Multiprocessing** allows multiple processes to run in parallel.

#### Example of Multithreading
```python
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
```

#### Example of Multiprocessing
```python
import multiprocessing

def print_numbers():
    for i in range(5):
        print(i)

process = multiprocessing.Process(target=print_numbers)
process.start()
process.join()
```

### Working with JSON
- The `json` module helps parse and generate JSON data.

#### Example
```python
import json

data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)
parsed_data = json.loads(json_string)
print(parsed_data["name"])  # Outputs: Alice
```

### Regular Expressions
- **Regular expressions** (`re` module) are used for pattern matching in strings.

#### Example
```python
import re

pattern = r"\d+"
text = "There are 123 apples"
match = re.findall(pattern, text)
print(match)  # Outputs: ['123']
```

## 4. Web Scraping with BeautifulSoup

### Installing `beautifulsoup4`
```bash
pip install beautifulsoup4
```

### Basic Usage
```python
from bs4 import BeautifulSoup
import requests

response = requests.get("https://example.com")
soup = BeautifulSoup(response.content, "html.parser")
print(soup.title.text)
```

### Extracting Data
```python
links = soup.find_all("a")
for link in links:
    print(link.get("href"))
```

## 5. Database Interactions with SQLite

### Creating a Database
```python
import sqlite3

connection = sqlite3.connect("example.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
connection.commit()
connection.close()
```

### Inserting Data
```python
connection = sqlite3.connect("example.db")
cursor = connection.cursor()
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
connection.commit()
connection.close()
```

### Querying Data
```python
connection = sqlite3.connect("example.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.close()
```

## 6. Conclusion
You've now covered advanced topics such as OOP, making HTTP requests, working with generators, decorators, multithreading, JSON handling, regular expressions, web scraping, and database interactions.

---

Let me know if you want a more in-depth explanation on any topic!
