class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        from functools import reduce
        from operator import or_
        
        def dfs(i, current_or):
            if i == len(nums):
                return 1 if current_or == max_or else 0
            return dfs(i + 1, current_or | nums[i]) + dfs(i + 1, current_or)

        max_or = reduce(or_, nums)
        return dfs(0, 0)