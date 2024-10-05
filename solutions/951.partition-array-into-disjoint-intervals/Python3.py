class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        left_max = nums[0]
        global_max = nums[0]
        partition_idx = 0

        for i in range(1, n):
            global_max = max(global_max, nums[i])
            if nums[i] < left_max:
                left_max = global_max
                partition_idx = i

        return partition_idx + 1