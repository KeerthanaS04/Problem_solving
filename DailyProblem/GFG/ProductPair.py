class Solution:
    def isProduct(self, arr, target):
        s = set()
        for num in arr:
            if num==0:
                if target==0:
                    return True
                continue

            if target%num==0:
                temp = target//num
                if temp in s:
                    return True
            s.add(num)
        return False