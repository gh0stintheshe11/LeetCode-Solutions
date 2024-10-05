class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = one = two = 0
        
        for num in nums:
            if num == 0:
                zero += 1
            elif num== 1:
                one += 1
            else:
                two += 1
                
        for i in range(zero):
            nums[i] = 0
        for i in range(zero, zero+one):
            nums[i] = 1
        for i in range(zero+one, zero+one+two):
            nums[i] = 2