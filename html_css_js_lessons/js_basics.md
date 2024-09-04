
# Introduction to JavaScript
![alt text](images/js.png)
## Lesson 15: Your First JavaScript Program

### Objective:
- Write and execute a basic JavaScript program.
- Understand the basic syntax and structure of a JavaScript program.
### pre-requests
* Install nodejs 

#### 1. Introduction to JavaScript
- Briefly explain what JavaScript is:
  - JavaScript is a programming language that enables you to create dynamically updating content, control multimedia, animate images, and much more on web pages.
- Discuss the importance of JavaScript in modern web development.

#### 2. Setting Up Your Environment
- Demonstrate how to write JavaScript code:
  - Using the browser's developer tools (F12 > Console) or Using edge vscode browsers debugger

```js
 console.log("Hello, World!");
```

#### 3. Writing Your First Program: "Hello, World!" in js file
- create a javascript file either using vscode explorer or cli
```
touch <path>/index.js
```
- then write the following code in the index.js file

```javascript
console.log("Hello, World!");
```

- Explain:
  - `console.log`: This prints the specified message to the browser’s console.
  - Strings: In JavaScript, text is written inside quotation marks (either single or double quotes).

#### 4. Running the Program
- Show how to run the code:
  - either In the browser’s developer console.
  - or Using terminal nodejs as follows
   ```bash
   node <path>/index.js
   ```
### exercise:
- Write your own JavaScript program that prints your name in the console.

---

## Lesson 16: Variables and Data Types in JavaScript

### Objective:
- Understand what variables are and how they are used in JavaScript.
- Learn about the different data types in JavaScript.
  
#### 1. Introduction to Variables
- Explain what a variable is:
  - A container that stores data values.
- Introduce variable declaration and initialization:

```javascript
var name = "John"; // Using var keyword
let age = 25;      // Using let keyword
const pi = 3.14;   // Using const keyword
```

- Discuss the difference between `var`, `let`, and `const`:
  - `var`: Function-scoped and can be re-declared.
  - `let`: Block-scoped and cannot be re-declared.
  - `const`: Block-scoped, and its value cannot be changed.

#### 2. Data Types in JavaScript
- Introduce the different data types in JavaScript:
  - **String:** Represents textual data (e.g., `"Hello, World!"`).
  - **Number:** Represents numeric values (e.g., `100`, `3.14`).
  - **Boolean:** Represents true/false values (e.g., `true`, `false`).
  - **Undefined:** A variable that has been declared but not assigned a value.
  - **Null:** Represents an empty or non-existent value.
  - **Object:** Represents collections of data or more complex entities (e.g., `{ name: "John", age: 25 }`).
  - **Array:** A special type of object used to store multiple values (e.g., `[1, 2, 3]`).

#### 3. Examples of Variables and Data Types
- Write examples demonstrating different data types:

```javascript
let name = "Alice";       // String
let age = 30;             // Number
let isStudent = true;     // Boolean
let address;              // Undefined
let result = null;        // Null
let person = {            // Object
    firstName: "John",
    lastName: "Doe",
    age: 25
};
let numbers = [1, 2, 3];  // Array
```

- Explain how to check the data type using `typeof`:

```javascript
console.log(typeof name); // Output: "string"
console.log(typeof age);  // Output: "number"
```

#### 4. Hands-On Activity 

```javascript
let favoriteColor = "Blue";
let numberOfPets = 2;
let isRaining = false;

console.log(favoriteColor);
console.log(numberOfPets);
console.log(isRaining);
```
 
### exercise:
- Create a JavaScript program that declares and prints five variables with different data types.

---

## Lesson 17: Operators and Expressions in JavaScript

### Objective:
- Understand and use different operators in JavaScript.
- Learn how to create expressions using operators.


#### 1. Introduction to Operators
- Explain what operators are:
  - Operators are used to perform operations on variables and values.
- Discuss different types of operators:
  - **Arithmetic Operators:** Used for mathematical operations (e.g., `+`, `-`, `*`, `/`, `%`).
  - **Assignment Operators:** Used to assign values to variables (e.g., `=`, `+=`, `-=`, `*=`, `/=`).
  - **Comparison Operators:** Used to compare two values (e.g., `==`, `===`, `!=`, `<`, `>`, `<=`, `>=`).
  - **Logical Operators:** Used to perform logical operations (e.g., `&&`, `||`, `!`).
  - **Unary Operators:** Operate on a single operand (e.g., `typeof`, `++`, `--`).
  - **Ternary Operator:** A shorthand for an if-else statement (e.g., `condition ? value1 : value2`).

#### 2. Examples of Arithmetic and Assignment Operators
- Show examples using arithmetic operators:

```javascript
let sum = 10 + 5;       // Addition
let difference = 10 - 5; // Subtraction
let product = 10 * 5;    // Multiplication
let quotient = 10 / 5;   // Division
let remainder = 10 % 3;  // Modulus
```

- Demonstrate assignment operators:

```javascript
let x = 10;
x += 5; // Equivalent to: x = x + 5
console.log(x); // Output: 15
```

#### 3. Comparison and Logical Operators
- Provide examples of comparison operators:

```javascript
console.log(10 == 10);   // true
console.log(10 === "10"); // false (strict equality)
console.log(10 != 5);    // true
console.log(10 > 5);     // true
```

- Demonstrate logical operators:

```javascript
let a = true;
let b = false;

console.log(a && b); // false (AND)
console.log(a || b); // true (OR)
console.log(!a);     // false (NOT)
```

#### exercise
  - Write a program that calculates the total cost of 5 items, applies a discount, and determines if the final cost is within a budget.

#### 5. Ternary Operator
- Introduce and demonstrate the ternary operator:

```javascript
let age = 18;
let canVote = (age >= 18) ? "Yes" : "No";
console.log(canVote); // Output: "Yes"
```

#### 6. Summary and Discussion
- Recap different types of operators and their use  

### Homework:
- Write a JavaScript program that uses arithmetic, comparison, and logical operators to evaluate conditions and print the results.
