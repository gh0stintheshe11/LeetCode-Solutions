class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        from collections import defaultdict
        
        remainder_count = defaultdict(int)
        count = 0
        
        for hour in hours:
            remainder = hour % 24
            complement = (24 - remainder) % 24
            count += remainder_count[complement]
            remainder_count[remainder] += 1
        
        return count