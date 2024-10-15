class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        # A set to store all the numbers present in nums
        num_set = set(nums)
        
        # Check for each power of 2 starting from 1, 2, 4, 8, ...
        power = 1
        while True:
            if power not in num_set:
                return power
            power *= 2