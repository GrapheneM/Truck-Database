Truck Database

A lightweight, experimental file-based database implemented in Python.

Truck Database explores how a simple database system can be designed using the local filesystem and JSON for persistent storage. It provides a hierarchical Trunk → Branch architecture along with database operations, password-based access, logging, and custom error handling.

Features

Hierarchical Trunk and Branch architecture

Persistent file-based storage

JSON-based data storage

Create, read, update, and delete operations

Password-protected database resources

Branch password management

Branch renaming and deletion

Basic operation logging

Custom exception handling

Python-based database API

Architecture

Truck Database organizes data into Trunks and Branches:

Trunk
├── Branch
│   ├── INFO.json
│   ├── DATA.json
│   └── LOG.txt
│
├── Branch
│   ├── INFO.json
│   ├── DATA.json
│   └── LOG.txt
│
└── Branch
    ├── INFO.json
    ├── DATA.json
    └── LOG.txt


A Trunk acts as a container for multiple Branches, while a Branch represents an individual data store.

Project Structure
Truck-Database/
├── Trunks/
├── database.py
├── helper.py
├── customErrors.py
├── Testing.py
└── waste.py

Core Modules
File	Description
database.py	Main database and Trunk/Branch implementation
helper.py	File and JSON handling utilities
customErrors.py	Custom exceptions used by the database
Testing.py	Examples and testing of database functionality
waste.py	Experimental code
Installation

Clone the repository:

git clone https://github.com/GrapheneM/Truck-Database.git
cd Truck-Database


Install the required dependency:

pip install pympler

Basic Usage
Import
from database import Database

Create a Trunk
Database.createTrunk(
    name="main",
    password="password123"
)

Connect to a Trunk
main = Database.connectTrunk(
    name="main",
    password="password123"
)

Create a Branch
main.createBranch("users")

Connect to a Branch
users = main.connectBranch(
    name="users",
    password="password123"
)

Write Data
users.write(
    {
        "name": "Alice",
        "age": 21
    },
    "password123"
)

Read Data
data = users.read("password123")

print(data)

Append Data
users.append(
    {
        "city": "Delhi"
    },
    "password123"
)

Get a Value
name = users.getValue(
    "name",
    "password123"
)

print(name)

Delete a Key
users.deleteKey(
    "age",
    "password123"
)

List Trunks
trunks = Database.listTrunks()

print(trunks)

List Branches
branches = main.listBranches()

print(branches)

Complete Example
from database import Database

# Create a Trunk
Database.createTrunk("main", "password123")

# Connect to the Trunk
main = Database.connectTrunk(
    "main",
    "password123"
)

# Create a Branch
main.createBranch("users")

# Connect to the Branch
users = main.connectBranch(
    "users",
    "password123"
)

# Write data
users.write(
    {
        "name": "Alice",
        "age": 21
    },
    "password123"
)

# Append data
users.append(
    {
        "city": "Delhi"
    },
    "password123"
)

# Read data
print(users.read("password123"))

# Retrieve a specific value
print(users.getValue("name", "password123"))

Storage

Data is persisted directly to the filesystem.

A typical database structure looks like:

Trunks/
└── main1/
    ├── INFO.json
    └── users/
        ├── INFO.json
        ├── DATA.json
        └── LOG.txt


The use of JSON makes the stored data human-readable and easy to inspect during development.

Error Handling

The project includes custom exceptions for handling database-related errors.

These are defined in:

customErrors.py


This allows database operations to communicate specific failure conditions instead of relying only on generic Python exceptions.

Security

The current implementation uses password-based access control for Trunks and Branches.

This project is experimental, and its authentication mechanism should not be considered suitable for production security.

For production use, passwords should be securely hashed rather than stored as plain text. Additional security measures such as access control, file permissions, and secure key management would also be required.

Limitations

Truck Database is designed as an experimental and educational project rather than a replacement for production database systems.

Current limitations include:

File-based storage

JSON-based data representation

No SQL query engine

No transaction system

No database indexing

Limited concurrency support

No schema enforcement

Not designed for high-volume workloads

Not designed for multi-user production environments

For larger applications, established database systems such as PostgreSQL, MySQL, or SQLite are more appropriate.

Project Goals

The primary goal of this project is to explore the fundamentals behind database systems and persistent storage without relying on an external database server.

The project focuses on:

Data persistence

Storage abstraction

CRUD operations

File management

Authentication concepts

Error handling

API design

Database organization

Testing

The repository includes Testing.py, which can be used to experiment with the database and its operations.

Run:

python Testing.py

Future Improvements

Potential improvements include:

Password hashing

Atomic file writes

File locking and concurrency support

Transaction support

Query and filtering operations

Indexing

Schema validation

Automated unit tests

Performance benchmarks

Type hints

Package distribution through PyPI

Continuous integration with GitHub Actions

Project Status

Experimental

Truck Database is currently a learning and experimentation project focused on implementing a simple database-like storage system using Python, JSON, and the local filesystem.

Author

GrapheneM

GitHub: https://github.com/GrapheneM