from typing import List
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def calculate_finish_time(first_start: List[int], first_duration: List[int], second_start: List[int], second_duration: List[int]) -> int:
            # find the earliest completion time of the first stage
            min_first_end = min(start+duration for start, duration in zip(first_start, first_duration))
            # for the second stage, we can start each activity at the maximum of its own time and the completion of the first stage
            min_total_time = min(
                max(start, min_first_end) + duration for start, duration in zip(second_start, second_duration)
            )
            return min_total_time
        
        # try both orderings
        land_then_water = calculate_finish_time(landStartTime, landDuration, waterStartTime, waterDuration)
        water_then_land = calculate_finish_time(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(land_then_water, water_then_land)