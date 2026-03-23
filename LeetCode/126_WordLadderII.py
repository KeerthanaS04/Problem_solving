from typing import List
from collections import deque, defaultdict
class Solution:
    def findLadder(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def build_paths(curr_path: List[str], curr_word: str) -> None:
            if curr_word==beginWord:
                result_paths.append(curr_path[::-1])
                return 
            
            # explore all predecessors which lead to curr word
            for pre_word in pre[curr_word]:
                curr_path.append(pre_word)
                build_paths(curr_path, pre_word)
                curr_path.pop()
        result_paths = []
        available_words = set(wordList)
        if endWord not in available_words:
            return result_paths
        available_words.discard(beginWord)
        word_distances = {beginWord: 0}
        pre = defaultdict()

        bfs_queue = deque([beginWord])
        target_found = False
        curr_distance = 0

        while bfs_queue and not target_found:
            curr_distance+=1
            level_size = len(bfs_queue)
            for _ in range(level_size):
                curr_word = bfs_queue.popleft()
                word_chars = list(curr_word)
                for char_index in range(len(word_chars)):
                    original_char = word_chars[char_index]
                    for letter_idx in range(26):
                        word_chars[char_index] = chr(ord('a')+letter_idx)
                        transfor_word = ''.join(word_chars)

                        # if word was already discovered add pre
                        if word_distances.get(transfor_word, 0)==curr_distance:
                            pre[transfor_word].add(curr_word)
                        if transfor_word not in available_words:
                            continue

                        # record pre and process word
                        pre[transfor_word].add(curr_word)
                        available_words.discard(transfor_word)
                        bfs_queue.append(transfor_word)
                        word_distances[transfor_word] = curr_distance

                        # check if target is reached
                        if transfor_word==endWord:
                            target_found=True
                    word_chars[char_index] = original_char
        if target_found:
            initial_path = [endWord]
            build_paths(initial_path, endWord)
        return result_paths