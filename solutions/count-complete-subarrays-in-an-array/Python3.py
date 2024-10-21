class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        distinct_total = len(set(nums))
        count = 0
        
        for start in range(n):
            seen = set()
            for end in range(start, n):
                seen.add(nums[end])
                if len(seen) == distinct_total:
                    count += n - end
                    break
        
        return count