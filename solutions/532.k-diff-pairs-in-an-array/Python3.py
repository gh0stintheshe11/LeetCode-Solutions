class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter

        if k < 0:
            return 0

        count = 0
        nums_counter = Counter(nums)

        if k == 0:
            for value in nums_counter.values():
                if value > 1:
                    count += 1
        else:
            for num in nums_counter:
                if num + k in nums_counter:
                    count += 1

        return count