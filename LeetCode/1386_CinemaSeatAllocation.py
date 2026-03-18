from typing import List
from collections import defaultdict
class Solution:
    def maximumNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_by_row = defaultdict(int)

        # convert reserved seats to bitmask manipulation
        for row, seat in reservedSeats:
            reserved_by_row[row]|=1<<(10-seat)
        
        # the seats can be given are 2-5, 6-9, and 4-7
        family_group_mask = (0b0111100000, 0b0000011110, 0b0001111000)

        # rows without any reservation
        total_families = (n-len(reserved_by_row))*2

        for row_reservation in reserved_by_row.values():
            for mask in family_group_mask:
                if row_reservation&mask==0:
                    # mark the reserved seats
                    row_reservation|=mask
                    total_families+=1
        return total_families
