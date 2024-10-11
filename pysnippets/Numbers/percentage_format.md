
# Percentage Formatting

This module provides a function to format a number as a percentage of a total.

## Functionality

### percentage_format

- **Args**:
  - `num` (float or int): The part value.
  - `total` (float or int): The total value.
  - `decimals` (int, optional): The number of decimal places.
- **Returns**:
  - `str`: The formatted percentage as a string.
  
### Example
```python
from percentage_format import percentage_format

print(percentage_format(50, 200)) # Outputs: 25.00%
```

---
