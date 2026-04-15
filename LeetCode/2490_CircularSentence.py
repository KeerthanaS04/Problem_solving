class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)

        for i, word in enumerate(words):
            next_word_idx = (i+1)%n
            if word[-1]!=words[next_word_idx][0]:
                return False
        return True