
import unittest
from caching import cache

@cache
def expensive_function(n):
    return n * n

class TestCache(unittest.TestCase):
    def test_cache(self):
        self.assertEqual(expensive_function(4), 16)
        self.assertEqual(expensive_function(4), 16)  # Cached result

if __name__ == '__main__':
    unittest.main()
