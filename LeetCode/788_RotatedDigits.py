class Solution:
    def rotatedDigits(self, n: int) -> int:
        def good_number(number):
            rotated_number = 0
            temp = number
            place_val = 1

            while temp:
                digit = temp%10

                if rotation_map[digit]==-1:
                    return False
                rotated_number = rotation_map[digit]*place_val + rotated_number
                place_val*=10
                temp//=10
            return rotated_number!=number
        rotation_map = [0,1,5,-1,-1,2,9,-1,8,6]
        return sum(good_number(i) for i in range(1,n+1))