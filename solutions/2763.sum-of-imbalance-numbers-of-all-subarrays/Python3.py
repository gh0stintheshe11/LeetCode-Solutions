class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        indices = {}
        total = 0
        prev = 0
        indices[nums[0]] = 0
        for i in range(1, len(nums)):
            curSum = prev
            below_index = indices[nums[i]-1] if nums[i]-1 in indices else -1
            above_index = indices[nums[i]+1] if nums[i]+1 in indices else -1
            cur_index = indices[nums[i]] if nums[i] in indices else -1
            soonest_zero_imbalance = max(max(below_index, above_index), cur_index)
            if soonest_zero_imbalance == -1:
                curSum += i
            else:
                curSum += i - soonest_zero_imbalance - 1
            if below_index != -1 and above_index != -1 and min(below_index, above_index) > cur_index:
                curSum -= min(below_index, above_index) + 1
                if cur_index != -1:
                    curSum += cur_index + 1
            total += curSum
            prev = curSum 
            indices[nums[i]] = i
        return total