class Solution:
    def subsetsWithDup(self, nums):
        res = [[]]
        nums.sort()
        for num in nums:
            res += [i + [num] for i in res if i + [num] not in res]
        return res