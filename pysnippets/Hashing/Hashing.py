import hashlib
from typing import Any, List, Optional, Tuple

class HashTable:
    def __init__(self, size: int = 10) -> None:
        self.size = size
        self.table: List[List[Tuple[int, Any]]] = [[] for _ in range(self.size)]

    def _hash_function(self, key: int) -> int:
        # Using simple modulo hash function
        return key % self.size

    def _resize(self) -> None:
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def load_factor(self) -> float:
        num_elements = sum(len(bucket) for bucket in self.table)
        return num_elements / self.size

    def insert(self, key: int, value: Any) -> None:
        if not isinstance(key, int):
            raise TypeError("Key must be an integer.")
        if self.load_factor() > 0.7:  # Check load factor
            self._resize()
        hash_key = self._hash_function(key)
        for pair in self.table[hash_key]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[hash_key].append((key, value))

    def search(self, key: int) -> Optional[Any]:
        if not isinstance(key, int):
            raise TypeError("Key must be an integer.")
        hash_key = self._hash_function(key)
        for pair in self.table[hash_key]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key: int) -> bool:
        if not isinstance(key, int):
            raise TypeError("Key must be an integer.")
        hash_key = self._hash_function(key)
        for i, pair in enumerate(self.table[hash_key]):
            if pair[0] == key:
                del self.table[hash_key][i]
                return True
        return False

    def display(self) -> None:
        for index, bucket in enumerate(self.table):
            print(f"Index {index} ({len(bucket)} entries): {bucket}")

    @staticmethod
    def string_hash(s: str, table_size: int) -> int:
        hash_value = sum(ord(char) for char in s)
        return hash_value % table_size

    @staticmethod
    def check_collisions(keys: List[int], table_size: int) -> List[int]:
        hash_table = {}
        collisions = []

        for key in keys:
            hash_key = key % table_size
            if hash_key in hash_table:
                collisions.append(key)
            else:
                hash_table[hash_key] = key

        return collisions

    @staticmethod
    def sha256_hash(string: str) -> str:
        return hashlib.sha256(string.encode()).hexdigest()


# Example usage:
if __name__ == "__main__":
    ht = HashTable()

    # Inserting values
    ht.insert(10, 'Value1')
    ht.insert(20, 'Value2')
    ht.insert(30, 'Value3')

    # Display the hash table
    ht.display()

    # Search for a key
    print("Search key 20:", ht.search(20))

    # Delete a key
    ht.delete(20)
    print("After deleting key 20:")
    ht.display()

    # Hashing a string
    print("Hash of 'example':", ht.string_hash("example", 10))

    # Checking collisions
    print("Collisions in [1, 2, 12, 22, 32]:", ht.check_collisions([1, 2, 12, 22, 32], 10))

    # SHA-256 Hashing
    print("SHA-256 hash of 'Hello, World!':", ht.sha256_hash("Hello, World!"))