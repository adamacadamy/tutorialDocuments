### **JavaScript Intermediate Lessons**

#### **Objective:**
Build on JavaScript fundamentals by introducing intermediate concepts such as higher-order functions, advanced object manipulation, asynchronous programming, and the JavaScript event loop.

---

### **Lesson Outline**

#### **1. Higher-Order Functions**
- **Definition:** Functions that take other functions as arguments or return them.
- **Examples:**
  ```javascript
  // Function accepting a callback
  function calculate(a, b, operation) {
    return operation(a, b);
  }

  const add = (x, y) => x + y;
  const multiply = (x, y) => x * y;

  console.log(calculate(5, 3, add)); // 8
  console.log(calculate(5, 3, multiply)); // 15
  ```

  - **Built-in Higher-Order Functions:**
    - `map`, `filter`, `reduce`.
    ```javascript
    const numbers = [1, 2, 3, 4];

    // map
    const doubled = numbers.map(num => num * 2);
    console.log(doubled); // [2, 4, 6, 8]

    // filter
    const evens = numbers.filter(num => num % 2 === 0);
    console.log(evens); // [2, 4]

    // reduce
    const sum = numbers.reduce((total, num) => total + num, 0);
    console.log(sum); // 10
    ```

---

#### **2. Advanced Object Manipulation**
- **Object Destructuring:**
  ```javascript
  const person = {
    name: "Alice",
    age: 25,
    address: {
      city: "Wonderland",
      zip: 12345
    }
  };

  const { name, age, address: { city } } = person;
  console.log(name, age, city); // Alice 25 Wonderland
  ```

- **Object Spread and Rest Operators:**
  ```javascript
  const obj1 = { a: 1, b: 2 };
  const obj2 = { c: 3, d: 4 };

  // Spread operator
  const combined = { ...obj1, ...obj2 };
  console.log(combined); // { a: 1, b: 2, c: 3, d: 4 }

  // Rest operator
  const { a, ...rest } = combined;
  console.log(a, rest); // 1 { b: 2, c: 3, d: 4 }
  ```

- **List Destructuring:**
  ```javascript
  const numbers = [1, 2, 3, 4, 5];

  // Destructuring the first two elements
  const [first, second] = numbers;
  console.log(first, second); // 1 2

  // Using rest to collect the remaining elements
  const [head, ...tail] = numbers;
  console.log(head, tail); // 1 [2, 3, 4, 5]

  // Skipping elements
  const [, , third] = numbers;
  console.log(third); // 3
  ```

---

#### **3. Asynchronous Programming**
- **Promises:**
  ```javascript
  const fetchData = () => {
    return new Promise((resolve, reject) => {
      setTimeout(() => resolve("Data received"), 2000);
    });
  };

  fetchData().then(data => console.log(data));
  ```

- **Async/Await:**
  ```javascript
  const fetchData = async () => {
    const data = await new Promise(resolve => {
      setTimeout(() => resolve("Data received"), 2000);
    });
    console.log(data);
  };

  fetchData();
  ```

---

#### **4. JavaScript Event Loop**
- **Understanding the Call Stack and Task Queue:**
  ```javascript
  console.log("Start");

  setTimeout(() => {
    console.log("Timeout");
  }, 0);

  console.log("End");
  // Output: Start, End, Timeout
  ```
  **Explanation:** The event loop processes tasks in the stack before handling tasks in the queue.

---

#### **5. Error Handling**
- **Try-Catch:**
  ```javascript
  try {
    const result = JSON.parse("invalid JSON");
  } catch (error) {
    console.error("Error parsing JSON:", error.message);
  }
  ```

- **Finally:**
  ```javascript
  try {
    console.log("Trying...");
  } finally {
    console.log("Finally block executes regardless of success or failure.");
  }
  ```

---
 