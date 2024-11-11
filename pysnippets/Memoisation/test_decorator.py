import unittest
from decorator import memoize

class TestMemoizeDecorator(unittest.TestCase):
    
    def test_memoize_add_function(self):
        call_count = 0
        
        @memoize
        def add(a, b):
            nonlocal call_count
            call_count += 1
            return a + b
        
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(call_count, 1)

if __name__ == "__main__":
    unittest.main() 