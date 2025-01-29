### **JavaScript Advanced Lessons**

#### **Objective:**
Explore advanced JavaScript concepts such as closures, prototypes, classes, modules, and advanced asynchronous programming techniques to deepen understanding.

---

### **Lesson Outline**

#### **1. Closures**
- **Definition:** A closure is a function that retains access to its lexical scope even when executed outside that scope.
- **Examples:**
  ```javascript
  function outerFunction(outerVariable) {
    return function innerFunction(innerVariable) {
      console.log(`Outer: ${outerVariable}, Inner: ${innerVariable}`);
    };
  }

  const closureExample = outerFunction("outside");
  closureExample("inside"); // Outer: outside, Inner: inside
  ```

---

#### **2. Prototypes and Inheritance**
- **Prototype Chain:**
  ```javascript
  function Person(name) {
    this.name = name;
  }

  Person.prototype.greet = function() {
    return `Hello, my name is ${this.name}`;
  };

  const alice = new Person("Alice");
  console.log(alice.greet()); // Hello, my name is Alice
  ```

- **Class Syntax with Prototypes:**
  ```javascript
  class Person {
    constructor(name) {
      this.name = name;
    }

    greet() {
      return `Hello, my name is ${this.name}`;
    }
  }

  const bob = new Person("Bob");
  console.log(bob.greet()); // Hello, my name is Bob
  ```

---

#### **3. Modules**
- **Export and Import:**
  - `export` allows pieces of code to be reused across files.
  ```javascript
  // math.js
  export const add = (a, b) => a + b;
  export const multiply = (a, b) => a * b;
  ```

  ```javascript
  // main.js
  import { add, multiply } from './math.js';

  console.log(add(2, 3)); // 5
  console.log(multiply(2, 3)); // 6
  ```

---

#### **4. Advanced Asynchronous Programming**
- **Promise Chaining:**
  ```javascript
  fetch("https://api.example.com/data")
    .then(response => response.json())
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.error("Error fetching data:", error);
    });
  ```

- **Async/Await with Error Handling:**
  ```javascript
  const fetchData = async () => {
    try {
      const response = await fetch("https://api.example.com/data");
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  fetchData();
  ```

---

#### **5. Advanced Class Features**
- **Static Methods:**
  ```javascript
  class MathUtils {
    static add(a, b) {
      return a + b;
    }
  }

  console.log(MathUtils.add(2, 3)); // 5
  ```

- **Getters and Setters:**
  ```javascript
  class Rectangle {
    constructor(width, height) {
      this.width = width;
      this.height = height;
    }

    get area() {
      return this.width * this.height;
    }

    set resize(factor) {
      this.width *= factor;
      this.height *= factor;
    }
  }

  const rect = new Rectangle(4, 5);
  console.log(rect.area); // 20
  rect.resize = 2;
  console.log(rect.area); // 80
  ```

---

#### **6. Package Management with npm**
- **Key Commands:**
  ```bash
  npm init -y # Creates a package.json file
  npm install <package-name> # Uninstalls a package
  npm uninstall <package-name> # Uninstalls a package
  npm update # Updates all dependencies
  ```

---
- **Installing npm Packages:**
  - npm (Node Package Manager) is used to manage JavaScript packages and dependencies.
  ```bash
  npm install <package-name> # Installs a package locally
  npm install -g <package-name> # Installs a package globally
  ```

- **Using a Package:**
  ```javascript
  // Example: Installing and using lodash
  // Install: npm install lodash
  const _ = require('lodash');

  const numbers = [1, 2, 3, 4];
  console.log(_.shuffle(numbers)); // Shuffles the array
  ```



 