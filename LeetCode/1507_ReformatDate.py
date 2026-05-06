class Solution:
    def reformatDate(self, date: str) -> str:
        date_parts = date.split()
        date_parts.reverse()

        month = ' JanFebMarAprMayJunJulAugSepOctNovDec'

        # convert month abbreviation to month number
        month_idx = month.index(date_parts[1])
        month_no = month_idx//3+1
        date_parts[1] = str(month_no).zfill(2)

        # extract day number by removing suffix(st,nd,rd,th)
        day_no = date_parts[2][:-2]
        date_parts[2] = day_no.zfill(2)
        return '-'.join(date_parts)