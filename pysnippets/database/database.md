## Overview
This documentation provides a guide to using the SQL and MongoDB database snippets available in the **PySnippets** package. These snippets cover essential operations for interacting with both **SQL-based** and **NoSQL-based** databases. The documentation includes examples for connection management, data manipulation, schema creation, and index management for both **SQL** and **MongoDB** databases.

## Table of Contents
- [SQL Database Snippets](#sql-database-snippets)
  - [SQL Connection Manager](#sql-connection-manager)
  - [Execute SQL Query](#execute-sql-query)
  - [Bulk Data Insertion](#bulk-data-insertion)
  - [Transaction Handling](#transaction-handling)
  - [SQL Schema Creation](#sql-schema-creation)
- [MongoDB Database Snippets](#mongodb-database-snippets)
  - [MongoDB Connection Manager](#mongodb-connection-manager)
  - [Insert Document](#insert-document)
  - [Query Documents](#query-documents)
  - [Update Document](#update-document)
  - [Manage MongoDB Indexes](#manage-mongodb-indexes)

---

## SQL Database Snippets

### 1. **SQL Connection Manager**
This snippet allows you to connect to a MySQL or PostgreSQL database.

**Function**:
- `connect_to_mysql(host, user, password, database)`: Connect to a MySQL database.
- `connect_to_postgresql(host, user, password, database)`: Connect to a PostgreSQL database.

**Parameters**:
- `host` (str): Database server address.
- `user` (str): Database username.
- `password` (str): Database user password.
- `database` (str): Name of the database to connect to.

**Example**:
```python
connection = connect_to_mysql('localhost', 'root', 'password', 'mydb')
# Use the connection
connection.close()
```

---

### 2. **Execute SQL Query**
This snippet allows you to execute basic SQL queries like `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.

**Function**:
- `execute_query(connection, query, params=None)`: Executes an SQL query.

**Parameters**:
- `connection`: The database connection object.
- `query` (str): SQL query to execute.
- `params` (tuple, optional): Parameters for the query.

**Example**:
```python
result = execute_query(connection, 'SELECT * FROM users WHERE id = %s', (1,))
print(result)
```

---

### 3. **Bulk Data Insertion**
Insert multiple rows into an SQL table using this snippet.

**Function**:
- `bulk_insert(connection, table, data)`: Bulk inserts data into a table.

**Parameters**:
- `connection`: The database connection object.
- `table` (str): Name of the table.
- `data` (list of tuple): List of tuples representing the rows.

**Example**:
```python
data = [(1, 'Alice'), (2, 'Bob')]
bulk_insert(connection, 'users', data)
```

---

### 4. **Transaction Handling**
Execute multiple queries in a transaction with support for commit and rollback.

**Function**:
- `execute_transaction(connection, queries)`: Executes multiple queries in a transaction.

**Parameters**:
- `connection`: The database connection object.
- `queries` (list): List of SQL queries to execute.

**Example**:
```python
queries = [
    "INSERT INTO users (id, name) VALUES (3, 'Charlie')",
    "UPDATE users SET name = 'Alice Updated' WHERE id = 1"
]
execute_transaction(connection, queries)
```

---

### 5. **SQL Schema Creation**
Create tables, indexes, or relationships using this snippet.

**Function**:
- `create_table(connection, create_table_query)`: Creates a table with the provided SQL query.

**Parameters**:
- `connection`: The database connection object.
- `create_table_query` (str): SQL query to create a table.

**Example**:
```python
query = """
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100)
)
"""
create_table(connection, query)
```

---

## MongoDB Database Snippets

### 1. **MongoDB Connection Manager**
This snippet allows you to connect to a MongoDB instance using a connection URI.

**Function**:
- `connect_to_mongodb(uri)`: Connects to a MongoDB instance.

**Parameters**:
- `uri` (str): MongoDB connection URI.

**Example**:
```python
client = connect_to_mongodb("mongodb://localhost:27017")
db = client.my_database
```

---

### 2. **Insert Document**
Insert a document into a MongoDB collection.

**Function**:
- `insert_document(collection, document)`: Inserts a document into a collection.

**Parameters**:
- `collection`: MongoDB collection object.
- `document` (dict): Document to insert.

**Example**:
```python
doc = {'name': 'Alice', 'age': 30}
insert_document(db.users, doc)
```

---

### 3. **Query Documents**
Query documents from a MongoDB collection with optional filters and projections.

**Function**:
- `query_documents(collection, filter_criteria=None, projection=None)`: Queries documents based on filters.

**Parameters**:
- `collection`: MongoDB collection object.
- `filter_criteria` (dict, optional): Query filters.
- `projection` (dict, optional): Fields to include or exclude.

**Example**:
```python
results = query_documents(db.users, {'age': {'$gt': 25}}, {'name': 1})
for doc in results:
    print(doc)
```

---

### 4. **Update Document**
Update a document or multiple documents in a MongoDB collection.

**Function**:
- `update_document(collection, filter_criteria, update_data, multiple=False)`: Updates one or more documents.

**Parameters**:
- `collection`: MongoDB collection object.
- `filter_criteria` (dict): Query filters to match documents.
- `update_data` (dict): Update data.
- `multiple` (bool, optional): Whether to update multiple documents.

**Example**:
```python
update_document(db.users, {'name': 'Alice'}, {'age': 31})
```

---

### 5. **Manage MongoDB Indexes**
Create and drop indexes in MongoDB collections.

**Functions**:
- `create_index(collection, field, unique=False)`: Creates an index on a field.
- `drop_index(collection, index_name)`: Drops a specific index.

**Parameters**:
- `collection`: MongoDB collection object.
- `field` (str): Field to index.
- `unique` (bool, optional): Whether the index is unique.
- `index_name` (str): Name of the index to drop.

**Example**:
```python
index_name = create_index(db.users, 'name', unique=True)
drop_index(db.users, index_name)
```

