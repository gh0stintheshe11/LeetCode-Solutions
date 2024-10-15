from typing import List
from collections import defaultdict

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_squares = 0
        for start in range(n):
            count_map = defaultdict(int)
            distinct_count = 0
            for end in range(start, n):
                if count_map[nums[end]] == 0:
                    distinct_count += 1
                count_map[nums[end]] += 1
                sum_of_squares += distinct_count * distinct_count
        return sum_of_squares