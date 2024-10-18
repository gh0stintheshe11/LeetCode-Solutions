class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        current_zeros = 0
        
        for num in nums:
            if num == 0:
                current_zeros += 1
                count += current_zeros
            else:
                current_zeros = 0
                
        return count