
# Python Intermediate Tutorial

## 1. Advanced Data Structures

### Lists
- **Lists** are ordered, mutable collections of elements that can contain duplicates. Lists support various built-in functions for manipulation.

#### Built-in Functions for Lists:
1. `append(item)`: Adds an item to the end of the list.
2. `insert(index, item)`: Inserts an item at a specified index.
3. `remove(item)`: Removes the first occurrence of an item.
4. `pop(index)`: Removes and returns an item at the given index (default is the last item).
5. `clear()`: Removes all items from the list.
6. `index(item)`: Returns the index of the first occurrence of an item.
7. `count(item)`: Returns the number of occurrences of an item.
8. `sort(reverse=False)`: Sorts the list in ascending order by default; set `reverse=True` for descending order.
9. `reverse()`: Reverses the order of the list.
10. `copy()`: Returns a shallow copy of the list.
11. `extend(iterable)`: Adds elements from another iterable (e.g., list) to the end of the list.

#### Example Usage:
```python
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert(0, 0)
numbers.remove(3)
print(numbers.pop())       # Outputs: 6
numbers.sort(reverse=True)
```

### Tuples
- **Tuples** are ordered, immutable collections. Their values cannot be changed after creation.

#### Built-in Functions for Tuples:
1. `count(item)`: Returns the number of occurrences of an item.
2. `index(item)`: Returns the index of the first occurrence of an item.

#### Example Usage:
```python
point = (1, 2, 3, 4, 2)
print(point.count(2))  # Outputs: 2
print(point.index(3))  # Outputs: 2
```

### Sets
- **Sets** are unordered collections of unique elements. They do not allow duplicates.

#### Built-in Functions for Sets:
1. `add(item)`: Adds an item to the set.
2. `remove(item)`: Removes an item from the set; raises `KeyError` if not found.
3. `discard(item)`: Removes an item if present, without raising an error.
4. `pop()`: Removes and returns an arbitrary set element.
5. `clear()`: Removes all elements from the set.
6. `copy()`: Returns a shallow copy of the set.
7. `union(other_set)`: Returns a new set with elements from both sets.
8. `intersection(other_set)`: Returns a new set with elements common to both sets.
9. `difference(other_set)`: Returns a new set with elements in the set that are not in the other set.
10. `symmetric_difference(other_set)`: Returns a new set with elements in either set but not in both.
11. `update(other_set)`: Adds elements from another set.
12. `intersection_update(other_set)`: Retains only elements found in both sets.
13. `difference_update(other_set)`: Removes elements found in another set.
14. `symmetric_difference_update(other_set)`: Retains elements in either set but not both.

#### Example Usage:
```python
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
fruits.remove("banana")
new_fruits = fruits.union({"mango", "grapes"})
common_fruits = fruits.intersection({"apple", "mango"})
```

### Dictionaries
- **Dictionaries** are collections of key-value pairs, where each key is unique.

#### Built-in Functions for Dictionaries:
1. `keys()`: Returns a view object containing the dictionary's keys.
2. `values()`: Returns a view object containing the dictionary's values.
3. `items()`: Returns a view object containing key-value pairs as tuples.
4. `get(key, default)`: Returns the value for a key, or `default` if the key is not found.
5. `pop(key, default)`: Removes and returns the value for a key, or `default` if the key is not found.
6. `popitem()`: Removes and returns the last inserted key-value pair.
7. `clear()`: Removes all key-value pairs from the dictionary.
8. `update(other_dict)`: Updates the dictionary with key-value pairs from another dictionary.
9. `copy()`: Returns a shallow copy of the dictionary.
10. `setdefault(key, default)`: Returns the value for a key if it exists; otherwise, sets it to `default`.

#### Example Usage:
```python
student = {"name": "Alice", "age": 25}
student["age"] = 26
student.update({"major": "Physics"})
print(student.keys())      # Outputs: dict_keys(['name', 'age', 'major'])
print(student.values())    # Outputs: dict_values(['Alice', 26, 'Physics'])
```

## 2. Advanced Looping Techniques

### `for` Loops
- A **`for` loop** is used to iterate over a sequence (such as a list, tuple, string, or range). It allows executing a block of code multiple times, once for each element in the sequence.

#### Example Usage:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Outputs: apple, banana, cherry
```

- **Looping with the `range()` function**:
  ```python
  for i in range(5):
      print(i)  # Outputs: 0, 1, 2, 3, 4
  ```

- **Using `else` with `for` loops**:
  ```python
  for i in range(3):
      print(i)
  else:
      print("Loop completed")  # Outputs: Loop completed
  ```

### `while` Loops
- A **`while` loop** executes a block of code as long as a specified condition is `True`.

#### Example Usage:
```python
count = 0
while count < 5:
    print(count)
    count += 1  # Outputs: 0, 1, 2, 3, 4
```

- **Breaking out of a `while` loop with `break`**:
  ```python
  count = 0
  while count < 5:
      if count == 3:
          break
      print(count)  # Outputs: 0, 1, 2
      count += 1
  ```

## 3. Advanced Functions

### Lambda Functions
- **Lambda functions** are small anonymous functions defined with the `lambda` keyword. They can have any number of arguments but only one expression.
  
#### Example Usage:
```python
add = lambda x, y: x + y
print(add(2, 3))  # Outputs: 5
```

### Map, Filter, and Reduce
- `map`: Apply a function to all items in a list.
  ```python
  numbers = [1, 2, 3, 4, 5]
  squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]
  ```

- `filter`: Filter items based on a function.
  ```python
  evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
  ```

- `reduce`: Apply a rolling computation.
  ```python
  from functools import reduce
  total = reduce(lambda x, y: x + y, numbers)  # 15
  ```

## 4. Working with Files

### Reading and Writing Files
- Open a file with `open()` and use `read()` or `write()`.
  ```python
  with open("sample.txt", "w") as file:
      file.write("Hello, World!")

  with open("sample.txt", "r") as file:
      content = file.read()
      print(content)
  ```

## 5. Error Handling

### Try-Except-Else-Finally
- Use `try` for code that may cause exceptions.
- Use `except` to catch exceptions.
- Use `else` to run code if no exceptions occur.
- Use `finally` to run code regardless of what happens.
  ```python
  try:
      number = int(input("Enter a number: "))
  except ValueError:
      print("Invalid input. Please enter a number.")
  else:
      print(f"You entered {number}")
  finally:
      print("End of program")
  ```

## 6. Modules and Packages

### Importing Modules
```python
import math
print(math.sqrt(16))  # Outputs: 4.0
```

### Creating Your Own Modules
```python
# file: my_module.py
def greet(name):
    return f"Hello, {name}!"
```

## 7. Conclusion
You’ve covered intermediate topics, including data structures, loops, and built-in functions!

---

Let me know if you need further explanations!
