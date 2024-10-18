class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums):
            j = i
            while j < len(nums) and bin(nums[i]).count('1') == bin(nums[j]).count('1'):
                j += 1
            nums[i:j] = sorted(nums[i:j])
            i = j
        return nums == sorted(nums)