class Solution:
    def subsequenceCount(self, nums):
        n, mod = len(nums), 10**9+7 

        even, odd = [0]*n, [0]*n      

        if nums[0]%2 == 0:
            even[0] = 1 
        else:
            odd[0] = 1 

        for i in range(1,n):
            if nums[i]%2 == 1:
                odd[i] = (even[i-1] + odd[i-1] + 1)%mod
                even[i] = (odd[i-1] + even[i-1])%mod
            else:
                odd[i] = 2*odd[i-1]%mod
                even[i] = (2*even[i-1] + 1)%mod 

        return odd[-1]%mod