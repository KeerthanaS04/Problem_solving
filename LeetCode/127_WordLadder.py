from typing import List
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        available_words = set(wordList)
        if endWord not in available_words:
            return 0
        queue = deque([beginWord])
        transform_length = 1
        
        while queue:
            transform_length+=1
            curr_size = len(queue)
            for _ in range(curr_size):
                curr_word = queue.popleft()
                word_chars = list(curr_word)
                for position in range(len(word_chars)):
                    original_char = word_chars[position]
                    for letter_idx in range(26):
                        word_chars[position] = chr(ord('a')+letter_idx)
                        new_word = ''.join(word_chars)

                        # skip the word if it is not in available words
                        if new_word not in available_words:
                            continue
                        # check if we reached the target
                        if new_word==endWord:
                            return transform_length
                        # add valid ones to the queue
                        queue.append(new_word)
                        # remove from the available words so to avoid revisiting
                        available_words.remove(new_word)
                    # restore the original character for next position
                    word_chars[position] = original_char
        return 0