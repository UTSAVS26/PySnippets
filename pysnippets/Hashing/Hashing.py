import hashlib
import logging
from typing import Any, List, Optional
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class HashTableEntry:
    key: int
    value: Any

class HashTable:
    def __init__(self, size: int = 10) -> None:
        self.size = size
        self.table: List[List[HashTableEntry]] = [[] for _ in range(self.size)]
        logging.info(f"Initialized HashTable with size {self.size}")

    def _hash_function(self, key: int) -> int:
        return key % self.size

    def _resize(self) -> None:
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        logging.info(f"Resized HashTable to new size {self.size}")

        for bucket in old_table:
            for entry in bucket:
                self.insert(entry.key, entry.value)

    def load_factor(self) -> float:
        num_elements = sum(len(bucket) for bucket in self.table)
        return num_elements / self.size

    def insert(self, key: int, value: Any) -> None:
        if not isinstance(key, int):
            raise TypeError("Key must be an integer.")
        if self.load_factor() > 0.7:
            self._resize()
        hash_key = self._hash_function(key)
        for entry in self.table[hash_key]:
            if entry.key == key:
                entry.value = value
                logging.info(f"Updated key {key} with new value {value}")
                return
        self.table[hash_key].append(HashTableEntry(key, value))
        logging.info(f"Inserted key {key} with value {value}")

    def search(self, key: int) -> Optional[Any]:
        if not isinstance(key, int):
            raise TypeError("Key must be an integer.")
        hash_key = self._hash_function(key)
        for entry in self.table[hash_key]:
            if entry.key == key:
                logging.info(f"Found key {key} with value {entry.value}")
                return entry.value
        logging.warning(f"Key {key} not found")
        return None

    def delete(self, key: int) -> bool:
        if not isinstance(key, int):
            raise TypeError("Key must be an integer.")
        hash_key = self._hash_function(key)
        for i, entry in enumerate(self.table[hash_key]):
            if entry.key == key:
                del self.table[hash_key][i]
                logging.info(f"Deleted key {key}")
                return True
        logging.warning(f"Key {key} not found for deletion")
        return False

    def display(self) -> None:
        for index, bucket in enumerate(self.table):
            logging.info(f"Index {index} ({len(bucket)} entries): {[(entry.key, entry.value) for entry in bucket]}")

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


if __name__ == "__main__":
    ht = HashTable()

    ht.insert(10, 'Value1')
    ht.insert(20, 'Value2')
    ht.insert(30, 'Value3')

    ht.display()

    print("Search key 20:", ht.search(20))

    ht.delete(20)
    print("After deleting key 20:")
    ht.display()

    print("Hash of 'example':", ht.string_hash("example", 10))

    print("Collisions in [1, 2, 12, 22, 32]:", ht.check_collisions([1, 2, 12, 22, 32], 10))

    print("SHA-256 hash of 'Hello, World!':", ht.sha256_hash("Hello, World!"))