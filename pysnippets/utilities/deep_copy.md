
# Deep Copy of an Object

This snippet creates a deep copy of an object, which can be useful when you want to create a copy that does not reference the original object.

## Code
```python
import copy

def deep_copy(obj):
    return copy.deepcopy(obj)
```

## Usage
```python
original = {'a': 1, 'b': [2, 3, 4]}
copy = deep_copy(original)
print(copy)
```
