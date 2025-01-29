### **JavaScript Basics**

#### **Objective:**
Teach the fundamentals of JavaScript, focusing on variables, data types, functions (with different writing styles), loops, and data structures, all within Jupyter Notebook.

---

### **Lesson Outline**

#### **1. Variables**
- **Key Points:**
  - Declaration keywords: `var`, `let`, `const`.
- **Example:**
  ```javascript
  var x = 5; // function-scoped
  let y = 10; // block-scoped
  const z = 15; // block-scoped, immutable
  console.log(x, y, z);
  ```

---

#### **2. Data Types**
- **Primitive Types:**
  - `string`, `number`, `boolean`, `undefined`, `null`, `symbol`, `bigint`.
- **Examples:**
  ```javascript
  let name = "John"; // string
  let age = 30; // number
  let isStudent = false; // boolean
  let notAssigned; // undefined
  let emptyValue = null; // null
  ```

- **Complex Types:**
  - **Array:** An ordered list of values.
    ```javascript 
    const numbers = [1, 2, 3, 4, 5];
    console.log(numbers);
    ```
  - **Object:** A collection of key-value pairs.
    ```javascript
    
    const person = {
      name: "Alice",
      age: 25
    };
    console.log(person);
    ```
  - **Set:** A collection of unique values.
    ```javascript 
    const uniqueValues = new Set(["a", "b", "a"]);
    console.log(uniqueValues);
    ```
  - **Map:** A collection of key-value pairs where keys can be of any type.
    ```javascript 
    const map = new Map();
    map.set("one", 1);
    map.set("two", 2);
    console.log(map);
    ```

---

#### **3. Functions**
- **Different Ways to Write Functions:**

1. **Function Declaration** (Traditional way):
   ```javascript 
   function greet(name) {
     return `Hello, ${name}!`;
   }
   console.log(greet("Alice"));
   ```

2. **Function Expression** (Anonymous function assigned to a variable):
   ```javascript 
   const greet = function(name) {
     return `Hello, ${name}!`;
   };
   console.log(greet("Bob"));
   ```

3. **Arrow Function** (Concise syntax):
   ```javascript 
   const greet = (name) => `Hello, ${name}!`;
   console.log(greet("Charlie"));
   ```

4. **Immediately Invoked Function Expression (IIFE):**
   ```javascript 
   (function() {
     console.log("This function runs immediately!");
   })();
   ```

5. **Method in an Object:**
   ```javascript 
   const person = {
     name: "Dana",
     greet() {
       return `Hi, I'm ${this.name}`;
     },
   };
   console.log(person.greet());
   ```

6. **Constructor Function** (Used for creating objects):
   ```javascript 
   function Person(name) {
     this.name = name;
   }
   const p = new Person("Eve");
   console.log(p.name);
   ```

7. **Class Method** (Introduced in ES6):
   ```javascript 
   class Person { 
     constructor(name) {
       this.name = name;
     } 
     greet() {
       return `Hi, I'm ${this.name}`;
     }
   }
   const p = new Person("Frank");
   console.log(p.greet());
   ```

---

#### **4. Loops**
- **Common Loops:**
  - `for` loop:
    ```javascript 
    for (let i = 0; i < 5; i++) {
      console.log(i);
    }
    ```
  - `while` loop:
    ```javascript 
    let count = 0;
    while (count < 3) {
      console.log(count);
      count++;
    }
    ```
  - `for...of` (iterating over arrays):
    ```javascript 
    const colors = ["red", "green", "blue"];
    for (const color of colors) {
      console.log(color);
    }
    ```
  ---

  - **Looping Through Object Keys and Values:**
    ```javascript
    const person = {
      name: "Alice",
      age: 25,
      city: "Wonderland"
    };

    // Using for...in to iterate through keys
    for (const key in person) {
      console.log(`${key}: ${person[key]}`);
    }

    // Using Object.entries() to iterate through key-value pairs
    Object.entries(person).forEach(([key, value]) => {
      console.log(`${key}: ${value}`);
    });
    ```


---

#### **5. Data Structures**
- **Arrays:**
  ```javascript 
  const fruits = ["apple", "banana", "cherry"];
  console.log(fruits[0]); // Access first element
  fruits.push("date"); // Add an element
  console.log(fruits);
  ```

- **Objects:**
  ```javascript 
  const person = {
    name: "Alice",
    age: 25,
    greet: function () {
      return `Hi, I'm ${this.name}`;
    },
  };
  console.log(person.name); // Access property
  console.log(person.greet()); // Call method
  ```

- **Array Methods:**
  - **forEach:** Iterates over an array and executes a function for each element.
    ```javascript 
    const numbers = [1, 2, 3, 4];
    numbers.forEach(num => console.log(num * 2));
    ```
  - **map:** Creates a new array by applying a function to each element.
    ```javascript 
    const squared = numbers.map(num => num * num);
    console.log(squared);
    ```
  - **filter:** Creates a new array with elements that pass a test.
    ```javascript 
    const evenNumbers = numbers.filter(num => num % 2 === 0);
    console.log(evenNumbers);
    ```
  - **map and filter combined:** Applying transformations and filtering results.
    ```javascript 
    const doubledEvenNumbers = numbers.map(num => num * 2).filter(num => num > 4);
    console.log(doubledEvenNumbers);
    ```

---
 