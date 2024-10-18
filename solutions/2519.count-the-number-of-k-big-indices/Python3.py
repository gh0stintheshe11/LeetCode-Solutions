from typing import List
from bisect import bisect_left, insort

class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        def count_smaller_left(nums):
            sorted_left = []
            res = []
            for num in nums:
                pos = bisect_left(sorted_left, num)
                res.append(pos)
                insort(sorted_left, num)
            return res

        def count_smaller_right(nums):
            sorted_right = []
            res = []
            for num in reversed(nums):
                pos = bisect_left(sorted_right, num)
                res.append(pos)
                insort(sorted_right, num)
            return res[::-1]

        left_smaller = count_smaller_left(nums)
        right_smaller = count_smaller_right(nums)

        k_big_count = 0
        for i in range(len(nums)):
            if left_smaller[i] >= k and right_smaller[i] >= k:
                k_big_count += 1

        return k_big_count