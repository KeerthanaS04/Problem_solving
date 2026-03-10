class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        from functools import cache
        MOD = 10**9+7

        @cache
        def count_arrays(zero_left: int, one_left: int, last_element: int) -> int:
            # base case: no zeros left
            if zero_left==0:
                return 1 if (last_element==1 and one_left<=limit) else 0
            # base case: no ones left
            if one_left==0:
                return 1 if (last_element==0 and zero_left<=limit) else 0
            
            # if last element is 0, we are placing another 0
            if last_element==0:
                total_ways = count_arrays(zero_left-1, one_left, 0)+ count_arrays(zero_left-1, one_left, 1)

                # subtract invalid cases
                if zero_left-limit-1>=0:
                    total_ways-=count_arrays(zero_left-limit-1, one_left, 1)
                return total_ways
            else:
                total_ways = count_arrays(zero_left, one_left-1, 0)+count_arrays(zero_left, one_left-1, 1)

                # subtract invalid cases
                if one_left-limit-1>=0:
                    total_ways-=count_arrays(zero_left, one_left-limit-1, 0)
                return total_ways
        result = (count_arrays(zero, one, 0)+count_arrays(zero, one, 1))%MOD
        count_arrays.cache_clear()
        return result