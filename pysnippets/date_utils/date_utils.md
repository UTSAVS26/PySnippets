# Overview

This module provides a function to convert date strings into ISO-8601 format. The function handles input strings in both 'YYYY-MM-DD' and 'MM/DD/YYYY' formats.

## Table of Contents

1. [Requirements](#requirements)
2. [Function: `convert_to_iso8601`](#function-convert_to_iso8601)
   - [Arguments](#arguments)
   - [Returns](#returns)
   - [Example Usage](#example-usage)

## Requirements

To use this module, you need Python's built-in `datetime` library. There are no additional libraries required.

## Function: `convert_to_iso8601`

```python
convert_to_iso8601(date_string)
```

Converts a date string to ISO-8601 format.

### Arguments

- **date_string** (str): A date string in the format 'YYYY-MM-DD' or 'MM/DD/YYYY'.

### Returns

- **str**: The date in ISO-8601 format (YYYY-MM-DD). If the input format is invalid, an error message is returned.

### Example Usage

```python
if __name__ == "__main__":
    print(convert_to_iso8601("2024-10-06"))  # Outputs: 2024-10-06T00:00:00
    print(convert_to_iso8601("10/06/2024"))  # Outputs: 2024-10-06T00:00:00
```
