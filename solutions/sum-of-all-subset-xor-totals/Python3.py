class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index, current_xor):
            if index == len(nums):
                return current_xor
            # Move to the next index without the current number
            without_current = dfs(index + 1, current_xor)
            # Include the current number in the XOR
            with_current = dfs(index + 1, current_xor ^ nums[index])
            return without_current + with_current
        
        return dfs(0, 0)