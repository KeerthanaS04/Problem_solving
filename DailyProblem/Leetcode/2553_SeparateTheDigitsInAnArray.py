class Solution:
    def separateDigits(self, nums):
        res = []
        for num in nums:
            digit_st = []
            while num>0:
                digit = num%10
                digit_st.append(digit)
                num = num//10
            res.extend(digit_st[::-1]) # add digits in correct order
        return res