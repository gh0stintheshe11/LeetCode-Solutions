class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for d in range(3, n):
            for c in range(2, d):
                for b in range(1, c):
                    for a in range(0, b):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            count += 1
        return count