class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = []
        B = 32
        def get(i): # get smallest j s.t. j|j+1==i
            prefix = 0
            for b in range(B - 1, -1, -1):
                prefix |= i & (1 << b)
                if prefix > 0 and prefix | (prefix - 1) == i:
                    return prefix - 1
            return -1

        for i in range(N):
            ans.append(get(nums[i]))
        return ans