class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter
        
        count = Counter(nums)
        good_pairs = 0
        
        for value in count.values():
            if value > 1:
                good_pairs += value * (value - 1) // 2
                
        return good_pairs