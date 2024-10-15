class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        
        counter_list = []
        counter = 0
        
        for num in nums:
            if num is 1: 
                counter += 1
            else:
                counter_list.append(counter)
                counter = 0
        
        counter_list.append(counter)
        max_con = max(counter_list)
        return max_con