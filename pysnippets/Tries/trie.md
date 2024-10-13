
# Tries Module - PySnippets

Welcome to the **Tries** module! This utility provides functionality to manage a collection of strings efficiently through a trie data structure, allowing for fast retrieval, insertion, and deletion of strings.

## Table of Contents

- [Introduction](#introduction)
- [Functionality](#functionality)
  - [Insert a Word](#insert-a-word)
  - [Search for a Word](#search-for-a-word)
  - [Delete a Word](#delete-a-word)
  - [Insert a List of Words](#insert-a-list-of-words)
  - [Starts With](#starts-with)
- [Usage Example](#usage-example)

---

## Introduction

The **Tries** module implements a trie data structure, which is a tree-like structure used to store a dynamic set of strings. It enables efficient retrieval, insertion, and deletion of words. This is particularly useful in applications such as autocomplete systems, spell checkers, and IP routing.

---

## Functionality

### Insert a Word

This method inserts a single word into the trie.

```python
trie.insert(word)
```

- **Args**: 
  - `word` (str): The word to insert into the trie.
  
- **Returns**: 
  - `None`
  
- **Example**:
  ```python
  trie = Trie()
  trie.insert("apple")
  ```

### Search for a Word

This method checks if a word exists in the trie.

```python
trie.search(word)
```

- **Args**: 
  - `word` (str): The word to search for in the trie.
  
- **Returns**: 
  - `bool`: `True` if the word exists, `False` otherwise.
  
- **Example**:
  ```python
  exists = trie.search("apple")  # returns True if "apple" is in the trie
  ```

### Delete a Word

This method removes a word from the trie.

```python
trie.delete(word)
```

- **Args**: 
  - `word` (str): The word to delete from the trie.
  
- **Returns**: 
  - `None`
  
- **Example**:
  ```python
  trie.delete("apple")
  ```

### Insert a List of Words

This method allows for inserting multiple words into the trie at once.

```python
trie.insert_list(words)
```

- **Args**: 
  - `words` (list of str): A list of words to insert into the trie.
  
- **Returns**: 
  - `None`
  
- **Example**:
  ```python
  trie.insert_list(["apple", "banana", "cherry"])
  ```

### Starts With

This method checks if any word in the trie starts with a given prefix.

```python
trie.starts_with(prefix)
```

- **Args**: 
  - `prefix` (str): The prefix to check for.
  
- **Returns**: 
  - `bool`: `True`  if any word starts with the prefix, `False` otherwise.
  
- **Example**:
  ```python
  exists = trie.starts_with("app")  # returns True if "apple" or "apply" or "application"... is in the trie
  ```


---

## Usage Example

To use the trie functionality, follow this example:

```python
if __name__ == "__main__":
    trie = Trie()
    
    trie.insert("apple")
    
    print(trie.search("apple"))   # Output: True
    print(tries.search("app"))    # Output: False
    print(trie.starts_with("app"))      # Output: True
    
    trie.delete("apple")
    print(trie.search("apple"))  # Output: False
    
    trie.insert_list(["banana", "cherry"])
    print(trie.search("banana"))  # Output: True
```

### Expected Output

```
True
False
True
False
True
```

You can replace the words with any string you want to manage in the trie.

---

Feel free to reach out if you have any questions about how to use the Tries module!
