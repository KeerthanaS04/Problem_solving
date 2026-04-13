class Solution:
    def nearestPalindromic(self, n: str) -> str:
        original_num = int(n)
        length = len(n)

        # intialize candidate set with edge cases
        # 1. Largest Palindrome with (length-1) 999...999
        # 2. Smallest Palindrome with (length+1) 100...001
        candidates = {10**(length+1)-1, 10**length+1}
        prefix_length = (length+1)//2
        prefix = int(n[:prefix_length])

        # genertae palindromes by mirroring prefix-1, prefix, prefix+1
        for prefix_variant in range(prefix-1, prefix+2):
            palindrome = prefix_variant
            suffix_to_mirror = prefix_variant if length%2==0 else prefix_variant//10

            # mirror the digits to create the full palindrome
            while suffix_to_mirror>0:
                palindrome = palindrome*10+suffix_to_mirror%10
                suffix_to_mirror//=10
            candidates.add(palindrome)
        
        # remove the original number from candidates
        candidates.discard(original_num)
        nearest_palindrome = -1
        for candidate in candidates:
            dist_to_candidate = abs(candidate-original_num)
            dist_to_curr_nearest = abs(nearest_palindrome-original_num)

            # update if this is the first candidate or if its closer, or if its equally close but smaller
            if (nearest_palindrome==-1 or dist_to_candidate<dist_to_curr_nearest or 
                (dist_to_candidate==dist_to_curr_nearest and candidate<nearest_palindrome)):
                nearest_palindrome = candidate
        return str(nearest_palindrome)