# Python Serialization

📚 Project Overview

Welcome to the Python Serialization project!

In this project, you will learn how to save Python data so that it can be stored in a file, shared with another program, or loaded again later.

You will explore four different ways of working with data:

JSON – Saving and loading Python data using JSON.

Pickle – Saving and loading Python objects, including custom classes.

CSV – Reading spreadsheet-style data and converting it into JSON.

XML – Saving and loading data using XML markup.

---

🗂️ Project Structure

Your directory contains the following files:
```
python_serialization/
├── task_00_basic_serialization.py
├── task_01_pickle.py
├── task_02_csv.py
├── task_03_xml.py
└── README.md
```

Each Python file demonstrates a different approach to storing or converting data.

---

## 1. What Is Serialization?

Serialization is the process of converting data into a format that can be saved or transferred.

For example, imagine you have a Python dictionary:

```py
student = {
    "name": "Alex",
    "age": 21,
    "is_student": True
}
```

This dictionary exists in your program's memory. If you want to save it to a file and use it again tomorrow, you need to store it in a suitable format.

Serialization converts the data into a storable representation.

Deserialization is the opposite process. It takes the stored representation and converts it back into a Python object.

The basic process
```
Python object
     |
     | Serialization
     v
File or stored data
     |
     | Deserialization
     v
Python object again
```

Why is serialization useful?

Serialization can help you:

- Save user settings between program runs.

- Store information about students, products, or customers.

- Exchange data between different applications.

- Save objects for later use.

- Convert spreadsheet data into a format that another program can read.

# 2. Task 00 — Basic JSON Serialization

File: task_00_basic_serialization.py

What is JSON?

JSON stands for JavaScript Object Notation. Despite its name, Python supports JSON directly through its built-in json module.

JSON is a common format for storing and exchanging structured data.

For example, this is valid JSON:
```
{
    "name": "Alex",
    "age": 21,
    "is_student": true
}
```

Notice that JSON uses true rather than Python's True.

Understanding the code

Your file contains two functions:

- serialize_and_save_to_file(data, filename)

- load_and_deserialize(filename)

Function 1: serialize_and_save_to_file()
```py
def serialize_and_save_to_file(data, filename):
    """Serialize a Python object and save it to a JSON file."""
    with open(filename, "w", encoding="utf-8") as JFILE:
        json.dump(data, JFILE)
```

Let's break this down.

Step 1: Receive the data and filename
```py
def serialize_and_save_to_file(data, filename):
```
- data is the Python object you want to save.

- filename is the name of the file where you want to save it.

Step 2: Open the file
```py
with open(filename, "w", encoding="utf-8") as JFILE:
```
- open() opens a file.

- "w" means write mode. It creates the file if it does not exist and overwrites it if it already exists.

- encoding="utf-8" specifies how text is encoded.

- with automatically closes the file when the block finishes.

- JFILE is the variable used to access the open file.

Step 3: Convert and save the data
```py
json.dump(data, JFILE)
```
json.dump() converts the Python object into JSON and writes it directly into the file.

Function 2: load_and_deserialize()
```py
def load_and_deserialize(filename):
    """Load JSON data from a file and deserialize it into a Python object."""
    with open(filename, "r", encoding="utf-8") as JFILE:
        return json.load(JFILE)
```

This function does the reverse.

- "r" opens the file in read mode.

- json.load(JFILE) reads JSON from the file and converts it into a Python object.

- return sends that object back to the code that called the function.

Example: Saving and loading a dictionary

Create a separate test file called test_json.py:
```py
from task_00_basic_serialization import (
    serialize_and_save_to_file,
    load_and_deserialize
)

student = {
    "name": "Alex",
    "age": 21,
    "is_student": True
}

serialize_and_save_to_file(student, "student.json")

loaded_student = load_and_deserialize("student.json")

print(loaded_student)
print(loaded_student["name"])
```

Run it:
```bash
python3 test_json.py
```

Expected output:
```
{'name': 'Alex', 'age': 21, 'is_student': True}
Alex
```
Your program creates a student.json file containing the serialized data.

Important JSON concepts

|Python |JSON   |
|---    |___    |
|dict   |Object |
|list   |Array  |
|str    |String |
|int    |Number |
|float  |Number |
|True   |true   |
|False  |false  |
|None   |null   |

Not every Python object can be serialized directly with JSON. For example, a custom class instance usually needs to be converted into a supported structure first.

---

Practice exercise

Try the following without copying the example above:

Create a dictionary containing a book's title, author, and publication year.

Save the dictionary to book.json.

Load it back into Python.

Print the title and publication year.

Challenge: Add a list of three favourite books to your dictionary and save it as JSON.

---

## 3. Task 01 — Serialization with Pickle

File: task_01_pickle.py

What is Pickle?

Python's pickle module can serialize many Python objects, including instances of custom classes.

Unlike JSON, Pickle is designed specifically for Python objects.

Your file defines a class called CustomObject and provides methods to display, serialize, and deserialize an instance.

Understanding serialize()

```py
def serialize(self, filename):
    try:
        with open(filename, "wb") as file:
            pickle.dump(self, file)
    except (OSError, pickle.PickleError, TypeError, AttributeError):
        return None
```

This method saves the current object to a file.

- "wb" means write binary mode.
- Pickle stores the object in a binary representation.
- pickle.dump(self, file) serializes the current object and writes it to the file.
- try lets the program attempt an operation that might fail.
- except catches the listed errors.
- If one of those errors occurs, the method returns None.

The method does not explicitly return a value when successful, so it returns None in that case too. The main difference is that a file should have been written successfully.

Understanding deserialize()
```py
@classmethod
def deserialize(cls, filename):
    try:
        with open(filename, "rb") as file:
            obj = pickle.load(file)

        if not isinstance(obj, cls):
            return None

        return obj

    except (
        OSError,
        pickle.PickleError,
        EOFError,
        TypeError,
        AttributeError,
        ImportError,
        ValueError
    ):
        return None
```

This method loads a previously saved object.

Important concepts:

- @classmethod allows the method to receive the class itself as cls.
- "rb" means read binary mode.
- pickle.load(file) reads and reconstructs the saved object.
- isinstance(obj, cls) checks whether the loaded object is an instance of the expected class.
- return obj gives the reconstructed object back to the caller.
- If a listed error occurs, the method returns None.

Example: Saving and loading a custom object

```py
Create test_pickle.py:

from task_01_pickle import CustomObject

student = CustomObject("Alex", 21, True)

# Save the object
student.serialize("student.pkl")

# Load the object
loaded_student = CustomObject.deserialize("student.pkl")

# Display the loaded object
if loaded_student is not None:
    loaded_student.display()
else:
    print("Could not load the object.")
```

Run it:
```bash
python3 test_pickle.py
```
Expected output:
```
Name: Alex
Age: 21
Is Student: True
```
The .pkl extension is a common naming convention for Pickle files.

JSON vs Pickle

|Feature                                |JSON               |Pickle                     |
|---                                    |---                |---                        |
|Human-readable file                    |Usually            |Usually not                |
|Works well with other languages        |Yes                |Generally Python-specific  |
|Saves basic dictionaries and lists     |Yes                |Yes                        |
|Saves custom Python objects directly   |Usually not        |Often yes                  |
|Safe to load from an untrusted source  |Generally, as data |No                         |

Security warning: Never load Pickle files from an untrusted source. Deserializing a malicious Pickle file can execute code.

## 4. Task 02 — Converting CSV to JSON

File: task_02_csv.py

What is CSV?

CSV stands for Comma-Separated Values.

It is a text format often used by spreadsheets and databases.

Example CSV file:
```
name,age,course
Alex,21,Python
Sam,24,Java
Jordan,19,C
```
The first row contains the column names. Each following row contains a record.

Your program reads this CSV data and converts it into JSON.

Understanding the imports
```
import csv
import json
```
csv provides tools for reading and writing CSV files.

json provides tools for converting Python data to and from JSON.

Both are included in Python's standard library.

Understanding convert_csv_to_json()
```py
def convert_csv_to_json(csv_filename):
    """Convert and save to json file"""
    try:
        data = []

        with open(csv_filename, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                data.append(row)

        with open("data.json", mode="w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True

    except (OSError, csv.Error, TypeError, ValueError):
        return False
```

Let's break it down.

Step 1: Create an empty list
```
data = []
```
This list will hold the rows from the CSV file.

Step 2: Open the CSV file
```py
with open(csv_filename, mode="r", encoding="utf-8") as csvfile:
```
The filename is provided when the function is called.

Step 3: Read the rows
```py
reader = csv.DictReader(csvfile)
```
csv.DictReader uses the first row as the column names and represents each subsequent row as a dictionary.

For example:
```
{
    "name": "Alex",
    "age": "21",
    "course": "Python"
}
```
Notice that "21" is a string, not an integer. CSV files store text, so the reader does not automatically convert numeric-looking values into numbers.

Step 4: Add each row to the list
```py
for row in reader:
    data.append(row)
```
The loop reads each row and adds its dictionary to data.

After reading the example CSV, data will look like this:
```
[
    {"name": "Alex", "age": "21", "course": "Python"},
    {"name": "Sam", "age": "24", "course": "Java"},
    {"name": "Jordan", "age": "19", "course": "C"}
]
```
Step 5: Save the data as JSON
```py
with open("data.json", mode="w", encoding="utf-8") as jsonfile:
    json.dump(data, jsonfile, indent=4)
```
This writes the list of dictionaries to data.json.

The indent=4 argument makes the JSON easier for humans to read.

Step 6: Return the result
```py
return True
```
The function returns True if the conversion completes.

If one of the listed exceptions occurs, it returns False.

Example: Converting a CSV file

Create a file called students.csv:
```
name,age,course
Alex,21,Python
Sam,24,Java
Jordan,19,C
```
Then create test_csv.py:
```py
from task_02_csv import convert_csv_to_json

result = convert_csv_to_json("students.csv")

if result:
    print("Conversion successful!")
else:
    print("Conversion failed.")
```
Run it:
```bash
python3 test_csv.py
```
Expected output:
```
Conversion successful!
```
Your program creates data.json in the current working directory.

Its contents will look like this:
```
[
    {
        "name": "Alex",
        "age": "21",
        "course": "Python"
    },
    {
        "name": "Sam",
        "age": "24",
        "course": "Java"
    },
    {
        "name": "Jordan",
        "age": "19",
        "course": "C"
    }
]
```
Understanding the file conversion
```
students.csv
     |
     | csv.DictReader()
     v
List of dictionaries
     |
     | json.dump()
     v
data.json
```
## 5. Task 03 — Serialization and Deserialization with XML

File: task_03_xml.py

What is XML?

XML stands for Extensible Markup Language.

It stores data using tags, similar to the way HTML uses tags to structure web pages.

Example XML:
```
<?xml version='1.0' encoding='utf-8'?>
<data>
    <name>Alex</name>
    <age>21</age>
    <course>Python</course>
</data>
```
Here:

- <data> is the root element.
- <name>, <age>, and <course> are child elements.
- The text between a pair of tags is the element's value.

Unlike JSON, XML uses opening and closing tags to organise the data.

Understanding the import
```py
import xml.etree.ElementTree as ET
```
ElementTree is a built-in Python module for creating, reading, and manipulating XML.

ET is a shorter alias for the module name.

Function 1: serialize_to_xml()
```py
def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
```

This function converts a dictionary into an XML file.

Step 1: Create the root element
```py
root = ET.Element("data")
```
This creates the main <data> element that will contain the other elements.

Step 2: Loop through the dictionary
```py
for key, value in dictionary.items():
```
.items() allows you to access each key and its corresponding value.

For this dictionary:
```py
student = {
    "name": "Alex",
    "age": 21,
    "course": "Python"
}
```
The loop processes each pair:
```
name   -> Alex
age    -> 21
course -> Python
```

Step 3: Create child elements
```py
child = ET.SubElement(root, key)
```
This creates a child element under the root.

For example, when key is "name", Python creates a <name> element.

Step 4: Store the value as text
```py
child.text = str(value)
```
XML element text is stored as a string, so str(value) converts values such as the integer 21 into "21".

Step 5: Write the XML file
```py
tree = ET.ElementTree(root)
tree.write(filename, encoding="utf-8", xml_declaration=True)
```
- ET.ElementTree(root) creates a tree representing the XML structure.
- tree.write() saves the XML to the requested filename.
- xml_declaration=True includes the XML declaration at the top of the file.

Function 2: deserialize_from_xml()
```py
def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data = {}

        for child in root:
            data[child.tag] = child.text

        return data

    except (OSError, ET.ParseError):
        return None
```

This function reads an XML file and converts its child elements into a Python dictionary.

Step 1: Parse the XML file
```
tree = ET.parse(filename)
```
This reads the file and builds a tree structure from the XML.

Step 2: Get the root
```
root = tree.getroot()
```
This retrieves the root element, which in your example is <data>.

Step 3: Create an empty dictionary
```
data = {}
```
The dictionary will store the element names and their text values.

Step 4: Read each child element
```py
for child in root:
    data[child.tag] = child.text
```
- child.tag gives the element's name.
- child.text gives its text value.

Step 5: Return the dictionary
```
return data
```
If the file cannot be opened or contains invalid XML, the function returns None.

Example: Saving and loading XML

Create test_xml.py:
```py
from task_03_xml import serialize_to_xml, deserialize_from_xml

student = {
    "name": "Alex",
    "age": 21,
    "course": "Python"
}

# Save the dictionary as XML
serialize_to_xml(student, "student.xml")

# Load the XML back into Python
loaded_student = deserialize_from_xml("student.xml")

print(loaded_student)
```

Run it:
```bash
python3 test_xml.py
```
Expected output:
```
{'name': 'Alex', 'age': '21', 'course': 'Python'}
```
Important: The age is now a string. Your XML deserialization function retrieves element text but does not convert numeric strings back into integers.

## 6. Comparing the Four Approaches

|Method |Main purpose                       |Common file extension  |
|---    |---|---                            |---                    |
|JSON   |Save and load structured data      |.json                  |
|Pickle |Save and load Python objects       |.pkl                   |
|CSV    |Store tabular data                 |.csv                   |
|XML    |Store structured data using tags   |.xml                   |

Which one should you use?

Use JSON when you want a readable format for settings, dictionaries, lists, or API data.

Use Pickle when you need to save Python objects and control both the saving and loading environment. Never load untrusted Pickle files.

Use CSV when working with rows and columns, especially when exchanging data with spreadsheets.

Use XML when you need a tag-based format, such as when working with systems that expect XML documents.

JSON and XML are both text-based formats. Pickle uses a Python-specific serialized representation, while CSV is primarily intended for tabular data.


