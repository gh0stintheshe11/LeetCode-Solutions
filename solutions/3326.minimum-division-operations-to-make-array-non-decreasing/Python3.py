class Solution:
    def minOperations(self, nums):
        def function(x):
            v, max_val = int(math.sqrt(x))+1, 1 

            for i in range(1,v):
                if x%i == 0:
                    if x//i != x:
                        max_val = max(max_val,x//i)

            return max_val 

        n, count = len(nums), 0 

        for i in range(n-2,-1,-1):
            if nums[i] > nums[i+1]:
                val = nums[i]//function(nums[i])
                if val > nums[i+1]:
                    return -1 
                else:
                    nums[i] = val
                    count += 1 

        return count