class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        # Option 1: change the two largest numbers
        change_two_largest = nums[n-2] - nums[1]
        
        # Option 2: change the largest and smallest number
        change_largest_and_smallest = nums[n-1] - nums[2]
        
        # Option 3: change the two smallest numbers
        change_two_smallest = nums[n-3] - nums[0]
        
        return min(change_two_largest, change_largest_and_smallest, change_two_smallest)