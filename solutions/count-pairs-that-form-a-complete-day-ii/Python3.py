class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        from collections import defaultdict

        remainder_count = defaultdict(int)
        count = 0

        for hour in hours:
            mod_val = hour % 24
            complement = (24 - mod_val) % 24
            count += remainder_count[complement]
            remainder_count[mod_val] += 1

        return count