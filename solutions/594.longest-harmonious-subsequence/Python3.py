class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        max_len = 0
        for k in count:
            if k + 1 in count:
                max_len = max(max_len, count[k] + count[k + 1])
        return max_len