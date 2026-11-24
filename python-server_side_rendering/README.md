# 🌐 Python Server-Side Rendering (SSR) — Beginner's Guide

Welcome! This project is an introduction to **Server-Side Rendering (SSR)** using **Python**, **Flask**, **Jinja2**, and **SQLite**.

If you are new to web development, think of a website like a restaurant:

* **The Browser (You):** The customer sitting at the table asking for a webpage.
* **The Server (Python & Flask):** The kitchen that receives your order, gathers the ingredients, and puts the meal together.
* **The Data (`.json`, `.csv`, `.db`):** The pantry (and walk-in fridge!) where raw information like product names, categories, and prices is stored.
* **The Templates (`.html`):** The empty plates with a specific layout waiting to be filled with data before being served to you.

---

## 📁 Project Structure

Here is how the files in this directory are organized and how they build upon each other:

```text
python-server_side_rendering/
│
├── task_00_intro.py       # Pure Python: Generates text invitations from a template
├── task_01_jinja.py       # Flask Basics: Serves static HTML pages using Jinja templates
├── task_02_logic.py       # Dynamic Logic: Reads JSON data and uses loops/if-statements in HTML
├── task_03_files.py       # File Handling: Reads data from either JSON or CSV based on URL parameters
├── task_04_db.py          # Database Integration: Adds SQLite database support alongside JSON and CSV
│
├── items.json             # Sample data list for Task 02
├── products.json          # Product catalog in JSON format (Tasks 03 & 04)
├── products.csv           # Product catalog in CSV format (Tasks 03 & 04)
├── products.db            # SQLite database file (created/queried in Task 04)
│
└── templates/             # Folder containing all HTML blueprints
    ├── header.html        # Reusable top navigation bar
    ├── footer.html        # Reusable bottom footer
    ├── index.html         # Home page
    ├── about.html         # About page
    ├── contact.html       # Contact page
    ├── items.html         # Page displaying a list of items (Task 02)
    └── product_display.html # Table displaying products from JSON, CSV, or SQLite (Tasks 03 & 04)
```

---

## 🔄 How Everything Talks to Each Other

Instead of sending an empty webpage to your browser and making your computer fetch the data separately, **Server-Side Rendering** builds the complete HTML page on the server first.

### The Full Request-to-Response Flow (Including the Database)

Here is the step-by-step conversation that happens when you visit a URL like `/products?source=sql&id=1`:

```text
[1. User's Browser] 
       │  Requests URL: http://127.0.0.1:5000/products?source=sql&id=1
       ▼
[2. Flask App (task_04_db.py)]
       │  Reads URL parameters:
       │   • source = "sql"  (Where should I look?)
       │   • id = "1"        (Do I need to filter for a specific item?)
       ▼
[3. Data Layer — Python picks ONE source based on "source="]
       ├── If source=json ──► Opens products.json (using Python's json module)
       ├── If source=csv  ──► Opens products.csv  (using Python's csv module)
       └── If source=sql  ──► Connects to products.db (using Python's sqlite3 module)
       │                        Runs: SELECT id, name, category, price FROM Products
       ▼
[4. Data Standardization (Python List of Dictionaries)]
       │  No matter where the data came from, Python converts it into the exact same format:
       │  [{'id': 1, 'name': 'Laptop', 'category': 'Electronics', 'price': 799.99}]
       ▼
[5. Jinja2 Template Engine (product_display.html)]
       │  Injects the Python data into HTML <table> rows (<tr><td>Laptop</td>...</tr>)
       │  Also pulls in header.html and footer.html
       ▼
[6. User's Browser]
          Receives a finished, ready-to-read HTML webpage!
```

---

## 🧩 File-by-File Breakdown

### 1. `task_00_intro.py` — Automated Mail Merge (No Web Server Yet)
* **What it does:** Before jumping into web servers, this script teaches the core concept of templating. It takes a text template containing placeholders like `{name}` and `{event_title}`, loops through a list of guest dictionaries, and generates personalized `.txt` files (`output_1.txt`, `output_2.txt`, etc.).
* **How it links:** Pure Python script $\rightarrow$ fills in missing values with `"N/A"` $\rightarrow$ writes new text files directly to your folder.

### 2. `task_01_jinja.py` — Your First Flask Web Server
* **What it does:** Sets up a basic web server using **Flask** and defines routes (URLs) like `/`, `/about`, and `/contact`.
* **How it links:**
  * When you visit `/about`, Flask calls `render_template('about.html')`.
  * Inside `about.html`, Jinja uses `{% include 'header.html' %}` and `{% include 'footer.html' %}` so you don't have to copy-paste your navigation bar onto every page.

### 3. `task_02_logic.py` & `items.json` — Adding Smart Templates
* **What it does:** Introduces dynamic content. Instead of hardcoding text into HTML, this script reads a list of items from `items.json` and passes it to `items.html`.
* **How it links:**
  * `task_02_logic.py` opens `items.json` and extracts the list of items.
  * It hands that list to `items.html`.
  * Inside `items.html`, Jinja uses a `{% for item in items %}` loop to automatically create an `<li>` bullet point for every item, or an `{% if %}` check to display *"No items found"* if the list is empty.

### 4. `task_03_files.py`, `products.json`, & `products.csv` — Switching File Sources
* **What it does:** Teaches the server how to read user choices from the URL (query parameters) and parse different flat-file formats.
* **How it links:**
  * You visit `/products?source=json` or `/products?source=csv` (with an optional `&id=...` filter).
  * Flask checks `request.args.get('source')` and `request.args.get('id')`.
  * Depending on your choice, Python reads either `products.json` or `products.csv` and converts the rows into a uniform list of dictionaries.
  * It sends that standardized data to `product_display.html` to build an HTML `<table>`. If you type an invalid source (like `?source=xml`), it sends `"Wrong source"` to the template instead.

### 5. `task_04_db.py` & `products.db` — Connecting a Real SQLite Database
* **What it does:** Upgrades Task 03 by adding **SQLite** database support (`?source=sql`) alongside JSON and CSV.
* **How the Database Works:**
  * Instead of reading a plain text file line-by-line, `task_04_db.py` uses Python's built-in `sqlite3` library to open a connection to `products.db`.
  * Inside `products.db`, there is a `Products` table with columns for `id`, `name`, `category`, and `price`.
  * Python creates a **cursor** (a database messenger), runs a SQL command (`SELECT * FROM Products`), fetches the matching rows, and turns each row into a Python dictionary.
* **Why This Architecture is So Useful:**
  * Look at `product_display.html`: **you didn't have to change your HTML template at all when adding the database!**
  * Because `task_04_db.py` formats SQLite rows into the exact same dictionary structure as `products.json` and `products.csv`, the HTML template doesn't care where the data came from—it just renders the table.

---

## 🛠️ Setting Up & Running the Project

### 1. Install Flask
If you haven't installed Flask yet, run:
```bash
pip install Flask
```

### 2. Create / Verify the SQLite Database (`products.db`)
If `products.db` isn't already generated in your folder, you can create and populate it using Python's built-in `sqlite3` module:
```python
import sqlite3

conn = sqlite3.connect('products.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL
    )
''')

cursor.execute('''
    INSERT OR IGNORE INTO Products (id, name, category, price)
    VALUES
    (1, 'Laptop', 'Electronics', 799.99),
    (2, 'Coffee Mug', 'Home Goods', 15.99)
''')

conn.commit()
conn.close()
```

### 3. Start the Server (Task 04)
Run the database-enabled Flask application:
```bash
python3 task_04_db.py
```

### 4. Test the Endpoints in Your Browser
Once the server is running on `http://127.0.0.1:5000`, try visiting these URLs to see the different data sources in action:

* **Home Page:** `http://127.0.0.1:5000/`
* **Read from JSON:** `http://127.0.0.1:5000/products?source=json`
* **Read from CSV:** `http://127.0.0.1:5000/products?source=csv`
* **Read from SQLite Database:** `http://127.0.0.1:5000/products?source=sql`
* **Filter Database by Product ID:** `http://127.0.0.1:5000/products?source=sql&id=1`
* **Test Error Handling (Invalid Source):** `http://127.0.0.1:5000/products?source=invalid`
