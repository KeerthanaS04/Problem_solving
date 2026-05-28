from typing import List
from math import inf

class Trie:
    __slots__ = ('children', 'length', 'idx')
    def __init__(self):
        self.children = [None]*26
        # store the minimum length of strings passing through this code
        self.length = inf
        # store th eindex of the string with minimum length at the node
        self.idx = inf
    
    def insert(self, word: str, index: int) -> None:
        node = self
        if node.length>len(word):
            node.length = len(word)
            node.idx = index
        
        # insert characters in reverse order (for suffix matching)
        for c in word[::-1]:
            char_idx = ord(c)-ord('a')
            if node.children[char_idx] is None:
                node.children[char_idx] = Trie()
            
            # move to child node
            node = node.children[char_idx]
            # update this node with minimum length word info
            if node.length>len(word):
                node.length = len(word)
                node.idx = index
    
    def query(self, word: str) -> int:
        # find the index of the word with the longest common suffix
        node = self
        for char in word[::-1]:
            char_idx = ord(char)-ord('a')

            # stop if no further matching suffix exists
            if node.children[char_idx] is None:
                break

            # move to the next node
            node = node.children[char_idx]
        return node.idx
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie()
        for i, word in enumerate(wordsContainer):
            trie.insert(word, i)
        return [trie.query(word) for word in wordsQuery]