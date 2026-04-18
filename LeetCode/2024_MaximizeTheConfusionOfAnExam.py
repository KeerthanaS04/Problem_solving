class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def find_max_consecutives(target_char: str) -> int:
            count = 0
            l = 0

            for r, char in enumerate(answerKey):
                if char==target_char:
                    count+=1
                if count>k:
                    if answerKey[l]==target_char:
                        count-=1
                    left+=1
            return len(answerKey)-left
        return max(find_max_consecutives('T'), find_max_consecutives('F'))