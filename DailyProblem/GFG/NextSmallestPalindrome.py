class Solution:
    def nextPalindrome(self, num):
        n = len(num)
        a = num[:] # copy to avoid modifying input
        ans = []
        solved = 0

        # try mirroring left->right
        for i in range(n//2, n):
            if a[i]<a[n-i-1]:
                a[i] = a[n-i-1]

                for j in range(i+1, n):
                    a[j] = a[n-j-1]
                solved = 1
                break
            elif a[i]>a[n-i-1]:
                break
        
        if solved:
            return a
        
        # increment middle and propagate carry
        carry = 1
        i = (n-1)//2

        while i>=0:
            if a[i]+carry==10:
                a[i] = 0
                carry = 1
            else:
                a[i]+=1
                carry = 0
                break
            i-=1
        
        # if carry still remains -> add new digit
        if carry:
            ans.append(1)
        
        # copy current array
        ans.extend(a)

        if carry==1:
            n+=1
        
        # mirror again
        for i in range((n+1)//2, n):
            ans[i] = ans[n-i-1]
        return ans