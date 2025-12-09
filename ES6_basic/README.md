# ES6 Basics


---

## 📝 Description

This project introduces the fundamentals of **ECMAScript 6 (ES6)**. You will explore modern JavaScript features such as arrow functions, block-scoped variables, rest/spread operators, iterators, and more.  
Your code will be tested with **Jest** and analyzed with **ESLint**.

---

## 📚 Resources

Recommended reading:

- ECMAScript 6 - ECMAScript 2015  
- Statements and declarations  
- Arrow functions  
- Default parameters  
- Rest parameter  
- JavaScript ES6 — Iterables and Iterators  

---

## 🎯 Learning Objectives (with Answers)

### **What ES6 is**

ES6 (ECMAScript 2015) is a major update to JavaScript introducing new syntax and features to make code more modern, clear, and powerful.

Example:

```js
// ES5
var x = 10;

// ES6
let y = 20;
const z = 30;
````

---

### **New features introduced in ES6**

Some major features include:

* `let` and `const`
* Arrow functions
* Template literals
* Default and rest parameters
* Spread operator
* Classes
* Promises
* Modules (`import` / `export`)
* Iterators and `for...of`

---

### **Difference between a constant and a variable**

* `let`: variable whose value can change.
* `const`: constant whose value cannot be reassigned (but objects can still be modified).

```js
let count = 1;
count = 2; // OK

const user = { name: "Ana" };
user.name = "Tom"; // OK (object can change)
```

---

### **Block-scoped variables**

`let` and `const` are limited to the block `{}` in which they are defined.

```js
if (true) {
  let x = 10;
}
console.log(x); // ❌ Error (x is block-scoped)
```

---

### **Arrow functions and default parameters**

Arrow functions provide shorter syntax and inherit `this`.

```js
const greet = (name = "Guest") => `Hello, ${name}`;

greet();       // "Hello, Guest"
greet("Ana");  // "Hello, Ana"
```

---

### **Rest and spread function parameters**

* **Rest (`...`)** collects multiple arguments into an array.
* **Spread (`...`)** expands an array into individual elements.

```js
// Rest
const sum = (...nums) => nums.reduce((a, b) => a + b);

// Spread
const arr = [1, 2, 3];
console.log(...arr); // 1 2 3
```

---

### **String templating in ES6**

Template literals allow embedded variables using backticks:

```js
const name = "Sam";
console.log(`Hello, ${name}!`);
```

---

### **Object creation and properties in ES6**

ES6 allows shorthand properties and method definitions.

```js
const age = 25;

const user = {
  age,
  greet() {
    console.log("Hi!");
  }
};
```

---

### **Iterators and for-of loops**

`for...of` loops through iterable objects like arrays and strings.

```js
for (const char of "ABC") {
  console.log(char);
}
// A B C
```

---

## 📌 Requirements

* Node 20.x.x, npm 9.x.x
* Code tested with **Jest**
* Code linted with **ESLint**
* All functions must be exported
* All files end with a newline

---

## 🛠️ Setup Instructions

### Install NodeJS 20

```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

### Install project dependencies

```bash
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env
npm install --save-dev eslint
npm install
```

---

## ▶️ Running Tests

```bash
npm test
```
```
