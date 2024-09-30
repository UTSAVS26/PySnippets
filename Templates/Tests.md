## Tests Template

```python
import unittest
from snippets.<category>.<snippet_name> import <function_name>

class Test<FunctionName>(unittest.TestCase):

    def test_case_1(self):
        # Test case for normal behavior
        self.assertEqual(<function_name>(<input>), <expected_output>)

    def test_case_2(self):
        # Test case for edge behavior
        self.assertEqual(<function_name>(<input>), <expected_output>)

    def test_case_invalid(self):
        # Test case for invalid input
        with self.assertRaises(<ExpectedException>):
            <function_name>(<invalid_input>)

if __name__ == '__main__':
    unittest.main()
```
