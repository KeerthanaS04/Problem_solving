class Solution:
    def minimumSteps(self, s: str) -> int:
        string_length = len(s)
        total_steps = 0
        ones_count = 0

        for curr_idx in range(string_length-1, -1, -1):
            if s[curr_idx] == '1':
                ones_count += 1

                # target positon is (string_length-ones_count)
                # steps needed = target_position - curr_idx
                steps_needed = (string_length-ones_count)-curr_idx
                total_steps += steps_needed
        return total_steps