# 🐍 Python - Object-Relational Mapping (ORM)

Welcome! If you are learning how to connect Python applications to a MySQL database, you are in the right place. This repository contains a step-by-step progression from writing raw SQL queries inside Python to using an **Object-Relational Mapper (ORM)** to manipulate database tables just like regular Python objects.

---

## 🧠 Core Concepts (Beginner's Guide)

Before diving into the files, here are the two main approaches used in this project:

### 1. Direct Database Connection (`MySQLdb`)
In the first half of this project (`0` through `5`), we use the `MySQLdb` library. 
* **How it works:** Python opens a connection to your MySQL server, creates a "cursor" (a pointer used to execute commands), and sends raw SQL strings (like `SELECT * FROM states`) directly to the database.
* **Pros:** Fast and straightforward if you already know SQL.
* **Cons:** Mixing SQL strings inside Python code can get messy, and if you aren't careful, you can accidentally leave your code vulnerable to **SQL Injection** attacks (which we explore in tasks `2` and `3`).

### 2. Object-Relational Mapping (`SQLAlchemy`)
In the second half of this project (`model_state.py`, `model_city.py`, and `7` through `14`), we switch to **SQLAlchemy**, the most popular Python ORM.
* **What is an ORM?** An ORM acts as a translator between Python and SQL. Instead of creating tables with `CREATE TABLE` and fetching rows with `SELECT`, you define a Python `class` (e.g., `class State`). Each attribute of the class represents a column, and each instance of the class represents a row in your database!
* **Pros:** Cleaner, safer code (automatically protects against SQL injection), and you don't have to switch your brain back and forth between Python and SQL syntax.

---

## 🛠️ Prerequisites & Setup

To run these scripts on your local machine, you will need:
* **Python 3** (3.8+)
* **MySQL Server** (running locally on `localhost`, port `3306`)
* **MySQLdb** (`mysqlclient`) and **SQLAlchemy** installed:

```bash
pip3 install mysqlclient SQLAlchemy
```

### How to Run the Scripts
Almost every script takes **3 standard command-line arguments** (plus an optional 4th argument for searching):
```bash
./<script_name>.py <mysql_username> <mysql_password> <database_name> [optional_search_argument]
```
*Example:*
```bash
./0-select_states.py root root hbtn_0e_0_usa
```

---

## 📂 Project Files Explained

### Part 1: Raw SQL with `MySQLdb`

* **`0-select_states.py`**
  * **What it does:** Connects to the database and lists all rows in the `states` table, sorted by `id` in ascending order.
  * **Beginner takeaway:** Learn the basic lifecycle of a database connection: `connect()` $\rightarrow$ `cursor()` $\rightarrow$ `execute()` $\rightarrow$ `fetchall()` $\rightarrow$ `close()`.

* **`1-filter_states.py`**
  * **What it does:** Lists all states whose names start with an uppercase **`N`**.
  * **Beginner takeaway:** Introduces SQL pattern matching (`LIKE BINARY 'N%'`) inside Python to ensure case-sensitive filtering.

* **`2-my_filter_states.py`**
  * **What it does:** Takes a 4th argument from the user (a state name) and displays all matching records using string formatting (`.format()`).
  * **Beginner takeaway:** Shows how to pass user input into a query—**and highlights a major security flaw** (SQL Injection) when using standard string formatting.

* **`3-my_safe_filter_states.py`**
  * **What it does:** Does the exact same thing as task `2`, but safely!
  * **Beginner takeaway:** Introduces **parameterized queries** (`%s` placeholders passed as a tuple to `execute()`). This ensures user input is treated strictly as text, not executable SQL commands.

* **`4-cities_by_state.py`**
  * **What it does:** Lists all cities alongside their corresponding state names, sorted by city `id`.
  * **Beginner takeaway:** Demonstrates how to use SQL `JOIN` statements inside Python to combine data from two different tables (`cities` and `states`) in a single query.

* **`5-filter_cities.py`**
  * **What it does:** Takes a state name as an argument and prints a comma-separated list of all cities belonging to that state.
  * **Beginner takeaway:** Combines safe parameterized queries with `JOIN` statements and Python list/string formatting (`", ".join(...)`).

---

### Part 2: Database Models with `SQLAlchemy`

* **`model_state.py`**
  * **What it does:** Defines the `State` class and creates the `Base` instance using `declarative_base()`.
  * **Beginner takeaway:** This is your blueprint! It maps the Python class `State` to the MySQL table `states`, defining `id` (primary key integer) and `name` (non-nullable string).

* **`model_city.py`**
  * **What it does:** Defines the `City` class, which maps to the `cities` table.
  * **Beginner takeaway:** Introduces **Foreign Keys** (`ForeignKey('states.id')`) in SQLAlchemy, linking every city to a valid state in the `states` table.

---

### Part 3: CRUD Operations with `SQLAlchemy`
*(CRUD stands for **C**reate, **R**ead, **U**pdate, and **D**elete—the four basic operations of persistent storage.)*

* **`7-model_state_fetch_all.py`** *(Read)*
  * **What it does:** Lists all `State` objects from the database using a SQLAlchemy `Session`.
  * **Beginner takeaway:** Replaces `SELECT * FROM states` with Pythonic syntax: `session.query(State).order_by(State.id).all()`.

* **`8-model_state_fetch_first.py`** *(Read)*
  * **What it does:** Fetches and prints only the very first `State` object (lowest `id`). If the table is empty, it prints `Nothing`.
  * **Beginner takeaway:** Using `.first()` instead of `.all()` is much more efficient when you only need a single record, as it stops searching after finding the first match.

* **`9-model_state_filter_a.py`** *(Read / Filter)*
  * **What it does:** Lists all `State` objects that contain the letter **`a`** in their name.
  * **Beginner takeaway:** Introduces SQLAlchemy's `.filter()` method combined with `.like('%a%')`.

* **`10-model_state_my_get.py`** *(Read / Search)*
  * **What it does:** Takes a state name as an argument and prints its `id` (or `Not found` if it doesn't exist).
  * **Beginner takeaway:** Shows how to safely filter by exact match (`State.name == sys.argv[4]`) without worrying about SQL injection.

* **`11-model_state_insert.py`** *(Create)*
  * **What it does:** Creates a new `State` object named `"Louisiana"`, adds it to the database, and prints its newly generated `id`.
  * **Beginner takeaway:** Learn the workflow for saving new data: instantiate the object $\rightarrow$ `session.add(new_state)` $\rightarrow$ `session.commit()`.

* **`12-model_state_update_id_2.py`** *(Update)*
  * **What it does:** Finds the state with `id = 2` and changes its name to `"New Mexico"`.
  * **Beginner takeaway:** Updating data in an ORM is as simple as changing a Python attribute (`state.name = "New Mexico"`) and calling `session.commit()`.

* **`13-model_state_delete_a.py`** *(Delete)*
  * **What it does:** Finds all states containing the letter **`a`** and deletes them from the database.
  * **Beginner takeaway:** Uses `session.delete(state)` followed by `session.commit()` to permanently remove records.

* **`14-model_city_fetch_by_state.py`** *(Read / Join)*
  * **What it does:** Prints all `City` objects grouped/formatted with their parent `State` name: `<state name>: (<city id>) <city name>`.
  * **Beginner takeaway:** Demonstrates how to query across two linked models (`session.query(City, State).join(State)`) using SQLAlchemy.

---

## 💡 Quick Cheat Sheet: Raw SQL vs. SQLAlchemy

| Action | Raw SQL (`MySQLdb`) | ORM (`SQLAlchemy`) |
| :--- | :--- | :--- |
| **Get all states** | `cur.execute("SELECT * FROM states")` | `session.query(State).all()` |
| **Filter states** | `cur.execute("SELECT * FROM states WHERE name LIKE '%a%'")` | `session.query(State).filter(State.name.like('%a%')).all()` |
| **Insert a state** | `cur.execute("INSERT INTO states (name) VALUES ('Louisiana')")` | `session.add(State(name='Louisiana')); session.commit()` |
| **Update a state** | `cur.execute("UPDATE states SET name='New Mexico' WHERE id=2")` | `state.name = 'New Mexico'; session.commit()` |
| **Delete a state** | `cur.execute("DELETE FROM states WHERE id=2")` | `session.delete(state); session.commit()` |
