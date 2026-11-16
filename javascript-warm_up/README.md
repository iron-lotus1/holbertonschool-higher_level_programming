# JavaScript - Warm Up 🚀

Welcome to my **JavaScript - Warm Up** repository! This directory is part of my journey through the **Holberton School Higher-Level Programming** curriculum, where I am transitioning from low-level programming (C) and Python into JavaScript using Node.js.

Rather than just storing completed tasks, this README serves as a **living study guide**—documenting the core concepts I am learning, runnable examples, and self-check practice questions to reinforce my understanding.

---

## 🎯 Learning Objectives

Through the exercises in this folder, I am practicing how to:
- Run JavaScript scripts outside the browser using **Node.js** (`#!/usr/bin/node`).
- Declare variables properly using `const` and `let` (and understand why `var` is avoided).
- Read command-line arguments in Node using `process.argv`.
- Handle dynamic typing, type conversion (`parseInt()`, `Number()`), and `NaN` checks.
- Control program flow with `if/else` statements, `for` loops, and `while` loops.
- Write reusable functions, recursion, and export modules (`module.exports` / `require`).
- Manipulate basic arrays and JavaScript objects.

---

## 🛠️ Environment & Setup

All scripts in this directory are written to conform to **semistandard** style guidelines and executed on Ubuntu using Node.js.

```bash
# Make a script executable
chmod +x 0-javascript_is_amazing.js

# Run a script directly
./0-javascript_is_amazing.js

# Or run using node
node 0-javascript_is_amazing.js
```

---

## 📂 Project Breakdown

| File | Concept Covered | Description |
| :--- | :--- | :--- |
| `0-javascript_is_amazing.js` | Constants & Output | Declares a `const` variable and prints it with `console.log()`. |
| `1-multi_languages.js` | Multi-line Output | Prints three distinct lines to standard output. |
| `2-arguments.js` | `process.argv` | Checks the count of command-line arguments passed to the script. |
| `3-value_argument.js` | Argument Indexing | Prints the first user-supplied argument without using `.length`. |
| `4-concat.js` | String Concatenation | Combines two passed arguments into a formatted sentence. |
| `5-to_integer.js` | Type Conversion | Converts the first argument to an integer and handles `NaN`. |
| `6-multi_languages_loop.js` | Arrays & Loops | Iterates through an array of strings to print multiple lines. |
| `7-multi_c.js` | Loops & Validation | Prints `"C is fun"` $x$ times based on a command-line integer. |
| `8-square.js` | Nested Loops | Prints a square of size $x$ using the character `X`. |
| `9-add.js` | Functions | Defines an `add(a, b)` function to sum two integers. |
| `10-factorial.js` | Recursion | Computes and prints a factorial recursively (`NaN` defaults to `1`). |
| `11-second_biggest.js` | Array Sorting / Logic | Finds the second largest integer from a list of arguments. |
| `12-object.js` | Objects | Mutates a property inside an existing JavaScript object. |
| `13-add.js` | Modules (`exports`) | Exports an `add` function so it can be imported by external files. |

---

## 💡 Key Concepts & Examples

### 1. Command-Line Arguments (`process.argv`)
In Node.js, `process.argv` is an array containing the command-line arguments passed when the process was launched:
- `process.argv[0]` $\rightarrow$ Path to the `node` executable
- `process.argv[1]` $\rightarrow$ Path to the JavaScript file being executed
- `process.argv[2]` $\rightarrow$ **First actual argument** passed by the user

```javascript
#!/usr/bin/node
const args = process.argv.slice(2); // Grabs only user-provided arguments

if (args.length === 0) {
  console.log('No argument');
} else {
  console.log(`First argument: ${args[0]}`);
}
```

### 2. Safe Type Conversion
Because all `process.argv` elements arrive as strings, arithmetic requires converting them to numbers and checking for `NaN` (Not-a-Number):

```javascript
#!/usr/bin/node
const num = parseInt(process.argv[2], 10);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
```

### 3. Exporting & Importing Modules (CommonJS)
To make a function available to another file (like in `13-add.js`):

```javascript
// mathHelper.js
exports.add = function (a, b) {
  return a + b;
};

// main.js
const { add } = require('./mathHelper');
console.log(add(4, 7)); // Output: 11
```

---

## 🧠 Knowledge Check: Practice Questions

Test your understanding of the concepts in this repository! Try answering before expanding the solutions.

### Question 1: `const` vs. Objects
Look at the following snippet. Will this throw a `TypeError` when executed? Why or why not?
```javascript
const user = { name: 'Holberton', level: 1 };
user.level = 2;
console.log(user.level);
```
<details>
<summary><strong>Click to reveal answer</strong></summary>

**No, it will not throw an error.** It will print `2`.  
`const` prevents **reassignment** of the variable binding (`user = ...`), not **mutation** of the object's internal properties. This is the exact concept practiced in `12-object.js`.
</details>

---

### Question 2: Argument Indexing
If you run `./script.js hello world`, what is the value of `process.argv.length`?
<details>
<summary><strong>Click to reveal answer</strong></summary>

The length is **`4`**.  
- `[0]`: `/usr/bin/node`  
- `[1]`: `./script.js`  
- `[2]`: `'hello'`  
- `[3]`: `'world'`
</details>

---

### Question 3: Mini Coding Challenge (Write from Scratch)
Write a small Node.js script that takes a list of numbers from the command line and prints the **sum of only the even numbers**. If no numbers are provided, print `0`.

*Example:* `./sum_evens.js 1 2 3 4 5 6` $\rightarrow$ `12`

<details>
<summary><strong>Click to reveal sample solution</strong></summary>

```javascript
#!/usr/bin/node
const args = process.argv.slice(2);
let sum = 0;

for (let i = 0; i < args.length; i++) {
  const num = parseInt(args[i], 10);
  if (!isNaN(num) && num % 2 === 0) {
    sum += num;
  }
}

console.log(sum);
```
</details>

---

## 🔜 Next Up
After warming up with JavaScript syntax and control flow, the next step in this repository is diving into **`javascript_objects_scopes_closures`** to explore prototypes, classes, `this`, and lexical scoping!
