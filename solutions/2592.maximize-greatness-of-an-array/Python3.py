class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        perm = nums
        perm.sort()
        cnt = 0
        i, j = 0, 0
        while i < len(nums) and j < len(perm):
            if nums[i] == perm[j]:
                j += 1
            elif nums[i] < perm[j]:
                cnt += 1
                i += 1
                j += 1
            else:
                i += 1
        return cnt