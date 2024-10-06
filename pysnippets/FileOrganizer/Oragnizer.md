# File Organizer - PySnippets

Welcome to the **File Organizer** module! This module provides functionality to organize files within a specified folder based on their file types. It helps in keeping your folders tidy and makes it easier to manage files.

## Table of Contents

- [Introduction](#introduction)
- [Functionality](#functionality)
  - [Organize Files by Type](#organize-files-by-type)
- [Error Handling](#error-handling)
- [Usage Example](#usage-example)

---

## Introduction

The **File Organizer** module is designed to categorize files into subfolders based on their extensions. It can categorize files into different types such as images, documents, videos, music, archives, scripts, fonts, and system files. This allows users to maintain a cleaner and more organized file structure.

---

## Functionality

### Organize Files by Type

This function organizes files in the specified folder by type. It creates subfolders for each file category and moves the files into their respective folders based on their extensions.

```python
organize_files_by_type(folder_path)
```

- **Args**: 
  - `folder_path` (str): The path to the folder to organize.
- **Returns**: None.
- **Example**: 
  If you have a folder with mixed files like images, documents, and videos, this function will move them into subfolders named 'Images', 'Documents', 'Videos', etc., according to their file types.

---

## Error Handling

The function includes error handling to manage invalid paths. If the specified `folder_path` does not exist, a `ValueError` will be raised.

- **Raises**:
  - `ValueError`: If the `folder_path` does not exist.

---

## Usage Example

To use the file organizing functionality, simply call the function by providing the path to your target folder:

```python
if __name__ == "__main__":
    folder_to_organize = r"path_to_the_folder"  # Replace with the actual folder path
    try:
        organize_files_by_type(folder_to_organize)
    except ValueError as e:
        print(e)
```

Replace `path_to_the_folder` with the path to the folder containing the files you want to organize. The function will then move files into categorized subfolders accordingly.

---

Feel free to reach out if you have any questions about how to use the File Organizer module!
