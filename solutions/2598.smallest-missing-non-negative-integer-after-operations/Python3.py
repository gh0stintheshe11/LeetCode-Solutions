class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        from collections import defaultdict
        
        remainder_counts = defaultdict(int)
        
        for num in nums:
            remainder = num % value
            remainder_counts[remainder] += 1
        
        mex = 0
        while True:
            remainder = mex % value
            if remainder_counts[remainder] > 0:
                remainder_counts[remainder] -= 1
            else:
                return mex
            mex += 1