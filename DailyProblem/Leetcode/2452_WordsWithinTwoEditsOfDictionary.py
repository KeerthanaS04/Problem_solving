from typing import List
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []

        for query_word in queries:
            for dict_word in dictionary:
                differences = sum(char_q!=char_d for char_q, char_d in zip(query_word, dict_word))

                if differences<=2:
                    res.append(query_word)
                    break
        return res