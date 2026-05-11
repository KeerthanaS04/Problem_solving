class Solution:
    def palindromePairs(self, arr):
        n = len(arr)
        mp = {}

        for i in range(n):
            mp[arr[i]] = i
        
        # case 1: direct reverse exists
        for i in range(n):
            reversed_word = arr[i][::-1]
            if reversed_word in mp and mp[reversed_word] != i:
                return 1
        
        # case 2: split the word and check for palindrome
        for i in range(n):
            curr = arr[i]
            for j in range(1, len(curr)):
                left = curr[:j]
                right = curr[j:]

                # if left is palindrome, check reversed right exists
                if self.is_palindrome(left):
                    reversed_right = right[::-1]
                    if reversed_right in mp:
                        return 1
                
                # if right is palindrome, check reversed left exists
                if self.is_palindrome(right):
                    reversed_left = left[::-1]
                    if reversed_left in mp:
                        return 1
        return 0
    
    def is_palindrome(self, word):
        i, j = 0, len(word) - 1
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True