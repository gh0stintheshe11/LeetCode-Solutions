class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_set = set()
        suffix_counts = [0] * n
        diff = [0] * n
        
        # Count unique elements in the suffix initially
        unique = set()
        for i in range(n - 1, -1, -1):
            unique.add(nums[i])
            suffix_counts[i] = len(unique)
        
        # Calculate the difference array
        for i in range(n):
            prefix_set.add(nums[i])
            if i < n - 1:
                diff[i] = len(prefix_set) - suffix_counts[i + 1]
            else:
                diff[i] = len(prefix_set)
        
        return diff