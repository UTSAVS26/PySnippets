# Hashing and Its Algorithms

## Introduction
Hashing is a process of mapping large amounts of data to smaller fixed-size values, known as hash values or hash codes. Hashing is primarily used in data structures such as hash tables to allow for fast data retrieval. Hash functions take an input (or key) and return a fixed-size string of bytes. The result is typically a unique value that represents the input, ensuring efficient searching, indexing, and data retrieval.

Hashing algorithms are used extensively in various applications such as cryptography, database indexing, and caching mechanisms.

## Key Concepts

### 1. Hash Function
A **Hash Function** is a function that takes input data (such as strings, files, or numbers) and returns a fixed-size, typically a shorter representation of the data, called a **hash value**. This hash value is used to index data into a hash table.

- **Deterministic**: A hash function must always produce the same hash value for the same input.
- **Efficient**: The computation of the hash value should be fast.
- **Uniform distribution**: The hash values should be uniformly distributed to minimize collisions.

![Hash Function Diagram](https://media.geeksforgeeks.org/wp-content/uploads/20240508162701/Components-of-Hashing.webp)

### 2. Hash Table
A **Hash Table** is a data structure that stores key-value pairs. The key is processed by a hash function, and its output determines where the value is stored in the table. Hash tables allow for average-case constant time complexity, O(1), for lookup, insertion, and deletion operations.

![Hash Table Structure](https://www.tutorialspoint.com/data_structures_algorithms/images/hash_function.jpg) 

### 3. Collisions and Collision Resolution
In practice, different inputs might produce the same hash value; this is known as a **collision**. A good hashing algorithm minimizes collisions, but when they occur, they are handled using **collision resolution techniques**:

- **Chaining**: Each slot of the hash table contains a linked list or another structure where all elements with the same hash are stored.
- **Open Addressing**: If a collision occurs, the algorithm looks for the next available slot. Different probing techniques are used:
  - **Linear Probing**: Finds the next open slot by moving sequentially.
  - **Quadratic Probing**: Searches for an empty slot with increasing intervals (e.g., 1, 4, 9).
  - **Double Hashing**: Uses a second hash function to calculate the next available slot.

![Collision Resolution Techniques](https://www.gatevidyalay.com/wp-content/uploads/2018/06/Collision-Resolution-Techniques-1.png) 

### 4. Load Factor
The **Load Factor** is defined as the ratio of the number of elements stored in the hash table to the total number of slots. A high load factor increases the chance of collisions.

- **Formula**: Load Factor = \( \frac{n}{m} \), where `n` is the number of elements, and `m` is the number of slots in the hash table.

### 5. Common Hashing Algorithms

- **Modulo Hashing**: Uses the remainder of a division to compute the hash value. 
  - Formula: `hash(x) = x % n`
  
- **Multiplicative Hashing**: Uses a constant multiplier and modulus to compute the hash.
  - Formula: `hash(x) = ((A * x) % 1) * m`, where `A` is a constant and `m` is the table size.
  
- **Cryptographic Hashing (e.g., SHA-256)**: Designed to produce a fixed output that is difficult to reverse engineer. These are used in cryptographic applications.

## Applications of Hashing
- **Hash Maps/Hash Tables**: Efficient key-value data storage.
- **Cryptography**: Hashing is fundamental in generating secure digital signatures and ensuring data integrity.
- **Database Indexing**: Hashing helps speed up the search process in databases.
- **Load Balancing**: Distributing traffic across multiple servers based on hashed values.
- **Caching**: Hashing is used to quickly access stored data.

## Hashing Algorithm Questions

1. **Question**: Write a function to compute the hash value of a string using the simple modulo method.
   
   **Code**:
   ```python
   def string_hash(s, table_size):
       hash_value = 0
       for char in s:
           hash_value += ord(char)
       return hash_value % table_size

   # Example usage
   print(string_hash("example", 10))  # Output: hash value
   ```

2. **Question**: Implement a function that checks for collisions in a list of keys using a given hash function.
   
   **Code**:
   ```python
    def check_collisions(keys, table_size):
        hash_table = {}
        collisions = []

        for key in keys:
            hash_key = key % table_size
            if hash_key in hash_table:
                collisions.append(key)
            else:
                hash_table[hash_key] = key

        return collisions

    # Example usage
    print(check_collisions([1, 2, 12, 22, 32], 10))  # Output: [12, 22]
   ```

