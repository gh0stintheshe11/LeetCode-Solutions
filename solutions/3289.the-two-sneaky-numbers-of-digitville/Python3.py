class Solution:
    def getSneakyNumbers(self, nums):
        from collections import Counter
        
        count = Counter(nums)
        result = [num for num, freq in count.items() if freq == 2]
        
        return result