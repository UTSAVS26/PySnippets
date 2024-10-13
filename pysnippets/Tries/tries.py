from typing import List

# Structure of the Trie Tree
class TrieNode:
  def __init__(self):
    self.children = {}
    self.is_end_of_word = False

# main class
class Trie:
  def __init__(self):
    self.root = TrieNode()
  
  def insert(self, word:str) -> None:
    # function to insert a single word in the trie
    if word == "":
      return

    current_node = self.root  
    
    for char in word:
    
      if char not in current_node.children:
        current_node.children[char] = TrieNode()
      current_node = current_node.children[char]
    
    current_node.is_end_of_word = True
  
  def insert_list(self, words:List[str]) -> None:
    # function to insert a list of words into the trie  
    current_node = self.root

    for word in words:
      self.insert(word)
  
  def search(self, word:str) -> bool:
    # function to search if a word is present in the trie or not
    # return type boolean value (True/False)    
    current_node = self.root

    for char in word:
      if char not in current_node.children:
        return False
      
      current_node = current_node.children[char]
    
    # return True if word is found in the trie and is the end of a word
    return current_node.is_end_of_word
      
  def starts_with(self, prefix:str) -> bool:
    # fucntion to search for a given pattern in the trie
    # return a boolean value
    current_node = self.root
    for char in prefix:
      if char not in current_node.children:
        return False

      current_node = current_node.children[char]
    return True
  
  def delete(self, word:str) -> None:
    # function to delete a word from trie

    def _delete(node: TrieNode, word:str, depth:int ) -> bool:
      # if trie is empty
      if not node:
        return False

      if depth == len(word):
        # for last character of the word , unmarks it as the end of word
        if not node.is_end_of_word:
          return False
        
        node.is_end_of_word = False

        # return if node has any child , if not it is safe to be deleted
        return len(node.children) == 0
      
      char = word[depth]
      if char not in node.children:
        return False
      
      # check if character can be deleted
      safe_to_delete = _delete(node.children[char], word, depth+1)

      # if true, delete the child node reference
      if safe_to_delete:
        del node.children[char]
        return len(node.children) == 0 and not node.is_end_of_word

      return False
    
    _delete(self.root, word, 0)
      
