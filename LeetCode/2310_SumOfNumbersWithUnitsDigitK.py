class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        # 10x+k
        if num == 0:
            return 0
        
        for i in range(1, num+1):
            remaining_val = num - i*k
            if remaining_val >= 0 and remaining_val % 10 == 0:
                return i
        return -1