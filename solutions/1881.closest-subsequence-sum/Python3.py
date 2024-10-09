class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        from itertools import combinations
        from bisect import bisect_left
        
        def get_all_sums(array):
            all_sums = set()
            n = len(array)
            for i in range(n + 1):
                for comb in combinations(array, i):
                    all_sums.add(sum(comb))
            return sorted(all_sums)
        
        n = len(nums)
        left_part = nums[:n // 2]
        right_part = nums[n // 2:]
        
        left_sums = get_all_sums(left_part)
        right_sums = get_all_sums(right_part)
        
        min_diff = float('inf')
        
        for sum_right in right_sums:
            required = goal - sum_right
            pos = bisect_left(left_sums, required)
            
            if pos < len(left_sums):
                min_diff = min(min_diff, abs(goal - (left_sums[pos] + sum_right)))
            
            if pos > 0:
                min_diff = min(min_diff, abs(goal - (left_sums[pos - 1] + sum_right)))
        
        return min_diff