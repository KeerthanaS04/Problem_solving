class Solution:
    def getCount(self, n):
        doubled_n = n<<1
        count = 0
        sequence_length = 1

        while sequence_length*(sequence_length+1) <= doubled_n:
            if (doubled_n%sequence_length == 0 and (doubled_n//sequence_length-sequence_length+1)%2 == 0):
                count += 1
            sequence_length += 1
        # we shouldn't include 1
        return count-1