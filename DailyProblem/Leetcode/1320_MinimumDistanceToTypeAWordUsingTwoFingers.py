class Solution:
    def minimumDistance(self, word: str) -> int:
        def calculate_dist(char1: int, char2: int) -> int:
            row1, col1 = divmod(char1, 6)
            row2, col2 = divmod(char2, 6)
            return abs(row1-row2)+abs(col1-col2)
        
        word_length = len(word)
        dp = [[[float('inf')]*26 for _ in range(26)] for _ in range(word_length)]

        first_char_idx = ord(word[0]) - ord('A')
        for finger_pos in range(26):
            dp[0][first_char_idx][finger_pos] = 0
            dp[0][finger_pos][first_char_idx] = 0
        
        # process each subsequent character
        for i in range(1, word_length):
            prev_char_idx = ord(word[i-1]) - ord('A')
            curr_char_idx = ord(word[i]) - ord('A')
            distance_between_char = calculate_dist(prev_char_idx, curr_char_idx)

            for other_finger in range(26):
                # case 1: same finger that typed previous char types curr char
                dp[i][curr_char_idx][other_finger] = min(
                    dp[i][curr_char_idx][other_finger],
                    dp[i-1][prev_char_idx][other_finger] + distance_between_char
                )

                # case 2: other finger types curr char
                if other_finger==prev_char_idx:
                    for prev_pos in range(26):
                        dist_to_curr = calculate_dist(prev_pos, curr_char_idx)
                        dp[i][curr_char_idx][other_finger] = min(
                            dp[i][curr_char_idx][other_finger],
                            dp[i-1][prev_pos][prev_pos] + dist_to_curr
                        )
            last_char_idx = ord(word[-1]) - ord('A')
            min_left_finger = min(dp[word_length-1][last_char_idx])
            min_right_finger = min(dp[word_length-1][j][last_char_idx] for j in range(26))
            return int(min(min_left_finger, min_right_finger))