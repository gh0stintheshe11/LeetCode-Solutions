class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        nums_idx = 0
        n = len(nums)
        
        for group in groups:
            found = False
            while nums_idx <= n - len(group):
                # Check if group matches subarray in nums starting at nums_idx
                if nums[nums_idx:nums_idx+len(group)] == group:
                    found = True
                    # Move nums index past the current group
                    nums_idx += len(group)
                    break
                else:
                    nums_idx += 1
            
            if not found:
                return False
        
        return True