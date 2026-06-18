class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = hour*30+minutes*0.5
        minute_angle = minutes*6
        res = abs(hour_angle-minute_angle)
        return min(res, 360-res)