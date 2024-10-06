class Solution:
    def maxProduct(self, nums) -> int:
        first_max, second_max = 0, 0
        
        for num in nums:
            if num > first_max:
                second_max = first_max
                first_max = num
            elif num > second_max:
                second_max = num
        
        return (first_max - 1) * (second_max - 1)