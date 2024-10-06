# File Reader - PySnippets

Welcome to the **File Reader** module! This simple module provides functionality to read and retrieve the contents of text files. It's useful for quickly accessing text data in your applications.

## Table of Contents

- [Introduction](#introduction)
- [Functionality](#functionality)
  - [Read File](#read-file)
- [Usage Example](#usage-example)

---

## Introduction

The **File Reader** module allows users to read the contents of text files easily. This functionality is essential for applications that need to extract data from files or display file content to users.

---

## Functionality

### Read File

This function reads the contents of a specified text file and returns it as a string.

```python
read_file(file_path)
```

- **Args**: 
  - `file_path` (str): The path to the file you want to read.
- **Returns**: 
  - `str`: The contents of the file as a string.
- **Example**:
  ```python
  >>> read_file('example.txt')
  'File contents here...'
  ```

---

## Usage Example

To use the file reading functionality, simply call the `read_file` function with the path to the text file you want to read:

```python
if __name__ == "__main__":
    content = read_file("example.txt")
    print(content)
```

Make sure to replace `"example.txt"` with the actual path to your target text file. The function will read the file's content and print it to the console.

---

Feel free to reach out if you have any questions about how to use the File Reader module!
