class Solution:
    def longestAwesome(self, s: str) -> int:
        prefix_status = {0: -1}
        max_length = 0
        current_status = 0

        for i, char in enumerate(s):
            digit = int(char)
            current_status ^= (1 << digit)

            if current_status in prefix_status:
                max_length = max(max_length, i - prefix_status[current_status])
            else:
                prefix_status[current_status] = i

            for j in range(10):
                test_status = current_status ^ (1 << j)
                if test_status in prefix_status:
                    max_length = max(max_length, i - prefix_status[test_status])

        return max_length