class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        from collections import Counter

        count = Counter(nums)
        maximum_frequency = max(count.values())
        
        total_numbers = len(nums)
        
        if maximum_frequency <= total_numbers // 2:
            return total_numbers % 2
        else:
            return 2 * maximum_frequency - total_numbers