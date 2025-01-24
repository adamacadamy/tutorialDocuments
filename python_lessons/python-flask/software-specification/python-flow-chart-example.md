# Python Function Examples and Flowcharts

Below are examples of Python functions along with their corresponding flowcharts to visually represent their logic and flow.

---

## **1. Example: Greeting Function**

### **Python Code**
```python
def greet(name):
    """
    Greets the user with their name.
    """
    if not name:
        return "Hello, Stranger!"
    return f"Hello, {name}!"

# Example Calls
print(greet("Alice"))  # Output: Hello, Alice!
print(greet(""))       # Output: Hello, Stranger!
```

### **Flowchart**
```text
+----------------------+  
|       Start          |  
+----------------------+  
         |
         v
+----------------------+  
| Is name provided?    |
+----------------------+  
     |       |
     | No    | Yes
     v       v
+-----------------+  +--------------------+
| Return 'Hello,  |  | Return 'Hello,     |
| Stranger!'      |  | {name}!'           |
+-----------------+  +--------------------+
         |
         v
+----------------------+  
|        End           |
+----------------------+  
```

---

## **2. Example: Sum of Two Numbers**

### **Python Code**
```python
def add_numbers(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b

# Example Call
result = add_numbers(5, 3)  # Output: 8
print(f"The sum is: {result}")
```

### **Flowchart**
```text
+----------------------+  
|       Start          |  
+----------------------+  
         |
         v
+----------------------+  
| Accept inputs: a, b  |
+----------------------+  
         |
         v
+----------------------+  
| Calculate sum (a + b)|
+----------------------+  
         |
         v
+----------------------+  
| Return the sum       |
+----------------------+  
         |
         v
+----------------------+  
|        End           |
+----------------------+  
```

---

## **3. Example: Factorial Calculation**

### **Python Code**
```python
def factorial(n):
    """
    Returns the factorial of a number.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example Call
print(factorial(5))  # Output: 120
```

### **Flowchart**
```text
+----------------------+  
|       Start          |  
+----------------------+  
         |
         v
+----------------------+  
| Is n = 0 or n = 1?   |
+----------------------+  
     | Yes  | No
     v      v
+----------------+  +----------------------+
| Return 1       |  | Calculate n * fact(n-1)|
+----------------+  +----------------------+
                             |
                             v
+----------------------+  
| Return result        |
+----------------------+  
         |
         v
+----------------------+  
|        End           |
+----------------------+  
```

---

## **4. Example: Checking Even or Odd**

### **Python Code**
```python
def is_even(number):
    """
    Checks if a number is even.
    """
    if number % 2 == 0:
        return True
    return False

# Example Call
print(is_even(4))  # Output: True
print(is_even(7))  # Output: False
```

### **Flowchart**
```text
+----------------------+  
|       Start          |  
+----------------------+  
         |
         v
+----------------------+  
| Accept number input  |
+----------------------+  
         |
         v
+----------------------+  
| Is number % 2 == 0?  |
+----------------------+  
     | Yes  | No
     v      v
+----------------+  +----------------+
| Return True    |  | Return False   |
+----------------+  +----------------+
         |
         v
+----------------------+  
|        End           |
+----------------------+  
```

---

By combining Python functions with flowcharts, you can clearly visualize the logical steps each function takes, making it easier to understand and debug your code. Let me know if you'd like to explore more complex examples!

