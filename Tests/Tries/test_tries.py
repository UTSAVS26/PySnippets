import unittest
from pysnippets.Tries.tries import Trie

class TestTrie(unittest.TestCase):
    
    def setUp(self):
        self.trie = Trie()

    def test_insert_single_word(self):
        # Test insertion of a single word into the Trie.
        
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"), "Should find the word 'apple'")
        self.assertFalse(self.trie.search("app"), "Should not find the word 'app' (not inserted)")
    
    def test_insert_multiple_words(self):
        # Test insertion of multiple words into the Trie.
        words = ["apple", "app", "apply", "bat", "ball"]
        self.trie.insert_list(words)
        
        # Check all words
        for word in words:
            self.assertTrue(self.trie.search(word), f"Should find the word '{word}'")
        
        # Check non-inserted words
        self.assertFalse(self.trie.search("batman"), "Should not find the word 'batman' (not inserted)")
        self.assertFalse(self.trie.search("apples"), "Should not find the word 'apples' (not inserted)")

    def test_starts_with_prefix(self):
        # Test the starts_with method to check if any words in the trie start with the given prefix.
        
        self.trie.insert("apple")
        self.trie.insert("app")
        self.assertTrue(self.trie.starts_with("app"), "Should return True for prefix 'app'")
        self.assertFalse(self.trie.starts_with("bat"), "Should return False for prefix 'bat'")

    def test_delete_word(self):
        # Test deletion of a word from the Trie.
        
        self.trie.insert("apple")
        self.trie.delete("apple")
        self.assertFalse(self.trie.search("apple"), "Should not find the word 'apple' after deletion")
    
    def test_partial_word_not_deleted(self):
        # Test that deleting a word does not affect other words with similar prefixes.
        
        self.trie.insert("apple")
        self.trie.insert("app")
        self.trie.delete("apple")
        self.assertFalse(self.trie.search("apple"), "Should not find 'apple' after deletion")
        self.assertTrue(self.trie.search("app"), "Should still find 'app'")

    def test_delete_non_existent_word(self):
        # Test deletion of a word that does not exist in the Trie.
        
        self.trie.insert("apple")
        self.trie.delete("banana")  # Deleting non-existent word should not raise an error
        self.assertTrue(self.trie.search("apple"), "Should still find 'apple' after attempting to delete 'banana'")

    def test_empty_trie(self):
        # Test search and starts_with on an empty Trie.
        
        self.assertFalse(self.trie.search("apple"), "Should not find any word in an empty Trie")
        self.assertFalse(self.trie.starts_with("a"), "Should return False for any prefix in an empty Trie")

    def test_insert_empty_string(self):
        # Test inserting an empty string into the Trie.
        
        self.trie.insert("")
        self.assertFalse(self.trie.search(""), "Should not find an empty string in the Trie")

    def test_insert_list_with_empty_string(self):
        # Test inserting a list of words where one of the words is an empty string.
        
        words = ["apple", "banana", ""]
        self.trie.insert_list(words)
        
        self.assertTrue(self.trie.search("apple"), "Should find the word 'apple'")
        self.assertTrue(self.trie.search("banana"), "Should find the word 'banana'")
        self.assertFalse(self.trie.search(""), "Should not find an empty string in the Trie")


if __name__ == '__main__':
    unittest.main()
