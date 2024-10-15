class Solution(object):
    def findNumbers(self, nums):
        
        counter = 0
        for num in nums:
            if (len(str(num))%2) is 0: 
                counter +=1
        return counter
                
        