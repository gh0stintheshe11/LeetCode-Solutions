class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        count_map = defaultdict(int)
        total_pairs = 0
        good_pairs_count = 0
        
        for i, num in enumerate(nums):
            x = num - i
            good_pairs_count += count_map[x]
            count_map[x] += 1
            total_pairs += i
        
        return total_pairs - good_pairs_count