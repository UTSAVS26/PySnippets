import hashlib
import unittest
from Hashing import HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable(size=5)

    def test_insert_and_search(self):
        self.ht.insert(10, 'Value1')
        self.ht.insert(15, 'Value2')
        self.assertEqual(self.ht.search(10), 'Value1')
        self.assertEqual(self.ht.search(15), 'Value2')
        self.assertIsNone(self.ht.search(20))

    def test_update_value(self):
        self.ht.insert(10, 'Value1')
        self.ht.insert(10, 'NewValue')
        self.assertEqual(self.ht.search(10), 'NewValue')

    def test_delete_key(self):
        self.ht.insert(10, 'Value1')
        self.assertTrue(self.ht.delete(10))
        self.assertIsNone(self.ht.search(10))
        self.assertFalse(self.ht.delete(10))

    def test_resize_table(self):
        for i in range(10):
            self.ht.insert(i, f'Value{i}')
        self.assertEqual(self.ht.size, 20)
        self.assertEqual(self.ht.search(5), 'Value5')
        self.assertEqual(self.ht.search(9), 'Value9')

    def test_string_hash(self):
        hash_value = HashTable.string_hash("example", 10)
        self.assertEqual(hash_value, sum(ord(char) for char in "example") % 10)

    def test_check_collisions(self):
        collisions = HashTable.check_collisions([1, 6, 11, 21], 5)
        self.assertEqual(collisions, [6, 11, 21])

    def test_sha256_hash(self):
        result = HashTable.sha256_hash("Hello, World!")
        expected = hashlib.sha256("Hello, World!".encode()).hexdigest()
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()